from dataclasses import dataclass, field
from typing import Any

from queue import PriorityQueue

import graph
from rules import rules

Path = list[graph.Edge]
VertexAndPath = tuple[graph.Vertex, Path]


# Create a class that can associate vertices with a priority
@dataclass(order=True)
class QueueItem:
  priority: int
  item: Any = field(compare=False)


def create_queue_item_for_vertex_and_path(
    vertex_and_path: VertexAndPath) -> QueueItem:
  priority = len(vertex_and_path[0])
  return QueueItem(priority, vertex_and_path)


class Solver:
  solution_graph: graph.Graph = None
  solution_found: bool = False
  end_vertex: graph.Vertex = None

  # The queue holds (Vertex, Path) tuples, where Path represents the
  # sequence of Edges from the root Vertex to the given Vertex. A vertex can be
  # reached multiple ways, but we only care about the shortest Path.
  # We maintain set[Path] so that when we reach the end Vertex, we can output
  # the path taken without needing to traverse the graph again.
  # Using a priority queue allows us to first check vertices with shorter
  # strings.
  vertices_to_visit: "PriorityQueue[QueueItem]" = None

  def __init__(self, new_solution_graph: graph.Graph,
               start_vertex: graph.Vertex, end_vertex: graph.Vertex):
    self.solution_graph = new_solution_graph
    self.vertices_to_visit = PriorityQueue()
    self.vertices_to_visit.put(
        create_queue_item_for_vertex_and_path((start_vertex, [])))
    self.end_vertex = end_vertex

  def step(self):
    if (self.vertices_to_visit.qsize() == 0):
      raise RuntimeError("No vertices to visit")
    queue_item = self.vertices_to_visit.get()
    vertex, path = queue_item.item
    print("Vertex: " + vertex)
    for rule_number, rule in rules.items():
      new_vertices = rule(vertex)
      for new_vertex in new_vertices:
        if new_vertex == self.end_vertex:
          print('End vertex found!')
          self.solution_found = True
        if not self.solution_graph.has_vertex(new_vertex):
          # It would be slightly cleaner to create the edge and then add it to
          # the graph, but I've already committed to an Edge not having a start
          # point.
          new_vertex_and_path = (new_vertex, path + [(new_vertex, rule_number)])
          self.vertices_to_visit.put(
              create_queue_item_for_vertex_and_path(new_vertex_and_path))
        self.solution_graph.add_edge(source_vertex=vertex,
                                     target_vertex=new_vertex,
                                     annotation=rule_number)

    # print('Step done. Press ENTER to continue.')
    # input()
