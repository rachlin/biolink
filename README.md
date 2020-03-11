# biolink
Biolink: A database of networked biological knowledge

The goal of biolink is to create a multi-model database to support queries on biological knowledge in the domains of genes, proteins, diseases, clinical trials, pathways, functional annotations (GO), bioassays, and compounds (Pubchem). Biolink can also serve as a nomenclature translation service.

### Links

- Check out the [API Documentation](./doc/api/endpoints.md) for how to use the API
- Read the [Progress Report](./doc/Biolink.pdf) for a comprehensive review of the progess we've made so far, and our goals for next steps
- See the [process documentation](./doc/process.md) for a less formal, more detailed account of the work we've done.

### Installation & Setup (Coming Soon)
We're working to make an easily configurable set up process, one that also helps with creating the neo4j database as well.


#### Setting up the Database

- Setup Neo4j (set up your user credentials)
- Start Neo4J

        $ git clone https://github.com/rachlin/biolink
        $ cd biolink
        $ git checkout dev-p2p
        $ ./setup.sh
        $ cd data
        ------
        $ conda create --name biolink_data_tool python=3.7.0
        $ conda activate biolink_data_tool
        ------
        $ python db.py
    

#### Setting up the back end

        $ cd biolink/app/api
        $ conda create --name biolink python=3.7.0
        $ conda activate biolink
        $ pip install -r requirements.txt


#### Setting up the front end

        $ cd biolink/app/client-app
        $ nvm use 12.13.1
        $ npm install
        $ npm start?


Current stack: Neo4J, Python (Flask), ReactJS
