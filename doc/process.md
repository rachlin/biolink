# This doc serves as a log of our research process

## 10/1 - 10/7 - Exploring Disgenet

We begin our exploration of what data is available to us - having decided to start with a well-defined scope, we settled upon Disgenet -- a database of disease gene associations.

The tables of interest to us at the moment are:
    - `geneDiseaseNetwork` - 
    - `geneAttributes` -
    - `diseaseAttributes` - 

### Data Info

While there are some attributes in these tables that are self explanatory, it's good to clarify and consolidate that information. We'll do a table-by-table analysis, also pulling in information from Disgenet's [database documentation](http://www.disgenet.org/dbinfo)

Reading their documentation, it's clear that they've taken great care when pulling from data sources, and have considered the issues that may arise when different databases store the same information differently. 

#### `geneAttributes`

- geneNID - Disgenet's own internal gene identifier
- geneId - NCBI Entrezgene identifier (When pulling from other data sources, Disgenet converts those that use "HGNC symbols and Uniport accession numbers" (other ways of identifying genes) to their appropriate NCBI Entrezgene identifiers. It's clear they're looking at a wide net of data.)
- geneName - gene symbol (entrez gene)
- uniprotId - "the Uniprot accession" - can search for protein associated with gene in Uniprot using this attribute
- Z - All are 0 (`select DISTINCT Z from geneAttributes;`)-
- P - All are 0 (`select DISTINCT P from geneAttributes;`)- possibly should be Panther protein class label
- pLI  - probability of being loss-of-function intolerant accoring to [GNOMAD](http://gnomad.broadinstitute.org/), the Genome Aggregation Database.
- DSI - [Disease Specificity Index](http://www.disgenet.org/dbinfo#section33) - reflects the size of the set of diseases the gene is associated with - ranges from 0.25 to 1. Low DSI means associated with more, high means associated with less. No DSI means gene is associated with only phenotypes.
- DPI - [Disease Pleiotropy Index](http://www.disgenet.org/dbinfo#section34) - similar to DSI, but considers that the diseases associated with a gene may be similar (belong to the same MeSH disease class) or completely different ones. DPI reflects the number of unique disease classes a gene is associated with - ranges from 0 to 1. (There are 29 unique disease classes in Disgenet). Low DPI means more of the associations are from the same set of disease classes, High DPI means the gene has associations that span more disease classes. No DPI value means the gene is associated only to phenotypes or associated diseases do not map to any MeSH classes.

#### `diseaseAttributes`
- diseaseNID - Disgenet's own internal gene identifier
- diseaseId - UMLS CUIs
- diseaseName - from the [UMLS Metathesaurus](https://www.nlm.nih.gov/research/umls/)
- type - phenotype, group, disease
    - disease: An entry that maps to following semantic types:
        - Disease or Syndrome
        - Neoplastic Process
        - Acquired Abnormality
        - Anatomical Abnormality
        - Congenital Abnormality
        - Mental or Behavioral Dysfunction 
    - phenotype: An entry that maps to the following semantic types:
        - Disease or Syndrome
        - Neoplastic Process
        - Acquired Abnormality
        - Anatomical Abnormality
        - Congenital Abnormality
        - Mental or Behavioral Dysfunction 
    - group: A disease entry that refers to the one of the following disease groups:
        - Cardiovascular Diseases
        - Autoimmune Diseases
        - Neurodegenerative Diseases
        - Lung Neoplasms
    - Any entry considered as a disease but not strictly a disease, like those belonging to:
        - Gene or Genome
        - Genetic Function
        - Immunologic Factor
        - Injury or Poisoning 
    are removed from Disgenet

#### diseaseClass

Represents the 29 [MeSH](https://meshb.nlm.nih.gov/treeView) classes of diseases

- diseaseClassNID - Disgenet's own internal identifier for the MeSH class
- vocabulary - the vocabulary set that includes this disease class (only value is MSH for MeSH)
- diseaseClass - the MeSH identifier for the disease class
- diseasClassName - the name of the disease class



#### disease2class

Links diseases to their appropriate disease class

#### geneDiseaseNetwork

Mapping the gene disease associations and metadata about those associations

- NID - association id
- diseaseNID - the internal ID for the disease
- geneNID - the internal ID for the gene
- source - the original source reporting the association (`select distinct source from geneDiseaseNetwork`)
- association 
- association type
- sentence - a sentence from the publication describing the association (if none exists, then the title is used)
- pmid - the (first?) publication that reports the association's Pubmed Id
- score - GDA score, ranges from 0 to 1 - 1 is good
- EL - evidence level - measures the strength of evidence of a gene-disease relationship that correlates to a qualitative classification: "Definitive", "Strong"(High Evidence), "Moderate", "Limited" (Low Evidence), "Conflicting Evidence", or "No Reported Evidence"
- EI - evidence index - indicates the existence of contradictory results in publications supporting the associations. "1" -> all publications support association, "<1" -> there are some publications that assert there is no association. No EI value means the index hasn't been computed.
- year - most likely assumed to be the first time the association was reported


## 10/8 - 10/15 - Further Data Exploration, SQLite, Scripts, Neo4j

Now that we have a better idea of what data is in Disgenet, and what the attribbutes for each table actually mean, we had a couple things we wanted to explore.

### Gene Disease Association - Evidence Level and Evidence Index

The evidence index reflects the number of published results that refute an association (EI = 1 means no evidence exists that contradicts it). The evidence level reflects the strength of evidence behind an association.

Having an EI of 1 for an association means much less if there's very limited evidence supporting it, especially compared to an association with the same EI with strong evidence. 

We wanted to explore this and see the distribution of the associations in Disgenet, comparing EL and EI. We plot the correlation in inquiry1. Notice the evidence levels, which are traditionally Strings, have been converted to numeric values. The following is a map of EL to its number in our plot: 

    {
        'no reported evidence': 0, 
        'moderate': 1, 
        'strong': 2, 
        'limited': 3, 
        'definitive': 4, 
        'disputed': 5
    }

Looking at the figure ![](./Correlation_ELvEI.png), we can see that there are associations at all levels where there is no reported evidence for the association, but an EI has been calculated. We likely aren't too concerned with these associations. Looking at the majority of the remaining associations, we can see the associations with 'Strong Evidence' or 'Definitive Evidence' tend to have lower EIs, but we do see some outliers here. Perhaps then, these associations with strong evidence are simply those that have been studied more heavily, and as a result just happen to have more studies that refute them, pushing EI down. 

Does score of the association directly correlate to EI? Or EL? These remain to be explored.


### Gene Disease Associations - Converting RDBMS data to Neo4j in automated fashion

Now that we have a better understanding of the data in Disgenet, we look to see how we might model that data as a Graph.

The intuition we follow is:
    - An entity is a node
    - A join-table is a relationship

#### A First Attempt at defining a Schema

Looking at gene-disease associations, we see that Gene and Disease serve as different types of data. They can be the Node Types of our graph. Then each row in the gene table becomes a node of the Gene node type, and the same holds for diseases. 

But do we really need copy over all the properties of a gene from the relational model? There are quite a few. We determine that we don't actualyply need Disgenet's internal identifier for the gene, and our model might actually be more flexible with future integrations if we consider only the Entrez gene id for the gene. The gene name would also be easily searchable, so we keep that as well. Values Z and P are 0 across all genes, so these don't seem useful to us. However, pLI, DSI, and DPI do have actual values, and espcially the latter two are calculated metrics related to diseases a gene is associated with.

With diseases, we will use the diseaseId (the UMLS CUI labell for the disease) as its identification. The disease name is also useful to us, along with perhaps the type. It would be nice to also use the disease class, but not all diseases have a disease class associated with them. We could definitely consider incorporating this data at a later time.

Now associations are join tables! We can join the associations table on the disease and gene tables by the internal gene and disease identifiers, and instead display entrez gene Ids and UMLS CUIs. That information is key to understanding the association. Metrics like associationType, association, EL, EI, and score, can help us better understand the validity of the association, and perhaps allow us to present data differently based on that association weight. 

Now we know what properties matter to us, we export SQL data for Gene, Disease, Associatin to CSV. Then we create the Gene Node Type, importing each gene record as a node, create the Disease Node Type, each disease record as a node, and then create a new relation between Gene and Disease for each association. In order to automate this process, we've written scripts to do this for us.

At a later time, we might want look into building a tool to create different models of the data dynamically, further abstracting developers from the SQL->CSV->Neo4J conversion process.



