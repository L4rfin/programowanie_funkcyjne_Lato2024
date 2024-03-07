def analyze_data(data):
    match data:
        case (x, y):
            return f"Tuple with elements {x} and {y}"
        case [x, y, z]:
            return f"List with elements {x}, {y}, and {z}"
        case _:
            return "Unknown type"


print(analyze_data((1, 2)))
print(analyze_data([1, 2, 3]))
