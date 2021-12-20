from collections.abc import Iterable
import re

def find_indices_of_substring(s: str, substring: str) -> Iterable[int]:
  # Thanks to https://stackoverflow.com/a/4664889/2452770 for this
  # Find indices where the string "III" appears in s. Use lookahead to find
  # overlaps.
  return (m.start() for m in re.finditer('(?={})'.format(substring), s))
