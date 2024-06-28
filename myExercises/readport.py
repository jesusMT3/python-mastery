import csv

# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                f'name' : row[0],
                f'shares' : int(row[1]),
                f'price' : float(row[2])
            }
            
            portfolio.append(record)
    return portfolio

def read_as_dict(filename):
    output = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            dict_row = {headers[i]: row[i] for i in range(len(headers))}
            
            output.append(dict_row)
    return output

def people_per_route_and_date(data, route_number: (int|str), date: str):
    route_number = str(route_number)
    
    data_filtered_per_route_number = [d for d in data if d['route'] == route_number]
    data_filtered_per_date = [d for d in data_filtered_per_route_number if d['date'] == date]
    return data_filtered_per_date
