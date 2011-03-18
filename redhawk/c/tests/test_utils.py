import redhawk.c.c_tree_converter as C
import redhawk.common.utils.misc_utils as U

import pycparser

import sys

RELATIVE_TEST_PATH = "c/tests/c_files/"
PICKLE_FILE = "c/tests/c_parsed.pickle"

def SetUp(filename, rel_path=RELATIVE_TEST_PATH):
  return U.ExtractASTFromDatabase(rel_path + filename,
                                  PICKLE_FILE,
                                  ParseC)
  

def ParseC(filename):
  """ Parse the file using pycparser and return the parsed AST."""
  try:
    tree = pycparser.parse_file(filename, use_cpp = True)
  except StandardError, e:
    sys.stderr.write(str(e))
    assert(False)
  return tree


def ConvertTree(t, filename=None):
  """ Convert the C-AST into the L-AST."""
  t.show()
  c = C.CTreeConverter(filename)
  ast = c.ConvertTree(t)
  print ast, "\n\n"
  return ast
