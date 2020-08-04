from autoneo import builder
import os, os.path, subprocess

current_path = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    setup_script = os.path.join(current_path, "setup.sh")

    config_file = os.path.join(current_path, "config.json")
    data_dir = os.path.join(current_path, "sources")
    query_dir = os.path.join(current_path, "query")
    csv_dir = os.path.join(current_path, "csv")

    if os.path.exists(data_dir) and len(os.listdir(data_dir)) == 0:
        print("Running setup script to download database files.")
        subprocess.run([
            setup_script
        ])

    builder.build(config_file, data_dir, query_dir, csv_dir)