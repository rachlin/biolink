import os
import os.path
import json
import subprocess
import shutil

dir_path = os.path.dirname(os.path.realpath(__file__))

def read():
    with open(os.path.join(dir_path, 'config.json')) as config_file:
        config = json.load(config_file)

        nodes = config["Nodes"]
        edges = config["Edges"]


        db_dir_path = os.path.join(dir_path, "sources")
        sql_dir_path = os.path.join(dir_path, "sql")
        csv_dir_path = os.path.join(dir_path, "csv")

        shutil.rmtree(csv_dir_path)
        os.mkdir(csv_dir_path)

        for node in nodes:
            db_file_path = os.path.join(db_dir_path, node["DataSource"]["DatabaseFile"])
            sql_file_path = os.path.join(sql_dir_path, node["DataSource"]["QueryFile"])
            csv_file_path = os.path.join(csv_dir_path, node["NodeType"] + ".csv")

            subprocess.run(
                ["sqlite3", "-header", "-csv", db_file_path, "<", sql_file_path, ">", csv_file_path],
                check=True, shell=True)


read()