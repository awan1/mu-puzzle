import signal
import sys

import solver
import graph

# A global flag for whether the program should stop executing
SHOULD_STOP = False


def _sigint_handler(sig, frame):
  global SHOULD_STOP
  print('SIGINT caught.')
  SHOULD_STOP = True


def display_solution(solution_graph: graph.Graph):
  print(solution_graph)


def main():
  """
  Runs the solution code until a solution is found or SIGINT is caught.
  """
  global SHOULD_STOP

  start_string = 'MI'
  end_string = 'MU'
  my_solution_graph = graph.Graph(start_string)
  my_solver = solver.Solver(my_solution_graph, start_string, end_string)

  # Catch SIGINT
  signal.signal(signal.SIGINT, _sigint_handler)

  while (not my_solver.solution_found and not SHOULD_STOP):
    try:
      my_solver.step()
    except RuntimeError as e:
      print('RuntimeError encountered: {}.'.format(e))
      SHOULD_STOP = True

  print('Finishing up.')
  display_solution(my_solution_graph)
  sys.exit(0)


if __name__ == "__main__":
  main()
