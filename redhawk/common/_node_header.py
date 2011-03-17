""" Node Classes.

    This file is AUTO GENERATED from
      node_cfg.yaml using _ast_gen.py
    The header is stored in node_header.py
"""

import writers.scheme_writer as S

import copy
import pprint

# A dictionary of allowed operators, and their arity.
ALLOWED_OPERATORS = {
     'UNARY_MINUS'         : ('-', 1)
    ,'UNARY_PLUS'          : ('+', 1)
    ,'SIZE_OR_LEN'         : ('size-or-len-of', 1)

    ,'MULTIPLY'            : ('*', 2)
    ,'ADD'                 : ('+', 2)
    ,'MINUS'               : ('-', 2)
    ,'DIVIDE'              : ('/', 2)
    ,'FLOOR_DIVIDE'        : ('//', 2)
    ,'POWER'               : ('power', 2)
    ,'MOD'                 : ('mod', 2)
    ,'LSHIFT'              : ('lshift', 2)
    ,'RSHIFT'              : ('rshift', 2)
    ,'BITWISE_OR'          : ('bitwise-or', 2)
    ,'BITWISE_XOR'         : ('bitwise-xor', 2)
    ,'BITWISE_AND'         : ('bitwise-and', 2)
    ,'BITWISE_NOT'         : ('bitwise-not', 1)

    ,'BOOLEAN_AND'         :('and', 2)
    ,'BOOLEAN_OR'          : ('or', 2)
    ,'BOOLEAN_NOT'         : ('not', 1)
    ,'EQ'                  : ('eq', 2)
    ,'NOT_EQ'              : ('not-eq', 2)
    ,'IS'                  : ('is', 2)
    ,'IN'                  : ('in', 2)
    ,'LT'                  : ('<', 2)
    ,'LTE'                 : ('<=', 2)
    ,'GT'                  : ('>', 2)
    ,'GTE'                 : ('>=', 2)

    # TODO(spranesh): Should we make this an if-else?
    ,'TERNARY_IF'          : ('ternary-if', 3) 

    ,'PRE_INCREMENT'       : ('pre-increment', 1)
    ,'POST_INCREMENT'      : ('post-increment', 1)
    ,'PRE_DECREMENT'       : ('pre-decrement', 1)
    ,'POST_DECREMENT'      : ('post-decrement', 1)
    ,'ADDRESS_OF'          : ('addr-of', 1)
    ,'POINTER_DEREFERENCE' : ('dereference-ptr', 1)

    ,'ATTRIBUTE_INDEX'     : ('.', 2)
    ,'ARROW'               : ('->', 2)
    ,'TYPE_CAST'           : ('cast', 2)
}


def ExpandList(li, f):
  """ Recursively expands a list li as follows:
        For element e in the list, li:
          * If e is a list, call ExpandList(li, f) recursively.
          * If e is a Node, expand it (into a list),
              by calling ExpandList(f(e), f)"""
  if type(li) is not list:
    return

  for (i, e) in enumerate(li):
    if type(e) is list:
      li[i] = ExpandList(li[i], f)
    elif isinstance(e, Node):
      li[i] = f(e)
      if type(li[i]) is list:
        li[i] = ExpandList(li[i], f)
  return li


class Node:
  """A Parse Tree Node."""
  def __init__(self):
    raise NotImplementedError("Node is an Abstract Class.")
    return

  def __repr__(self):
    return self.ToStr()

  def __str__(self):
    return self.ToStr()

  def MakeCopy(self):
    return copy.deepcopy(self)

  def GetChildren(self):
    raise NotImplementedError("Base Node Class!")

  def ToStr(self):
    return S.WriteToScheme(self)

  def GetSExp(self):
    raise NotImplementedError("Base Node Class!")

  def GetRecursiveSExp(self):
    return ExpandList(self.GetSExp(), lambda x: x.GetSExp())

  def GetAttributes(self):
    """ Return the attributes of the class as a 
    pair - (class-name, dictionary-of-attributes). """
    d = {}
    d['tags'] = []
    for x in dir(self):
      if 'a' <= x[0] <= 'z':
        d[x] = getattr(self, x)
    return (self.__name__.__class__, d)

  def GetXMLAttributes(self):
    return self.GetAttributes()

  def GetJSONAttributes(self):
    return self.GetAttributes()

  def GetDotAttributes(self):
    return self.GetAttributes()

