import sqlite3
import neo4j
import os
import os.path

dir_path = os.path.dirname(os.path.realpath(__file__))

def get_one_gene_sql():
    """
    Proof of Concept:
    gene attributes -   1636	2261	FGFR3	fibroblast growth factor receptor 3	0.0	0.0	1.8338e-05	0.417	0.759
    1636  = disgenet id for gene
    """
    conn = sqlite3.connect(os.path.join(dir_path, "sources/disgenet_2018.db"))
    c = conn.cursor()
    c.execute('SELECT * FROM geneAttributes WHERE geneNID=1636')
    return c.fetchone()

def get_one_disease_sql(diseasenid):
    conn = sqlite3.connect(os.path.join(dir_path, "sources/disgenet_2018.db"))
    c = conn.cursor()
    c.execute('SELECT * FROM diseaseAttributes WHERE diseaseNID=?', (diseasenid, ))
    return c.fetchone()

def get_diseases_associated_with_gene(genenid):
    conn = sqlite3.connect(os.path.join(dir_path, "sources/disgenet_2018.db"))
    c = conn.cursor()
    return c.execute('SELECT * FROM geneDiseaseNetwork WHERE geneNID=?', (genenid, ))

def put_stuff_in_neo4j():
    uri = "bolt://localhost:7687"
    driver = neo4j.GraphDatabase.driver(uri, auth=("neo4j", "password"))
    with driver.session() as session:
        gene_details = get_one_gene_sql()
        print(gene_details)
        associations_for_gene = get_diseases_associated_with_gene(gene_details[0])
        print(associations_for_gene)
        diseases_details = []
        for association in associations_for_gene:
            diseases_details.append(get_one_disease_sql(association[1]))
        
        print(diseases_details)
        create_query = "CREATE " + make_gene(gene_details) + "," + make_diseases([make_disease(d) for d in diseases_details]) + make_associations([make_association(a) for a in associations_for_gene])
        create_query = create_query[:-1]

        print(create_query)
        session.
        session.run(create_query)
        

def make_gene(details):
    return "(" + str(details[0]) + ":gene { name :" + str(details[2]) + "})"

def make_disease(details):
    return "(" + str(details[0]) + ":disease { name :" + str(details[2]) + "})"

def make_diseases(disease_queries):
    appended = ""
    for query in disease_queries:
        appended += query + ","
    return appended

def make_association(details):
    # return "(" + str(details[0]) + ":disease { score :" + str(details[8]) + "})"
    return ""

def make_associations(assocation_queries):
    appended = ""
    for query in assocation_queries:
        appended += query + ","
    # return appended
    return ""

# def get_one disease_sql():

# def put_one_disease_neo():

put_stuff_in_neo4j()