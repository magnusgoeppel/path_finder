# Path Finder

## Description

This Python program allows users to find the shortest path between two stations in a network. It reads network data from a file containing the stations and the travel times between them. The program uses Dijkstra's algorithm to calculate the shortest path, total travel time, and the lines used. It is particularly suitable for finding routes in transportation networks such as city rail systems.

## Functionality

The program consists of several parts:

- `read_graph_from_file(filename)`: Reads the graph from a file.
- `dijkstra(graph, start, end)`: Finds the shortest path between two points.
- `print_path_details(cost, path, lines)`: Outputs details of the found path.
- `main()`: Main function that processes command-line arguments and initiates the search.

## Requirements

- Python 3.4 or higher

## Usage

To use the program, follow this command in the console or terminal:

```shell
python path_finder.py filename_graph start end 
```

- `filename_graph`: The file path to the graph file.
- `start`: Name of the start station.
- `end`: Name of the destination station.
