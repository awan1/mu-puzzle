"""
Implements the rules of the MU puzzle
"""
import utils

def rule1(s: str) -> list[str]:
  """
  You can add a U to any string ending in I: xI --> xIU
  """
  if (s.endswith('I')):
    return [s + 'U']
  return []

def rule2(s: str) -> list[str]:
  """
  If you have Mx, you can create Mxx: Mx --> Mxx
  """
  if (s.startswith('M') and len(s) > 1):
    x = s[1:]
    return ['M' + x + x]
  return []

def rule3(s: str) -> list[str]:
  """
  You can replace III with U: xIIIy --> xUy
  """
  iii_indices = utils.find_indices_of_substring(s, 'III')
  def replace_3_chars_with_u_at_index(idx: int) -> str:
    return s[:idx] + 'U' + s[idx+3:]
  return [replace_3_chars_with_u_at_index(i) for i in iii_indices]

def rule4(s: str) -> list[str]:
  """
  You can delete UU from a string: xUUy --> xy
  """
  # It's possible that it's not necessary to use lookahead here, i.e. it's not
  # necessary to worry about overlaps, because `UUU` will convert to `U`
  # regardless of which `UU` is replaced. For convenience though, re-use this
  # method and then dedupe the return.
  uu_indices = utils.find_indices_of_substring(s, 'UU')
  def delete_2_chars_at_index(idx: int) -> str:
    return s[:idx] + s[idx+2:]
  # Deduplicate return
  return list(set(delete_2_chars_at_index(i) for i in uu_indices))

# Provide a way to get all the rules in one object
rules = [rule1, rule2, rule3, rule4]
