import csv
from math import sqrt

def k_nearest_neighbours(path: str, center: str, k: int) -> list:
    """
    Count k nearest values to the given one (center), table
    should be represented as csv file where first line is empty /
    contains names of params, the table itself consists of rows where first
    column has value name and the others - some numeric data
    :param path: path to csv file
    :param center: name of key value
    :param k: k neighbours
    :return: dictionary where the key is center and value is a list of
            k nearest neighbours
    """
    distances = []
    with open(path, encoding='utf-8') as f:
        table = csv.reader(f)
        data = []
        for i in table:
            data.append(i)
    key = [i for i in data if i[0] == center][0]
    for i in range(1, len(data)):
        if data[i][0] == center:
            continue
        sum_sqrt_dist = 0
        for j in range(1, len(data[i])):
            sum_sqrt_dist += (float(key[j]) - float(data[i][j]))**2
        distances.append((data[i][0], sqrt(sum_sqrt_dist)))
    distances.sort(key=lambda x: x[1])
    return {center: [i[0] for i in distances if distances.index(i) < k]}

