import pulp
import json
from pulp import PULP_CBC_CMD
from LpProblem import boxSolver
import sys


# sets up the environment for the weights of items
weights = [] # weights of all items
volumes = [] # volumes of all items
W_max = 10000  # Max weight per box
V_max = 1260000  # Max volume per box
filtered_weights = [] # filtered weights due to scaling error
filtered_volumes = [] # filtered volumes due to scaling error


# Commandline Validation
if (len(sys.argv) <= 1) or (sys.argv[1] not in ["data_100_items.json", "data_1000_items.json",
                                          "data_10000_items.json", "data_100000_items.json"]):
    raise ValueError("Commandline argument error: " +
                     "Please enter one of the data_'number'_items file into the command line")

fileName = sys.argv # returns a list of 2 items -> [Arbitrary, data_chosen]

# Retrieves the data from the chosen file
with open (f"Data/{fileName[1]}", "r") as file:
    data = json.load(file)
    for item in data:
        weights.append(round(float(item["Weight"]), 1))
        volumes.append(round(float(item["Volume"])))


# filters all items which are volumes are too large to arrange
for item in volumes:
    if item < (V_max/3):
        filtered_volumes.append(item)
        index = volumes.index(item)
        item2 = weights[index]
        filtered_weights.append(item2)

# Chooses a delimiter to divide the filtered items into cases
# 100 items need only 1 case
if len(filtered_weights) < 100:
    items_per_case = len(filtered_weights)-1
else:
    items_per_case = 100


def main(filteredNum, case_weights, case_volumes, result, box_counter, case):
    for i in range(0, filteredNum):

        if (i % items_per_case == 0 and i != 0) or i == filteredNum-1:

            if i > items_per_case:
                weight = filtered_weights[i]
                volume = filtered_volumes[i]
                case_weights.append(weight)
                case_volumes.append(volume)

            case += 1
            case_items = len(case_weights)

            x, y, prob = boxSolver(case_items, case_weights, case_volumes, W_max, V_max)
            prob.solve(PULP_CBC_CMD(msg=False))
            print()
            print(f"CASE {case}")

            if pulp.LpStatus[prob.status] == 'Optimal':
                print(f"The number of items in this case is: {len(case_weights)}")
                total_boxes = sum(pulp.value(y[j]) for j in range(case_items))
                result += total_boxes
                print(f"Total boxes used: {int(total_boxes)}")

                for j in range(case_items):
                    if pulp.value(y[j]) == 1:
                        print(f"Box {box_counter} contains items: ", end="")

                        box_counter +=1
                        for p in range(case_items):
                            if pulp.value(x[p, j]) == 1:
                                print(f"Item {p + 1} ", end="")

                        print()
                case_weights = []
                case_volumes = []
            else:
                print(f"The number of items in this case is: {len(case_weights)}")
                print("No optimal solution found.")
        else:
            weight = filtered_weights[i]
            volume = filtered_volumes[i]
            case_weights.append(weight)
            case_volumes.append(volume)

    print()
    print()

    print(f"There are {round(result)} trucks being used.")
    print()
    print("It takes 2 hours 17 minutes from Sheffield to Newcastle")
    newResult = round(result) * 137.0
    hours = int(newResult/60)
    min = ((newResult/60) - hours) * 60
    print(f"The shortest time possible is {hours} hours {round(min)} minutes ")

filteredNum = len(filtered_weights)
case = 0
case_weights = []
case_volumes = []
result = 0
box_counter = 1

if __name__ == "__main__":
    main(filteredNum, case_weights, case_volumes, result, box_counter, case)