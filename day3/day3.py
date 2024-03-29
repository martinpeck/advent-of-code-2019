def calculate_distance(route1, route2):

    route1_locations = perform_moves_for_route(route1)
    route2_locations = perform_moves_for_route(route2)

    route1_set = set(route1_locations)
    route2_set = set(route2_locations)

    common_locations = route1_set.intersection(route2_set)

    shortest_distance = None
    shortest_steps = None

    for location in common_locations:
        distance = abs(location[0]) + abs(location[1])
        if not shortest_distance or distance < shortest_distance:
            shortest_distance = distance

        route1_steps = route1_locations.index(location) + 1
        route2_steps = route2_locations.index(location) + 1
        total_steps = route1_steps + route2_steps

        if not shortest_steps or total_steps < shortest_steps:
            shortest_steps = total_steps

    return shortest_distance, shortest_steps


def perform_moves_for_route(route):

    locations = []
    new_location = (0, 0)
    for move in route:
        new_locations = perform_move(new_location, move)
        locations.extend(new_locations)
        new_location = new_locations[-1]

    return locations


def perform_move(current_position, move):

    new_locations = []
    direction = move[0]
    distance = int(move[1:])

    new_position = current_position

    for iteration in range(distance):

        if direction == "U":
            new_position = (new_position[0], new_position[1] + 1)
        elif direction == "D":
            new_position = (new_position[0], new_position[1] - 1)
        elif direction == "L":
            new_position = (new_position[0] - 1, new_position[1])
        elif direction == "R":
            new_position = (new_position[0] + 1, new_position[1])
        else:
            raise Exception(f"Illegal direction [{direction}]")

        new_locations.append(new_position)

    return new_locations


def load_routes(filepath):
    with open(filepath, "r") as file:
        route1_as_string = file.readline()
        route2_as_string = file.readline()

        return (
            convert_route_string_to_list(route1_as_string),
            convert_route_string_to_list(route2_as_string),
        )


def convert_route_string_to_list(route_string):
    return route_string.split(",")


def solve_part1():
    route1, route2 = load_routes("input.txt")
    distance, steps = calculate_distance(route1, route2)
    return distance


def solve_part2():
    route1, route2 = load_routes("input.txt")
    distance, steps = calculate_distance(route1, route2)
    return steps


def solve_all():
    print(f"*** {__file__} ***")
    print(f"Solution to part 1: {solve_part1()}")
    print(f"Solution to part 2: {solve_part2()}")


if __name__ == "__main__":
    solve_all()
