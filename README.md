# PathFinder

## Beschreibung

Dieses Python-Programm ermöglicht es dem Nutzer, den kürzesten Pfad zwischen zwei Stationen in einem Netzwerk zu finden. Es liest die Daten des Netzwerks aus einer Datei, die die Stationen und die Zeiten zwischen ihnen enthält. Das Programm verwendet den Dijkstra-Algorithmus, um den kürzesten Weg sowie die Gesamtfahrzeit und die benutzten Linien zu berechnen. Es eignet sich besonders für die Wegfindung in Verkehrsnetzwerken wie Stadtbahnsystemen.

## Funktionsweise

Das Programm besteht aus mehreren Teilen:

- `read_graph_from_file(filename)`: Liest den Graphen aus einer Datei.
- `dijkstra(graph, start, end)`: Findet den kürzesten Pfad zwischen zwei Punkten.
- `print_path_details(cost, path, lines)`: Gibt Details zum gefundenen Pfad aus.
- `main()`: Hauptfunktion, die die Befehlszeilenargumente verarbeitet und die Suche initiiert.

## Voraussetzungen

- Python 3.4 oder höher

## Benutzung

Um das Programm zu verwenden, folgen Sie diesem Kommando in der Konsole oder dem Terminal:

```shell
python path_finder.py filename_graph start end 
```
- filename_graph: Der Dateipfad zur Graphendatei.
- start: Name der Startstation.
- end: Name der Zielstation.
