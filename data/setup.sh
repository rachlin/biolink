#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
DISGENET_DB_FILE_NAME="disgenet_2018.db"

# install sqllite3, neo4j, wget, gunzip

# download disgenet into data/sources
wget  -P "${SCRIPT_DIR}/sources/" "http://www.disgenet.org/static/disgenet_ap1/files/current/${DISGENET_DB_FILE_NAME}.gz"
gunzip "${DISGENET_DB_FILE_NAME}.gz"

# set-up local neo4j db

# run data.py - connect to sqllite db and neo4j, pull all *genes and diseases and associations* and add the ones not in neoj into neo4j



