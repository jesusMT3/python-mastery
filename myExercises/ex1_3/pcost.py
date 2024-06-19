import os

data_file = "../../Data/portfolio.dat"
paortfolio_cost = 0

with open(data_file, "r") as f:
    for line in f:
        input_data = line.split()
        paortfolio_cost += float(input_data[1]) * float(input_data[2])
       
        
print(paortfolio_cost)