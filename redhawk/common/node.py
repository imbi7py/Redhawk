""" The Node Class. """

import util

import copy

class Node:
  """ Signifies a node in the parse tree."""
  def __init__(self):
    raise NotImplementedError("Node is an Abstract Class.")
    return

  def __repr__(self):
    return self.ToStr()

  def __str__(self):
    return self.ToStr()

  def ToStr(self):
    """ Should return a list of lines, which will be indented by the
    whitespace argument using a function decorator."""
    raise NotImplementedError("Not implemented for the Base Node Class.")

class Constant(Node):
  def __init__(self, position, value, type=None):
    self.value = value
    self.type = type
    self.position = position
    return
  
  @util.ConvertToStringWithIndent
  def ToStr(self, indent_level=0):
    return ["constant", str(self.value), self.type]

class Return(Node):
  def __init__(self, position, expr):
    self.position = position
    self.return_expression = expr
    return

  @util.ConvertToStringWithIndent
  def ToStr(self, indent_level=0):
    return ["return", self.return_expression]
