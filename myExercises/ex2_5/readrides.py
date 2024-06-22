import csv
import collections

class RideData(collections.abc.Sequence):
    def __init__(self) -> None:
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []
        
    def __len__(self) -> int:
        return len(self.routes)
    
    def __getitem__(self, index) -> dict:
        
        return {'route': self.routes[range(index)],
                'date': self.dates[range(index)],
                'daytype': self.daytypes[range(index)],
                'rides': self.numrides[range(index)]}
    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])
        

def read_rides_as_dicts(filename: str) -> dict:
    """
    Read the bus ride data into four lists, representing columns
    """
    records = RideData()
    
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route, 
                'date': date, 
                'daytype': daytype, 
                'rides' : rides
                }
            records.append(record)
            
    return records
    
