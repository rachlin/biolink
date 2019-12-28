import sys
import csv

def write_csv(gaf_file_path, csv_file_path):
    with open(gaf_file_path) as gaf:
        with open(csv_file_path, 'w') as csv_file:
            csv_file_writer = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            go_terms = []
            for line in gaf:
                if line.startswith('UniProtKB'):
                    line_arr = line.split('\t')
                    go_term = line_arr[4]
                    
                    if go_term not in go_terms:
                        go_terms.append(go_term)

            csv_file_writer.writerows([ [go_term] for go_term in go_terms ])
            

def main():
    rest_args = sys.argv[1:]

    if len(rest_args) == 2:
        write_csv(rest_args[0], rest_args[1])
    

if __name__ == "__main__":
    main()