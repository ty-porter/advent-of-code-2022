def read_prompt():
  f = open("prompt.txt", "r")
  string = f.read()
  array = string.split("\n")

  return array

values = read_prompt()

def part_1_solution(values):
  count = 0
  maximum = 0

  for value in values:
    if value != "":
      count += int(value)
    else:
      count = 0

    if maximum < count:
      maximum = count

  print(maximum)

def part_2_solution(values):
  count = 0
  counts = []

  for value in values:
    if value != "":
      count += int(value)
    else:
      count = 0

    counts.append(count)

    if len(counts) > 3:
      counts.remove(min(counts))

  print(sum(counts))

part_1_solution(values)
part_2_solution(values)