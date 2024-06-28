def portfolio_cost(filename):
    price = 0
    with open(filename, "r") as f:
        for line in f:
            input_data = line.split()
            try:
                input_data[1] = float(input_data[1])
                input_data[2] = float(input_data[2])
            except:
                raise ValueError("Invalid type of data")
            
            price += input_data[1] * input_data[2]

    print(price)