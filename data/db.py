import os
import os.path
import json
import shutil
import subprocess
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))

db_dir_path = os.path.join(dir_path, "sources")
query_dir_path = os.path.join(dir_path, "query")
csv_dir_path = os.path.join(dir_path, "csv")

def build():
    with open(os.path.join(dir_path, 'config.json')) as config_file:

        print("Loading Neo4j graph configuration...")
        config = json.load(config_file)

        nodes = config["nodes"]
        edges = config["edges"]

        if os.path.exists(csv_dir_path):
            shutil.rmtree(csv_dir_path)
        os.mkdir(csv_dir_path)

        for node in nodes:
            db_type = node["dataSource"]["dbType"]
            db_file_path = os.path.join(db_dir_path, node["dataSource"]["dbFile"])
            query_file_path = os.path.join(query_dir_path, node["dataSource"]["queryFile"])
            csv_file_path = os.path.join(csv_dir_path, node["entityType"] + ".csv")

            print("Exporting " + node["entityType"] + " info (i.e. " + str(node["properties"]) + ") from " + node["dataSource"]["dbFile"] + " into CSV file...")
            export_db_csv(db_type, db_file_path, query_file_path, csv_file_path)

            print("Loading CSV details for " + node["entityType"] + " into Neo4j...")
            load_db(node, csv_file_path)

        for edge in edges:
            db_type = edge["dataSource"]["dbType"]
            db_file_path = os.path.join(db_dir_path, edge["dataSource"]["dbFile"])
            query_file_path = os.path.join(query_dir_path, edge["dataSource"]["queryFile"])
            csv_file_path = os.path.join(csv_dir_path, edge["nodeType"] + ".csv")

            print("Exporting " + edge["edgeType"] + " info (i.e. " + str(edge["properties"]) + ") from " + edge["dataSource"]["dbFile"] + " into CSV file...")
            export_db_csv(db_type, db_file_path, query_file_path, csv_file_path)

            print("Loading CSV details for " + edge["edgeType"] + " into Neo4j...")
            load_db(edge, csv_file_path, isNode=False)
            

def export_db_csv(db_type, db_path, query_file_path, csv_file_path):
    if db_type == "sqllite3":
        sqllite_csv_path = os.path.join(dir_path, "sqlite_csv.sh")
        subprocess.run(
            [sqllite_csv_path, db_path, query_file_path, csv_file_path], 
            check=True, shell=False)
    elif db_type == "gaf":
        subprocess.run(
            ["python", query_file_path, db_path, csv_file_path],
            check=True, shell=True
        )
    else:
        return None


def load_db(entity, csv_file_path, isNode=True):
    if isNode:
        query = "USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM \"file:" + csv_file_path + "\" AS row "
        prop_dict = {}

        for prop in entity["properties"]:
            prop_dict[prop] = "row." + prop

        query += "CREATE (:" + entity["entityType"] + str(prop_dict) + ");"
        run_query(query)

        for index in entity["indices"]:
            query = "CREATE INDEX ON :" + entity["entityType"] + "(" + index+ ");"
            run_query(query)

    else:
        query = "USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM \"file:" + csv_file_path + "\" AS row "
        query += "MATCH (from:" + entity["fromNodeType"] + "{ " + entity["fromNodeKey"] + ": row." + entity["fromNodeKey"] +  "}) "
        query += "MATCH (to:" + entity["toNodeType"] + "{ " + entity["toNodeKey"] + ": row." + entity["toNodeKey"] + "}) "

        query += "MERGE (from)-[e:" + entity["edgeType"] + "]->(to) "

        query += "ON CREATE SET "

        for prop in entity["properties"]:
            if is_numeric(prop):
                query += "e." + prop + " = toFloat(row." + prop + ") "
            else:
                query += "e." + prop + " = row." + prop + " "
        
        query += ";"
        run_query(query)


def is_numeric(property):
    return property == "score"


def run_query(query_string):
    from neo4j import GraphDatabase
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "admin"))

    with driver.session() as session:
        results = session.write_transaction(
            call_tx, query_string
        )
        driver.close()
        return results


def call_tx(tx, query_string):
    result = tx.run(query_string)
    return result.data()


def delete():
    with open(os.path.join(dir_path, 'config.json')) as config_file:

        print("Loading Neo4j graph configuration...")
        config = json.load(config_file)

        nodes = config["nodes"]
        edges = config["edges"]


        for edge in edges:
            query = "MATCH (:" + edge["fromNodeType"] + ")-[e:" + edge["edgeType"] +"]->(:"+edge["toNodeType"]+") DELETE e;"
            run_query(query)

        for node in nodes:
            for index in node["indices"]:
                query = "DROP INDEX ON :" + node["entityType"] + "(" + index + ");"
                run_query(query)

            query = "MATCH (node:" + node["entityType"] + ") DELETE node;"
            run_query(query)


if __name__ == '__main__':
    args = sys.argv

    if "create" in args:
        build()
    elif "delete" in args:
        delete() 
    else:
        print("wtf")