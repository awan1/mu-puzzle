from typing import Any, Generic, Mapping, TypeVar

Vertex = TypeVar('V')
Annotation = TypeVar('A')
# An edge technically should have a start and an end, but we can omit the start
# if we only use edges in conjunction with the Graph.
Edge = tuple[Vertex, Annotation]
'''
class Vertex:
  """
  A specific implementation of a Vertex for the MU puzzle.

  This class could be generic but it helps to provide the priority method.
  """
  _value: str = None

  def __init__(self, value):
    self._value = value

  @property
  def priority(self):
    return len(self._value)
'''


class Graph:
  """
  A generic implementation of a Graph.

  Vertices are keys in a dict. The values are sets of Edges.

  An Edge has two pieces of information: the target Vertex, and an Annotation
  about the edge.

    {
      A: [ ( B, 1 ), ( C, 2 ) ],
      B: [],
      C: [],
    }

  This dict describes a graph with vertices A, B, and C. A is connected to B
  with edge 1, and to C with edge 2.
  """

  _data: Mapping[Vertex, set[Edge]] = dict()

  def __init__(self, root: Vertex):
    """Initialize the graph with a given root."""
    self._data[root] = set()

  def add_vertex(self, vertex: Vertex):
    """Add a vertex to the graph. No-op if it already exists."""
    if (vertex not in self._data):
      self._data[vertex] = set()

  def has_vertex(self, vertex: Vertex):
    return vertex in self._data

  def add_edge(self, source_vertex: Vertex, target_vertex: Vertex,
               annotation: Annotation):
    """Adds an edge.

    source_vertex must already be in the graph. target_vertex is added to the
    graph if it does not exist.
    """
    if not self.has_vertex(source_vertex):
      raise RuntimeError("Can't add edge: source vertex [{}] not in "
                         "graph".format(source_vertex))
    self.add_vertex(target_vertex)
    self._data[source_vertex].add((target_vertex, annotation))

  def __str__(self):
    return '\n'.join([str(x) for x in self._data.items()])
