"""
Implements the rules of the MU puzzle
"""

def rule1(start_str: str) -> list[str]:
  """
  You can add a U to any string ending in I: xI --> xIU
  """
  # TODO: implement
  return []

def rule2(start_str: str) -> list[str]:
  """
  If you have Mx, you can create Mxx: Mx --> Mxx
  """
  # TODO: implement
  return []

def rule3(start_str: str) -> list[str]:
  """
  You can replace III with U: xIIIy --> xUy
  """
  # TODO: implement
  return []

def rule4(start_str: str) -> list[str]:
  """
  You can delete UU from a string: xUUy --> xy
  """
  # TODO: implement
  return []

# Provide a way to get all the rules in one object
rules = [rule1, rule2, rule3, rule4]
