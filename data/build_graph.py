from autoneo import builder
import os, os.path

current_path = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    config_file = os.path.join(current_path, "config.json")
    data_dir = os.path.join(current_path, "sources")
    query_dir = os.path.join(current_path, "query")
    csv_dir = os.path.join(current_path, "csv")

    builder.build(config_file, data_dir, query_dir, csv_dir)