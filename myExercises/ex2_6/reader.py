import csv

def read_csv_as_dicts(file_path: str, col_types: list):
    with open(file_path) as f:
        rows = csv.reader(f)
        list_of_dictionaries = []
        header = next(rows)
        for row in rows:
            record = { name:func(val) for name, func, val in zip(header, col_types, row) }
            list_of_dictionaries.append(record)
            
    return list_of_dictionaries
            
rows = read_csv_as_dicts('../../Data/ctabus.csv', [str,str,str,int])
print(len(rows), rows[0])