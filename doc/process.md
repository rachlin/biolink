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