char_list = [
  [64, 91],
  [96, 123]
]

length = 2

def append(*ranges):
  global length
  for range in ranges:
    char_list.append(range)
    length += 1

list = char_list
