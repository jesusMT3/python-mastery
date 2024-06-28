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

if __name__ == "__main__":
    data = "../../Data/ctabus.csv"
    bus_data = read_as_dict(data)
    
    # How many bus routes exist in Chicago?
    bus_routes = len({b['route'] for b in bus_data}) 
    print('Number of bus routes: ', bus_routes)
    
    # How many people rode the number 22 bus on February 2, 2011?  
    # What about any route on any date of your choosing?
    
    filtered_data = people_per_route_and_date(bus_data, route_number = '22', date = '02/22/2011')
    print(filtered_data)
    
    # What is the total number of rides taken on each bus route?
    from collections import Counter
    number_rides = Counter()
    for row in bus_data:
        route = str(row['route'])
        rides = int(row['rides'])
        number_rides[route] += rides
        
    print(number_rides)
    
    # What five bus routes had the greatest ten-year increase 
    # in ridership from 2001 to 2011?
    
    from datetime import datetime
    
    date_limit = datetime.strptime("01/01/2011", '%m/%d/%Y')
    print(date_limit)
    data_filtered_by_date = [d for d in bus_data if datetime.strptime(d['date'], '%m/%d/%Y') < date_limit]
    
    sorted_data = sorted(data_filtered_by_date, key=lambda x: x['rides'], reverse=True)

    top_five_routes = sorted_data[:5]
    print(top_five_routes)