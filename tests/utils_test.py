from context import utils

class TestFindIndicesOfSubstring:
  def test_return_1(self):
    assert list(utils.find_indices_of_substring('AA', 'AA')) == [0]
    assert list(utils.find_indices_of_substring('xAA', 'AA')) == [1]
    assert list(utils.find_indices_of_substring('xAAy', 'AA')) == [1]

  def test_return_2(self):
    assert list(utils.find_indices_of_substring('xAAyAAz', 'AA')) == [1, 4]

  def test_return_overlapping(self):
    assert list(utils.find_indices_of_substring('AAA', 'AA')) == [0, 1]
    assert list(utils.find_indices_of_substring('AAAA', 'AA')) == [0, 1, 2]

