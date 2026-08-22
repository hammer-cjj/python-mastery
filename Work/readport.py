import csv

from readrides import read_rides_as_dicts


# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                "name": row[0],
                "shares": int(row[1]),
                "price": float(row[2]),
            }
            portfolio.append(record)
    return portfolio


rows = read_rides_as_dicts("../Data/ctabus.csv")

# question 1
routes = set()
for row in rows:
    routes.add(row["route"])

print(len(routes))


# question 2
def rides_on_route_date(route, date):
    for row in rows:
        if row["route"] == route and row["date"] == date:
            print(f"Route: {row['route']}, Date: {row['date']}, Rides: {row['rides']}")
            break


rides_on_route_date("22", "02/02/2011")


# question 3
rides_per_route = {r["route"]: 0 for r in rows}
for row in rows:
    rides_per_route[row["route"]] += int(row["rides"])

for route, count in rides_per_route.items():
    print("%5s %10d" % (route, count))


# question 4
ride_per_route_2001 = {r["route"]: 0 for r in rows}
ride_per_route_2011 = {r["route"]: 0 for r in rows}
for row in rows:
    if row["date"].endswith("2001"):
        ride_per_route_2001[row["route"]] += int(row["rides"])
    elif row["date"].endswith("2011"):
        ride_per_route_2011[row["route"]] += int(row["rides"])

from collections import Counter

counter_2001 = Counter(ride_per_route_2001)
counter_2011 = Counter(ride_per_route_2011)

counter_increate = counter_2011 - counter_2001
five_greatest_increase = counter_increate.most_common(5)
print("Five routes with the greatest increase in rides from 2001 to 2011:")
for route, increase in five_greatest_increase:
    print(f"Route: {route}, Increase: {increase}")
