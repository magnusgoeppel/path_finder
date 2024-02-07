import heapq
import sys


# Liest die Datei ein und erstellt den Graphen
def read_graph_from_file(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split(':')  # Trenne Linienname und Stationen
            line_name = line[0]
            stations = line[1].strip().split('"')[1::2]  # Extrahiere Stationsnamen
            times = line[1].strip().split('"')[2::2]  # Extrahiere Zeiten
            times = [int(times) if times else 0 for times in times]  # Konvertiere Zeiten zu Integer

            # Füge die Stationen und Zeiten zum Graphen hinzu
            for i in range(len(stations) - 1):
                if stations[i] not in graph:  # Stellt sicher, dass auch eingehende Kanten erstellt werden
                    graph[stations[i]] = []
                graph[stations[i]].append((stations[i + 1], times[i], line_name))
                if stations[i + 1] not in graph:
                    graph[stations[i + 1]] = []
                graph[stations[i + 1]].append((stations[i], times[i], line_name))
    return graph


# Berechnet den kürzesten Weg von Start zu Endpunkt
def dijkstra(graph, start, end):
    queue = []
    heapq.heappush(queue, (0, [start], []))  # Kosten, Pfad, benutzte Linien
    visited = set()
    while queue:
        (cost, path, lines) = heapq.heappop(queue)
        node = path[-1]
        if node == end:
            return cost, path, lines
        if node not in visited:
            visited.add(node)
            for neighbour, neighbour_cost, line in graph[node]:
                if neighbour not in visited:
                    total_cost = cost + neighbour_cost
                    heapq.heappush(queue, (total_cost, path + [neighbour], lines + [line]))
    return None


# Gibt den kürzesten Weg aus
def print_path_details(cost, path, lines):
    print(f'Der kürzeste Pfad von {path[0]} nach {path[-1]} ist:')
    current_line = lines[0] if lines else None
    print(f'Sie starten in {path[0]} mit der Linie {current_line}.')
    for i in range(1, len(path)):
        if i <= len(lines) and lines[i-1] != current_line:
            print(f'Umsteigen von {current_line} zu {lines[i-1]} in {path[i-1]}.')
            current_line = lines[i-1]
        print(f'{path[i-1]} - {path[i]} ({current_line})')
    print(f'Sie sind nun in {path[-1]} angekommen.')
    print(f'Die Gesamtfahrzeit beträgt {cost} Minuten.')


# Gibt den kürzesten Rundweg aus
def print_tsp_details(path, cost):
    print(f'Der kürzeste Rundweg, der bei {path[0]} beginnt und endet und alle Stationen besucht, ist:')
    for i in range(len(path) - 1):
        print(f'{path[i]} - {path[i+1]}')
    print(f'Die Gesamtfahrzeit beträgt {cost} Minuten.')


def main():

    if len(sys.argv) < 4 or len(sys.argv) > 4:
        print("Usage: python path_finder.py filename_graph start end")
        return

    filename_graph = sys.argv[1]
    start = sys.argv[2]
    end = sys.argv[3]

    graph = read_graph_from_file(filename_graph)

    cost, path, lines = dijkstra(graph, start, end)
    print_path_details(cost, path, lines)


if __name__ == "__main__":
    main()
