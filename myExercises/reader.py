import csv
import logging
log = logging.getLogger(__name__)

def read_csv_as_dicts(filename: str, types: list) -> list[dict]:
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        records = csv_as_dicts(rows, types)
    return records


def read_csv_as_instances(filename: str, cls: any) -> list[any]:
    '''
    Read CSV data into a list of instances
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        records = csv_as_instances(rows, cls)
    return records

def csv_as_dicts(lines: list, types: list, header: list = None) -> list[dict]:
    '''
    Read lines and convert them to a list of dictionaries
    '''
    dictionary_list = []
    if header is None:
        headers = next(lines)
    else:
        headers = header
    for idx, line in enumerate(lines):
        try:
            line_dict = { name: func(val) 
                        for name, func, val in zip(headers, types, line)}
            dictionary_list.append(line_dict)
        except ValueError as e:
            log.warning(f'Row {idx}: Bad row: {line}')
            log.debug(f'Reason: {e}')
    return dictionary_list

def csv_as_instances(lines: list, cls: any, header: list = None) -> list[any]:
    '''
    Read lines and convert to list of instances
    '''
    instances_list = []
    if header is None:
        headers = next(lines)
    else:
        headers = header

    for line in lines:
        instance = cls.from_row(line)
        instances_list.append(instance)
    return instances_list

def convert_csv(lines, func, *, headers = None):
    rows = csv.reader(lines)
    if headers is None:
        headers = next(lines)

    return map(lambda row: func(headers, row), rows)
    
def test1():
    file = '../Data/portfolio.csv'
    port = read_csv_as_dicts(file, [str, int, float])
    from stock import Stock
    port2 = read_csv_as_instances(file, Stock)
    print(port)
    print(port2)
    
def test2():
    def make_dict(headers, row):
        return dict(zip(headers, row))
    
    lines = open('../Data/portfolio.csv')
    converted_csv = convert_csv(lines, make_dict(headers = next(lines), row = lines))
    for line in converted_csv:
        print(line)
    
if __name__ == '__main__':
    ...