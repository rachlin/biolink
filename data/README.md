## Data Import Tool - Autoneo

We use autoneo, which makes it possible to define what the neo4j database will look like using a JSON format. See `config.json` for examples on how to add nodes and edges to the graph.


### Creating the database in neo4j using Autoneo

#### Requirements
To run this locally, ensure your neo4j instance allows external imports - this allows data imported as a csv to be loeaded into the graph database without needing to place it in the default import directory. 

To do this, go to the config file for your instance:
1. Comment out this line: `dbms.directories.import=import` (Add a `#`)
2. Uncomment this line: `#dbms.security.allow_csv_import_from_file_urls=true` (Remove the `#`)

#### Create DB
Using Python3, install all the requirements needed: `pip install -r requirements.txt`

Then run: `python build_graph.py`