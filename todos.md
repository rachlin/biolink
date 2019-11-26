# Task tracking

### 11/26 - 12/2

- [] - Write up a Paper
- [] - Next Steps for Next Semester:

		-Plot DSI vs DPI

			- colorcoded by disease class
			
			- ClientSide - Graph Plotting (Plotly JS) - https://plot.ly/javascript/sankey-diagram/

			- GO Annotations

			- Explore old biolink data dump

			- ETL Pipeline: https://neo4j.com/blog/rdbms-neo4j-etl-tool/

			- Config file stuff

### 11/19 - 11/26

- [x] - Client-side Table View
	- See resources: `https://codesandbox.io/s/github/tannerlinsley/react-table/tree/master/examples/sorting`
	- Done: See process docs for details
- [x] - Client-side Search functionality
	- Done: See process docs for details
- [x] - Think about potential update strategy
	- Done - Looked at https://neo4j.com/blog/rdbms-neo4j-etl-tool/
- [x] - Update process.md
- [ ] - Explore old biolink data dump
	- Revisit: See process docs for details
- [ ] - Start working on paper
	- Revisit: See process docs for details
- [ ] - Optional - GO Annotations
	- Revisit: See process docs for details


### 11/14 - 11/19

Being a bit ambitious with this week's tasks (may not get to many of these, but this is where I want to see growth in the project, to streamline how easy it is to add to the graph. Also want to look into how I can leverage our own API to add data to the database, so we may not need to wipe and rebuild everytime from scratch.)
 - [x] - Continue to work on Site/App - rendering explorative experience
	- Views for Gene/Disease
		- Related Disease/Gene
		- Similar Genes/Diseases by Association
	- Action Items:
		- React - Figure out how to maintain state for gene/disease list, so lists actually render asynchronously
		- API - Endpoints are good, but need to ensure that it's extensible, as the graph model changes, we want our queries to support that change
	- Done - Need to leverage react-table to render data, but have a clickbale view that allows navigation between genes and diseases that is extensible and will also work if we add GOAnnotations

- [x] - Extensibility in Adding New Data sources
	- Intuition: Use config.json as source of truth for not only building the graph database, but as a tool that the API can use as an understanding of schema
	- Done - Abstracted db calls, but still need to leverage config.json and make the ultimate source of truth

- [x] - Process documentation

	- Done - Updated with this week's progress

- [x] - Drafting paper

	- Done - Sections added, need to begin writing

- [ ] - Explore NCBI FTP Site Data (ftp://ftp.ncbi.nlm.nih.gov/gene/DATA/, ftp://ftp.ncbi.nlm.nih.gov/gene/GeneRIF/)
	- Easier way to get GO Annotations: Gene info, gene2go, gene2pubmed, gene_neighbors (might be interesting)




### 11/5 - 11/14

- [x] - Continue to work on Site/App - rendering explorative experience
	- Views for Gene/Disease
		- Related Disease/Gene
		- Similar Genes/Diseases by Association

- [x] - Process documentation

- [ ] - Explore NCBI FTP Site Data (ftp://ftp.ncbi.nlm.nih.gov/gene/DATA/, ftp://ftp.ncbi.nlm.nih.gov/gene/GeneRIF/)
	- Easier way to get GO Annotations: Gene info, gene2go, gene2pubmed, gene_neighbors (might be interesting)

### 10/29 - 11/5

- [x] - Interactive tools for exploring relations between genes and diseaes - this is a priority
	- For gene g:
		- list (should be clickable) of diseases involved
		- list of pathways involved in
	- Find similar genes based on disease overlap

	- Done: Partially rendering View for Genes; need to figure out routing in React

- [x] - Think about website architecture

	- Done - Current Setup:
		- REST API: powered by Flask, using neo4j and (explicit queries for DAO operations)
		- FrontEnd (Client): powered by React, make API calls to Flask

	- Next steps:
		- Graph API: powered by Flask, FlaskGraphQL, Graphene? Benefits: No need to make predetermined queries then
		- Revisit once the actual core of the project is complete.


- [x] - Process documentation

- [ ] - Explore NCBI FTP Site Data (ftp://ftp.ncbi.nlm.nih.gov/gene/DATA/, ftp://ftp.ncbi.nlm.nih.gov/gene/GeneRIF/)
	- Easier way to get GO Annotations -Gene info, gene2go, gene2pubmed, gene_neighbors (might be interesting)
	- REVISIT FOR Next week

- [ ] - GO Annotations - continue to explore
	 - REVISIT FOR Next week


### 10/22 - 10/29

- [x] - Exploring the data:
	
	- For each association (with either Asthma or Diabetes), get EL , EI, score, num of publibcations, (also number of publications with contradictory results)
	- genes are rows, columns will be values for either gene
	- come up 

	- Done (in part) - can view the details for each gene/disease association pai by pubmed id - REVISIT for next week

- [x] - Integrate (the correct version of) Gene Ontology Annotations [the one with genes]

	- Done (in part) - Added GO Annotations, need to plan way to add Add GO terms in a hierarchical way. Also need to figure out how to filter annotations not pertaining to genes (there are many focused on gene products or associations) - REVISIT for next week

- [ ] - Interactive tools for exploring relations between genes and diseaes
	- For gene g:
		- list (should be clickable) of diseases involved
		- list of pathways involved in
	- Find similar genes based on disease overlap
	- Look into CLI now, and maybe UI for generaing tables in the future

	- REVISIT for next week

- [ ] - If time permits, work more on paper:

	- [ ] Mendeley - Look for sources (at least 3) - integrating biological data and visuzalizing it as graph

	- REVISIT for next week

- [x] - Process documentation



### 10/15 - 10/22
- [x] - Show plot of EL vs. EI

	- See [here](./doc/process.md#gene-disease-association---evidence-level-and-evidence-index)

- [x] - Learn about stored procedures in Neo4j/Cypher
	
	- Function that takes a disease and generates a subgraph (genes associated with it)
	- bipartite graph

	- Done: See [here](./app/test.py) and [here](./app/proc.py)

- [ ] Pick and proceed with one of the following options:
	- [ ] - Interactive tools for exploring relations between genes and diseaes
		- For gene g:
			- list (should be clickable) of diseases involved
			- list of pathways involved in
		- Find similar genes based on disease overlap
		- Look into CLI now, and maybe UI for generaing tables in the future

	- [ ] - Integrating GO data

	- Revisiting next week

- [ ] A system for importing CSVs into Neo4j via a config file
	- we would provide different graph db configs and see which ones look better

- [x] - Begin writing paper - Abstract

	- see [here](./doc/paper.md)


### 10/8 - 10/15

- [x] See if I can manually create a neo4j instance(s) (via a script following a pattern specified in the email I received)
	- Next step: 
		- query for each model that shows why its better
		- overlapping genes for different diseases
		- A system for importing CSVs into Neo4j via a config file
		- we would provide different graph db configs and see which ones look better
		- Delivered - create_db.sh, export sql to csv scripts, cypher query to create nodes and relations in database

- [x] Understand correlation between evidence level and evidence index
	- find if any are high evidence level but low evidence index
	- scatterplot
	- Will show next week


### 10/1 - 10/7

- [x] Data familiarity - become more familiar with the attributes of the data

	- Some insightful queries:

		```
		select distinct association , count(*)
		from geneDiseaseNetwork
		where pmid != '\N'
		group by association;

		select year, count(*)
		from geneDiseaseNetwork
		group by year
		order by year;

		select diseaseName, count(*)
		from geneDiseaseNetwork g join diseaseAttributes d using (diseaseNID)
		where pmid != '\N'
		and association = 1
		group by diseaseName
		order by count(*) desc;
		```

	- data described in `process.md`

- [ ] Settle upon a schema for Neo4j, that's intuitive but allows for multi-modality

	- Revisit once we build a tool for coming up with different configs

- [ ] Github 

	- [x] - Actively make the repo a working document of our research

		- made `process.md`

### 9/24 - 9/30

- [x] Create Github todo doc for tracking progress

- [x] Mendeley

	- [x] Creating shareable libraries on Mendeley
		- Created a "group" titled 'jr_rr_2019_shared_library'

	- [x] Establishing a workflow for building a bibliography
		- Potential workflow:
			1. Find article
			2. Drag into 'to-review' folder
			3. Once reviewed, can move it to the root of the group

- [x] Neo4j

	- [x] Download Neo4j CE

	- [ ] Try to get disgenet in neo4j (or maybe just gene associations for one gene if size is a constraint 
		
		- revisiting this for next week

	- [x] Keep data off Github, look into writing scripts to download data at setup time, and parse and store accordingly in neo4j

	- [ ] Proof of Concept for getting stuff in Neo4j (local instance for now

		- revisiting this for next week

- [x] Find and keep O'Reilly Graph Database book as a resource
