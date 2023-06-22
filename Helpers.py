import json
import math


def updateJson(jsonData: dict, keyString: str, function) -> None:
  """
  Updates a nested JSON with a function.

  Args:
    jsonData: The JSON data to update.
    keyString: A string representing the keys in the JSON.
    function: A function that takes one argument and returns one value.

  Returns:
    The updated JSON data.
  """
  
  if not function:
    raise Exception("Modifying function should be provided")
  
  tokens = keyString.split(".")
  currentValue = jsonData
  for key in tokens[:-1]:
    if isinstance(currentValue, dict):
      currentValue = currentValue[key]
    elif isinstance(currentValue, list):
      currentValue = currentValue[int(key)]
    else:
      raise ValueError("The key {} is not valid".format(key))
  currentValue[tokens[-1]] = function(currentValue[tokens[-1]])

def prettifyFileSizes(size: str) -> str:
  """
  Human readable file size
  """
  if size == 0:
    return '0 bytes'
  if size == 1:
    return '1 byte'

  exponent = min(int(math.log(size, 1024)), 5)
  quotient = float(size) / 1024 ** exponent
  unit = ["bytes", "kB", "MB", "GB", "TB", "PB"][exponent]
  return "{:.4f} {}".format(quotient, unit)




