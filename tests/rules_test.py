from context import rules

# Note that these tests do not only test MIU-system strings. This is on purpose,
# to demonstrate the generality of the rules.

class TestRule1:

  def test_method_runs(self):
    rules.rule1('')

  def test_method_appends(self):
    assert rules.rule1('I') == ['IU']
    assert rules.rule1('xI') == ['xIU']

  def test_method_returns_empty(self):
    assert rules.rule1('Iy') == []
    assert rules.rule1('xIy') == []

class TestRule2:
  def test_method_runs(self):
    rules.rule2('')

  def test_method_appends(self):
    assert rules.rule2('Mx') == ['Mxx']
    assert rules.rule2('Mxy') == ['Mxyxy']
    assert rules.rule2('Mxyz') == ['Mxyzxyz']

  def test_method_returns_empty(self):
    assert rules.rule2('M') == []
    assert rules.rule2('xM') == []
    assert rules.rule2('xMy') == []

class TestRule3:
  def test_method_runs(self):
    rules.rule3('')

  def test_method_replaces_one(self):
    assert rules.rule3('III') == ['U']
    assert rules.rule3('xIII') == ['xU']
    assert rules.rule3('IIIy') == ['Uy']
    assert rules.rule3('xIIIy') == ['xUy']

  def test_method_replaces_with_multiple_options(self):
    assert rules.rule3('xIIIyIII') == ['xUyIII', 'xIIIyU']

  def test_method_replaces_with_overlapping(self):
    assert rules.rule3('IIII') == ['UI', 'IU']
    # Note that even with two possible replacements, one application of the rule
    # only does one replacement
    assert rules.rule3('IIIIII') == ['UIII', 'IUII', 'IIUI', 'IIIU']

  def test_method_does_not_replace(self):
    # the three 'I's must be adjacent
    assert rules.rule3('MIIUI') == []

class TestRule4:
  def test_method_runs(self):
    rules.rule4('')

  def test_method_deletes(self):
    assert rules.rule4('UU') == ['']
    assert rules.rule4('xUU') == ['x']
    assert rules.rule4('UUy') == ['y']
    assert rules.rule4('xUUy') == ['xy']

  def test_method_deletes_with_multiple_options(self):
    assert sorted(rules.rule4('xUUyUUz')) == sorted(['xyUUz', 'xUUyz'])

  def test_method_deletes_with_overlapping(self):
    # Deduplicates
    assert rules.rule4('UUU') == ['U']
    assert rules.rule4('UUUU') == ['UU']

  def test_method_does_not_delete(self):
    assert rules.rule4('U') == []
    assert rules.rule4('xUyU') == []
