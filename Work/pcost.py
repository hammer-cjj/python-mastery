with open("../Data/portfolio.dat", "r") as f:
    sum = 0.0
    for line in f:
        item = line.split()
        sum += int(item[1]) * float(item[2])
print("sum =", sum)
