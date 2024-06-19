def portfolio_cost(filename):
    price = 0
    with open(data_file, "r") as f:
        for line in f:
            input_data = line.split()
            try:
                input_data[1] = float(input_data[1])
                input_data[2] = float(input_data[2])
            except:
                raise ValueError("Invalid type of data")
            
            price += input_data[1] * input_data[2]

    print(price)

if __name__ == "__main__":
    data_file = "../../Data/portfolio.dat"
    portfolio_cost("../../Data/portfolio.dat")
    portfolio_cost("../../Data/portfolio2.dat")
    portfolio_cost("../../Data/portfolio3.dat")