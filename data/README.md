## Data Import Tool

This Python script makes it possible to define what the neo4j database will look like using a JSON format. See `config.json` for examples on how to add nodes and edges to the graph.

Current limitations:
    - Data import is only possible in an automated way from a SQLLITE 3 DB. Users are expected to provide a SQL script that extracts the desired fields (even for edges). Currently there is no way to automate adding new node types and then connect those nodes to existing nodes without manually using a CYPHER script.


### Creating the database in neo4j

#### Requirements
To run this locally, ensure your neo4j instance allows external imports - this allows data imported as a csv to be loeaded into the graph database without needing to place it in the default import directory. 

To do this, go to the config file for your instance:
1. Comment out this line: `dbms.directories.import=import` (Add a `#`)
2. Uncomment this line: `#dbms.security.allow_csv_import_from_file_urls=true` (Remove the `#`)

#### Create DB
Using Python3, install all the requirements needed: `pip install -r requirements.txt`

Then run: `python db.py create`

#### Delete DB
Sometimes you might want to delete the database (if you're testing the addition of a new node for example and messed up. (I have)). Run: `python db.py delete`
