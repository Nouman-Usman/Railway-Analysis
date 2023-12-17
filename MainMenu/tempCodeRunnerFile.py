source = 'Rawalpindi'
target = 'Karachi'
shortest_path = graph.dijkstra(source, target)

print(f"Shortest path from {source} to {target} is {shortest_path}")