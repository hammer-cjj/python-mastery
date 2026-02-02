def portfolio_cost(filename):
    """Compute the total cost of the portfolio."""
    with open(filename, "r") as f:
        sum = 0.0
        for line in f:
            try:
                item = line.split()
                sum += int(item[1]) * float(item[2])
            except ValueError as e:
                print("Couldn't parse:", line[:-1])
                print("Reason:", e)
    return sum


if __name__ == "__main__":
    print(portfolio_cost("../Data/portfolio.dat"))
