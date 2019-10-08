# Task tracking

### 10/8 - 10/16

- [ ] See if I can manually create a neo4j instance(s) (via a script following a pattern specified in the email I received)
	- query for each model that shows why its better
	- overlapping genes for different diseases

	- [ ] A system for importing CSVs into Neo4j via a config file
		- we would provide different graph db configs and see which ones look better

- [ ] Understand correlation between evidence level and evidence index
	- find if any are high evidence level but low evidence index
	- scatterplot

- [ ] Mendeley - Look for sources (at least 3) - integrating biological data and visuzalizing it as graph



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
