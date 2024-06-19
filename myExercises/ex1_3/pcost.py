import os

data_file = "../../Data/portfolio.dat"
price_list = []

with open(data_file, "r") as f:
    for line in f:
        input_data = line.split()
        price_line = {"Name": input_data[0],
                      "Price": round(float(input_data[1]) * float(input_data[2]), 2)}
        
        price_list.append(price_line)
        
print(price_list)