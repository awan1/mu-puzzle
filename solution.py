import argparse
import signal
import sys

from solver import Solver
from graph import Graph

# A global flag for whether the program should stop executing
SHOULD_STOP = False


def _sigint_handler(sig, frame):
  global SHOULD_STOP
  print('SIGINT caught.')
  SHOULD_STOP = True


def display_solution(solution_graph: Graph):
  print(solution_graph)


def main(args):
  """
  Runs the solution code until a solution is found or SIGINT is caught.
  """
  global SHOULD_STOP

  start_string = 'MI'
  end_string = 'MU'
  solution_graph = Graph(start_string)
  solver = Solver(solution_graph, start_string, end_string)

  # Catch SIGINT
  signal.signal(signal.SIGINT, _sigint_handler)

  while (not solver.solution_found and not SHOULD_STOP):
    try:
      solver.step()
    except RuntimeError as e:
      print('RuntimeError encountered: {}.'.format(e))
      SHOULD_STOP = True

  print('Finishing up.')
  if (args.print_graph):
    print(solution_graph)
  sys.exit(0)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(
      description='Navigate through the MIU-system')
  parser.add_argument('-p',
                      '--print-graph',
                      dest='print_graph',
                      action='store_true',
                      help='print the graph on exit. Warning: can be large')
  args = parser.parse_args()
  main(args)
