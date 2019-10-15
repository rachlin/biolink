#!/bin/bash

rm -rf ../csv
mkdir ../csv

sqlite3 -header -csv "sources/disgenet_2018.db" < "sql/export_gene.sql" > "csv/gene.csv"
sqlite3 -header -csv "sources/disgenet_2018.db" < "sql/export_disease.sql" > "csv/disease.csv"
sqlite3 -header -csv "sources/disgenet_2018.db" < "sql/export_association.sql" > "csv/association.csv"
