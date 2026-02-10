# readrides.py

import csv
from collections import namedtuple


def read_rides_as_tuples(filename):
    """
    Read the bus ride data as a list of tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_dicts(filename):
    """
    Read the bus ride data as a list of dictionaries
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            # record = dict(zip(headings, row))
            record = {
                "route": row[0],
                "date": row[1],
                "daytype": row[2],
                "rides": int(row[3]),
            }
            records.append(record)
    return records


class Row:
    __slots__ = ["date", "daytype", "rides", "route"]

    def __init__(self, route, date, daytype, rides):
        self.rides = rides
        self.route = route
        self.date = date
        self.daytype = daytype


def read_rides_as_classes(filename):
    """
    Read the bus ride data as a list of Row instances.
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = Row(route=row[0], date=row[1], daytype=row[2], rides=int(row[3]))
            records.append(record)
        return records


def read_rides_as_namedtuples(filename):
    """
    Read the bus ride data as a list of named tuples
    """
    Row = namedtuple("Row", "route date daytype rides")
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = Row(route=row[0], date=row[1], daytype=row[2], rides=0)
            records.append(record)
        return records


if __name__ == "__main__":
    import tracemalloc

    tracemalloc.start()
    rows = read_rides_as_classes("../Data/ctabus.csv")
    print("Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory())
