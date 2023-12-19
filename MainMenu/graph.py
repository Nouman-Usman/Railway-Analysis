import heapq


class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, node1, node2, weight):
        if node1 not in self.edges:
            self.edges[node1] = []
        if node2 not in self.edges:
            self.edges[node2] = []
        self.edges[node1].append((weight, node2))
        self.edges[node2].append((weight, node1))

    def dijkstra(self, start, end):
        queue = [(0, start)]
        seen = {start: 0}
        path = {}

        while queue:
            (cost, node) = heapq.heappop(queue)

            if node not in path:
                path[node] = cost

                # Check if the node is in the graph before iterating
                if node in self.edges:
                    for weight, neighbour in self.edges[node]:
                        old_cost = seen.get(neighbour, float('inf'))
                        new_cost = cost + weight
                        if new_cost < old_cost:
                            seen[neighbour] = new_cost
                            heapq.heappush(queue, (new_cost, neighbour))

        return path[end] if end in path else "No Path"


# Example usage
graph = Graph()

# Modify the locations list based on your "Locations.csv" file
locations = ['Lahore', 'Karachi', 'Quetta', 'Rawalpindi', 'Multan', 'Peshawar']

# Add edges
edges = [
    ('Lahore', 'Karachi', 5),
    ('Lahore', 'Quetta', 4),
    ('Lahore', 'Rawalpindi', 1),
    ('Quetta', 'Karachi', 3),
    ('Quetta', 'Multan', 5),
    ('Lahore', 'Peshawar', 6),
    ('Karachi', 'Peshawar', 8)
]

for edge in edges:
    graph.add_edge(*edge)

# Ensure all locations are present in the graph
for location in locations:
    if location not in graph.edges:
        print(f"Warning: {location} not found in the graph.")

# Now you can use the graph for Dijkstra's algorithm
# source = 'Rawalpindi'
# target = 'Karachi'
# shortest_path = graph.dijkstra(source, target)

# print(f"Shortest path from {source} to {target} is {shortest_path}")
