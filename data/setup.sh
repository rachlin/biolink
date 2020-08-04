#!/bin/bash
# Downloads the database dumps and places them in sources directory

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
DISGENET_DB_FILE_NAME="disgenet_2018.db"
GOA_HUMAN_PROTEIN_GAF_FILE_NAME="goa_human.gaf"

# install sqllite3, neo4j, wget, gunzip

# download disgenet into data/sources
wget  -P "${SCRIPT_DIR}/sources/" "http://www.disgenet.org/static/disgenet_ap1/files/current/${DISGENET_DB_FILE_NAME}.gz"
gunzip "${SCRIPT_DIR}/sources/${DISGENET_DB_FILE_NAME}.gz"

# download GO Annotations for Human (protein GAF)
wget -P "${SCRIPT_DIR}/sources/" "http://geneontology.org/gene-associations/${GOA_HUMAN_PROTEIN_GAF_FILE_NAME}.gz"
gunzip "${SCRIPT_DIR}/sources/${GOA_HUMAN_PROTEIN_GAF_FILE_NAME}.gz"