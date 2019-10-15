#!/bin/bash

rm -rf csv
mkdir csv

sqlite3 -header -csv "sources/disgenet_2018.db" < "sql/export_gene.sql" > "csv/gene.csv"
sqlite3 -header -csv "sources/disgenet_2018.db" < "sql/export_disease.sql" > "csv/disease.csv"
sqlite3 -header -csv "sources/disgenet_2018.db" < "sql/export_association.sql" > "csv/association.csv"

cat cypher/import_csv.cypher | sudo cypher-shell -u neo4j -p admin
# if neo4j prevents you from importing from outside of files theres a line you have to comment out in conf
# which constrains external imports.