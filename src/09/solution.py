from src.prompt import Prompt

def distance(head, tail):
  x_dist = abs(head[0] - tail[0])
  y_dist = abs(head[1] - tail[1])

  return [x_dist, y_dist]

def move_part(head, tail, direction):
  dist = distance(head, tail)

  if dist[0] < 2 and dist[1] < 2:
    return tail

  # Diagonal, should move into rank or file H occupies
  if sum(dist) > 2:
    if dist[0] < dist[1]:
      tail[0] = head[0]
    else:
      tail[1] = head[1]

    # Recalculate distance after move
    dist = distance(head, tail)

  if direction == "U":
    tail[1] += 1
  elif direction == "D":
    tail[1] -= 1
  elif direction == "L":
    tail[0] -= 1
  elif direction == "R":
    tail[0] += 1

  return tail

def part_1_solution(instructions):
  H = [0, 0]
  T = [0, 0]
  visited = [tuple(T)]

  for direction, distance in instructions:
    for _ in range(distance):
      if direction == "U":
        H[1] += 1
      elif direction == "D":
        H[1] -= 1
      elif direction == "L":
        H[0] -= 1
      elif direction == "R":
        H[0] += 1
      else:
        raise Exception(f"{direction} is not a valid direction!")

      move_part(H, T, direction)

      if tuple(T) not in visited:
        visited.append(tuple(T))

  return len(visited)

def print_rope(rope):
  max_x = 10
  max_y = 10

  for position in rope:
    if position[0] > max_x:
      max_x = position[0]

    if position[1] > max_y:
      max_y = position[1]

  grid = [["." for x in range(max_x)] for y in range(max_y)]

  # print(grid)
  for i, position in enumerate(reversed(rope)):
    grid[position[1]][position[0]] = "H" if i == len(rope) - 1 else str(len(rope) - 1 - i)

  for row in reversed(grid):
    print("".join(row))

  print("\n")

def part_2_solution(instructions):
  rope = [[0, 0] for _ in range(10)]
  visited = [tuple(rope[-1])]

  for direction, distance in instructions:
    for _ in range(distance):
      if direction == "U":
        rope[0][1] += 1
      elif direction == "D":
        rope[0][1] -= 1
      elif direction == "L":
        rope[0][0] -= 1
      elif direction == "R":
        rope[0][0] += 1
      else:
        raise Exception(f"{direction} is not a valid direction!")

      new_rope = [rope[0]]

      for i, part in enumerate(rope):
        if i == 0:
          continue

        new_rope.append(move_long_part(rope[i - 1], part))

      rope = new_rope
      print_rope(rope)
      # breakpoint()

      if tuple(rope[-1]) not in visited:
        visited.append(tuple(rope[-1]))

  return len(visited)


def transform_prompt():
  test_data = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''.split("\n")

  return [[part if i == 0 else int(part) for i, part in enumerate(line.split(" "))] for line in test_data]
  # return [[part if i == 0 else int(part) for i, part in enumerate(line.split(" "))] for line in Prompt.read_to_list(__file__)]
