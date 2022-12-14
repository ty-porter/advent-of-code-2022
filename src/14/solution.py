from src.prompt import Prompt

START_X = 500
START_Y = 0

WALL = 1
SAND = 2

def dist(p1, p2):
  return (p1[0] - p2[0], p1[1] - p2[1])

def points_between(p1, p2):
  distance = dist(p1, p2)

  if distance[0] != 0:
    direction = -1 if distance[0] > 0 else 1
    return [(p1[0] - distance[0] - (i * direction), p1[1]) for i in range(abs(distance[0]) + 1)]
  else:
    direction = -1 if distance[1] > 0 else 1
    return [(p1[0], p1[1] - distance[1] - (i * direction)) for i in range(abs(distance[1]) + 1)]

def print_grid(grid_dict):
  min_x = min(grid_dict, key=lambda x: x[0])[0]
  min_y = min(grid_dict, key=lambda x: x[1])[1]

  max_x = max(grid_dict, key=lambda x: x[0])[0]
  max_y = max(grid_dict, key=lambda x: x[1])[1]

  for y in range(min_y, max_y + 1):
    row = ""
    for x in range(min_x, max_x + 1):
      if (x, y) in grid_dict and grid_dict[x, y] == WALL:
        row += '#'
      elif (x, y) in grid_dict and grid_dict[x, y] == SAND:
        row += 'o'
      else:
        row += '.'

    print(row)

def falling_sand(lines, floor_offset=0):
  cave = {}
  floor = None
  solid_floor = floor_offset != 0

  # breakpoint()

  for line in lines:
    prv_point = line[0]
    cave[prv_point] = WALL
    
    for point in line[1:]:
      for new_point in points_between(prv_point, point):
        if floor is None or floor < new_point[1]:
          floor = new_point[1]

        cave[new_point] = WALL

      prv_point = point
  
  floor += floor_offset

  # breakpoint()

  grid_full = False
  while not grid_full:
    stopped = False
    grain = [START_X, START_Y]
    while not stopped:
      downward_move = tuple([grain[0], grain[1] + 1])
      left_diagonal_move = tuple([grain[0] - 1, grain[1] + 1])
      right_diagonal_move = tuple([grain[0] + 1, grain[1] + 1])

      # if grain[1] >= 11:
      #   breakpoint()
      if downward_move not in cave:
        # Has hit the solid floor
        if (solid_floor and downward_move[1] <= floor - 1):
          if left_diagonal_move not in cave:
            grain = list(left_diagonal_move)
          elif right_diagonal_move not in cave:
            grain = list(right_diagonal_move)
          else:
            cave[tuple(grain)] = SAND
            stopped = True
        # Has fallen off the bottom
        elif downward_move[1] > floor:
          grid_full = True

          break
        else:
          grain = list(downward_move)
      else:
        if grain == [START_X, START_Y]:
          grid_full = True
          
          break
        elif left_diagonal_move not in cave:
          grain = list(left_diagonal_move)
        elif right_diagonal_move not in cave:
          grain = list(right_diagonal_move)
        else:
          cave[tuple(grain)] = SAND
          stopped = True

    # print(list(cave.values()).count(SAND))
    # print_grid(cave)
    
  return list(cave.values()).count(SAND)

def part_1_solution(lines):
  # return
  return falling_sand(lines)

def part_2_solution(lines):
  return
  return falling_sand(lines, 2)

TEST = [
  '498,4 -> 498,6 -> 496,6',
  '503,4 -> 502,4 -> 502,9 -> 494,9'
]

def transform_prompt():
  # return [[(int(part.split(",")[0]), int(part.split(",")[1])) for part in line.split(" -> ")] for line in TEST]
  return [[(int(part.split(",")[0]), int(part.split(",")[1])) for part in line.split(" -> ")] for line in Prompt.read_to_list(__file__)]
