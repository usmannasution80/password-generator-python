def between(*args):
  if type(args[1]) is list:
    for values in args[1]:
      if between(args[0], values[0], values[1]):
        return True
    return False

  return args[0] > args[1] and args[0] < args[2]
