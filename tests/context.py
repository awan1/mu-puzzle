import os
import sys
# Follows suggestion from https://docs.python-guide.org/writing/structure/#test-suite
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import rules
import utils
