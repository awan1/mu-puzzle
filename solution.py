import signal
import sys

import solver
import solution_graph

# A global flag for whether the program should stop executing
SHOULD_STOP = False

def _sigint_handler(sig, frame):
  global SHOULD_STOP
  print('SIGINT caught. Finishing up.')
  SHOULD_STOP = True

def display_solution(solution_graph: solution_graph.SolutionGraph):
  print(solution_graph)

def main():
  """
  Runs the solution code.
  """
  my_solver = solver.Solver()
  my_solution_graph = solution_graph.SolutionGraph()
  my_solver.solution_graph = my_solution_graph

  # Catch SIGINT
  signal.signal(signal.SIGINT, _sigint_handler)

  while (not my_solver.solution_found and not SHOULD_STOP):
    my_solver.step()
  # On loop end or SIGINT, display solution
  display_solution(my_solution_graph)

  sys.exit(0)

if __name__ == "__main__":
  main()
