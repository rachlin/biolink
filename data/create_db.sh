#!/bin/bash

## Runs the SQL queries from specified files and exports results to CSVs
##    - Exports genes, disease, and associations (specifying diseaseId and geneId instead of diseaseNID and geneNID) CSV

rm -rf csv
mkdir csv

sqlite3 -header -csv "sources/disgenet_2018.db" < "sql/export_gene.sql" > "csv/gene.csv"
sqlite3 -header -csv "sources/disgenet_2018.db" < "sql/export_disease.sql" > "csv/disease.csv"
sqlite3 -header -csv "sources/disgenet_2018.db" < "sql/export_association.sql" > "csv/association.csv"


## Run a cypher query to create the Nodes and Relations in the Neo4J instance
## By default, Neo4j prevents using LOAD CSV (which is in our cypher query and helps read from CSV files) from
## files that aren't in the default imports directory. Moving these CSVs there can be a hassled. Instead,
## we can remove this constraint!
## Check your Neo4j instance's config file:
## - by default on Ubuntu, it's here: /etc/neo4j/neo4j.conf
## Look for: dbms.directories.import=/var/lib/neo4j/import . Comment that out and restart your Neo4j instance!
cat cypher/create_db.cypher | sudo cypher-shell -u neo4j -p admin