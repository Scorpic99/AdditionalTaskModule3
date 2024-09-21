data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

general_sum = 0


def calculate_structure_sum(my_struct):
    global general_sum
    for i in range(len(my_struct)):
        if type(my_struct[i]) == list:
            if len(my_struct) != 0:
                calculate_structure_sum(my_struct[i])
                print()
        elif type(my_struct[i]) == tuple:
            if len(my_struct) != 0:
                calculate_structure_sum(my_struct[i])
                print()
        elif type(my_struct[i]) == str:
            general_sum += len(my_struct[i])
        elif type(my_struct[i]) == dict:
            my_keys = list(my_struct[i].keys())
            my_values = list(my_struct[i].values())
            for j in my_keys:
                if type(j) == str:
                    general_sum += len(j)
                elif type(j) == int:
                    general_sum += j
            for j in my_values:
                if type(j) == str:
                    general_sum += len(j)
                elif type(j) == int:
                    general_sum += j
        elif type(my_struct[i]) == set:
            if len(my_struct) != 0:
                calculate_structure_sum(my_struct[i])
                print()
        elif type(my_struct[i]) == int:
            general_sum += my_struct[i]


calculate_structure_sum(data_structure)
print(general_sum)

