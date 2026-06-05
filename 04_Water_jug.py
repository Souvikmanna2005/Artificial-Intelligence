from collections import deque

def water_jug_problem_trace_path(jug1_capacity, jug2_capacity, target):
    # Queue stores (state, path)
    queue = deque([((0, 0), [(0, 0)])])
    visited = {(0, 0)}

    while queue:
        (jug1, jug2), path = queue.popleft()

        # Goal check
        if jug1 == target or jug2 == target:
            return path

        # Possible actions
        actions = [
            (jug1_capacity, jug2),  # Fill Jug 1
            (jug1, jug2_capacity),  # Fill Jug 2
            (0, jug2),              # Empty Jug 1
            (jug1, 0),              # Empty Jug 2

            # Pour Jug 2 -> Jug 1
            (
                min(jug1_capacity, jug1 + jug2),
                jug2 - (min(jug1_capacity, jug1 + jug2) - jug1)
            ),

            # Pour Jug 1 -> Jug 2
            (
                jug1 - (min(jug2_capacity, jug1 + jug2) - jug2),
                min(jug2_capacity, jug1 + jug2)
            )
        ]

        for action in actions:
            if action not in visited:
                visited.add(action)
                queue.append((action, path + [action]))

    return None


# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 2

path = water_jug_problem_trace_path(jug1_capacity, jug2_capacity, target)

if path:
    print("Path of states followed:")
    for state in path:
        print(state)
else:
    print("No solution found.")