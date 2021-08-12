import random


class CityNode:
    def __init__(self, direction, weight):
        self.status = direction
        self.value = weight


city_list = {0: 'Podgorica,\n Montenegro',
             1: 'Vatican City,\n Vatican City',
             2: 'Addis Ababa,\n Ethiopia',
             3: 'Gaborone,\n Botswana',
             4: 'Vaduz,\n Liechtenstein'}
city_list2 = {0: 'Podgorica, Montenegro',
              1: 'Vatican City, Vatican City',
              2: 'Addis Ababa, Ethiopia',
              3: 'Gaborone, Botswana',
              4: 'Vaduz, Liechtenstein'}

city_num = len(city_list)

distance_list = [564,  # Podgorica & Vatican City
                 4173,  # Podgorica & Addis Ababa
                 7493,  # Podgorica & Gaborone
                 929,  # Podgorica & Vaduz
                 4469,  # Vatican City & Addis Ababa
                 7530,  # Vatican City & Gaborone
                 627,  # Vatican City & Vaduz
                 3997,  # Addis Ababa & Gaborone
                 5056,  # Addis Ababa & Vaduz
                 8152  # Gaborone & Vaduz
                 ]

adjacency_matrix = [
    [0, 1, 1, 1, -1],
    [-1, 0, 1, 1, -1],
    [-1, -1, 0, 1, 1],
    [-1, -1, -1, 0, 1],
    [1, 1, 0, 0, -1]
]  # default graph of your choice

# set up the graph
city_matrix = [[CityNode(0, -1) for j in range(city_num)] for i in range(city_num)]
for i in range(city_num):
    for j in range(i, city_num):
        if i != j:
            distance = distance_list.pop(0)
            city_matrix[i][j] = CityNode(adjacency_matrix[i][j], distance)
            city_matrix[j][i] = CityNode(adjacency_matrix[j][i], distance)
            distance_list.append(distance)

path = []


def reset():
    for i in range(city_num):
        for j in range(i, city_num):
            if i == j:
                city_matrix[i][j].status = 0
                city_matrix[i][j].value = -1
            else:
                city_matrix[i][j].status = adjacency_matrix[i][j]
                city_matrix[j][i].status = adjacency_matrix[j][i]
    path.clear()


def add_edge(departure, arrival):
    if city_matrix[departure][arrival].status == 0:
        city_matrix[departure][arrival].status = 1
        city_matrix[arrival][departure].status = -1

    else:
        print("The edge between " + city_list2[departure] + " and " + city_list2[arrival] + " already exists!")


def remove_edge(departure, arrival):
    if city_matrix[departure][arrival].status != 0:
        city_matrix[departure][arrival].status = 0
        city_matrix[arrival][departure].status = 0
    else:
        print("The edge between " + city_list2[departure] + " and " + city_list2[arrival] + " does not exists!")


def generate_random_edge():
    while True:
        random_edge = random.sample(range(city_num), 2)
        if city_matrix[random_edge[0]][random_edge[1]].status == 0:
            print(city_list2[random_edge[0]] + ' to ' + city_list2[random_edge[1]] + ' is added')
            break
    add_edge(random_edge[0], random_edge[1])
    return random_edge


def function():
    cycle = []
    vertex = 0
    starting_vertex = 0
    while not path:
        if vertex > 0:
            starting_vertex = generate_random_edge()[0]
            # Start from the outgoing vertex of the random edge instead of from the beginning to save time
        for vertex in range(starting_vertex, city_num):
            if city_matrix[vertex][vertex].status == 0 and city_matrix[vertex][vertex].value == -1:
                cycle_detection(vertex, vertex, cycle)
            city_matrix[vertex][vertex].status = 0
            city_matrix[vertex][vertex].value = -1
    print("Cycle detected: ")
    for each_cycle in path:
        print(each_cycle)


def cycle_detection(predecessor, vertex, cycle):
    city_matrix[vertex][vertex].status = 1  # Mark the current vertex as visited
    for adjacent in range(city_num):  # for every adjacent vertex
        if vertex != adjacent and city_matrix[vertex][adjacent].status == 1:  # Check if it is adjacent
            city_matrix[vertex][vertex].value = adjacent
            if city_matrix[adjacent][adjacent].status == 0:
                cycle_detection(predecessor, adjacent, cycle)
            elif city_matrix[adjacent][adjacent].status == 1:  # The adjacent vertex has been visited, cycle detected
                form_cycle(adjacent, cycle)
    if city_matrix[vertex][vertex].value == -1 or city_matrix[predecessor][predecessor].value == vertex:
        city_matrix[vertex][vertex].status = -1
    else:
        city_matrix[vertex][vertex].status = 0


def form_cycle(vertex, cycle):
    stop = vertex
    while not cycle.__contains__(vertex):
        cycle.append(vertex)
        vertex = city_matrix[vertex][vertex].value
    if vertex == stop:
        cycle.append(vertex)
        path.append(cycle.copy())
        cycle.clear()
    else:
        print("Hehe, weird right?")


function()
