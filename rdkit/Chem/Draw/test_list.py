tests = [
  ("python", "UnitTestDraw.py", {}),
  ("python", "UnitTestSimilarityMaps.py", {}),
  ("python", "UnitTestIPython.py", {}),
]

longTests = []

if __name__ == '__main__':
  import sys

  from rdkit import TestRunner
  failed, tests = TestRunner.RunScript('test_list.py', 0, 1)
  sys.exit(len(failed))
