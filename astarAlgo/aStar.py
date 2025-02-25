import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position  # (x, y) coordinates
        self.parent = parent  # Parent node (to reconstruct path)
        self.g = g  # Cost from start node
        self.h = h  # Heuristic (estimated cost to goal)
        self.f = g + h  # Total cost

    def __lt__(self, other):
        return self.f < other.f  # Priority queue will use f-value

def heuristic(a, b):
    """Calculate Manhattan distance heuristic"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal):
    """A* search algorithm on a grid"""
    rows, cols = len(grid), len(grid[0])
    open_list = []
    closed_set = set()

    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Reverse path

        closed_set.add(current_node.position)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Move in 4 directions
            new_position = (current_node.position[0] + dx, current_node.position[1] + dy)

            if (0 <= new_position[0] < rows and 0 <= new_position[1] < cols and
                grid[new_position[0]][new_position[1]] == 0 and
                new_position not in closed_set):

                new_g = current_node.g + 1
                new_h = heuristic(new_position, goal)
                new_node = Node(new_position, current_node, new_g, new_h)

                heapq.heappush(open_list, new_node)

    return None  # No path found

# Example usage:
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)
path = a_star_search(grid, start, goal)

print("Path found:", path)
