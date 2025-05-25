import heapq

def dijkstra(graph, start):
    shortest_path = {node: float('inf') for node in graph}
    shortest_path[start] = 0
    priority_queue = [(0, start)]  # (вартість, вузол)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > shortest_path[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < shortest_path[neighbor]:
                shortest_path[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_path

# Орієнтований граф із вагами
graph_weighted = {
    'A': [('B', 1), ('C', 4), ('D', 2)],
    'B': [('A', 1), ('D', 3)],
    'C': [('A', 4), ('D', 5)],
    'D': [('A', 2), ('B', 3), ('C', 5)]
}

print("\nНайкоротші шляхи від A:", dijkstra(graph_weighted, 'A'))

