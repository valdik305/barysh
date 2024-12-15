def calculate_structure_sum(data):
    total_sum = 0
    def recursive_sum(data):
        nonlocal total_sum
        if isinstance(data, list):
            for item in data:
                recursive_sum(item)
        elif isinstance(data, tuple):
            for item in data:
                recursive_sum(item)
        elif isinstance(data, dict):
            for key, value in data.items():
                if isinstance(key, str):
                    total_sum += len(key)
                if isinstance(value, str):
                    total_sum += len(value)
                elif isinstance(value, (int, float)):
                    total_sum += value
                else:
                    recursive_sum(value)
        elif isinstance(data, str):
            total_sum += len(data)
        elif isinstance(data, (int, float)):
            total_sum += data
        elif isinstance(data, set):
            for item in data:
                recursive_sum(item)
        elif isinstance(data, frozenset):
            for item in data:
                recursive_sum(item)
    recursive_sum(data)
    return total_sum
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)