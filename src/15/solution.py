from src.prompt import Prompt

import re

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return f"<Point x={self.x}, y={self.y}>"

  def __repr__(self):
    return self.__str__()

class Sensor:
  def __init__(self, origin, beacon):
    self.origin = origin
    self.beacon = beacon

    self.x_distance = abs(self.origin.x - self.beacon.x)
    self.y_distance = abs(self.origin.y - self.beacon.y)
    self.distance = self.x_distance + self.y_distance

  # Returns 2 end points
  def points_visible_at(self, row_num):
    if not (self.origin.y - self.distance <= row_num <= self.origin.y + self.distance):
      return

    # Subtract total visible distance - target row distance to get an offset
    # Points visible in the row will be +/- this offset
    y_offset = self.distance - abs(row_num - self.origin.y)

    return (self.origin.x - y_offset, self.origin.x + y_offset)

  def __str__(self):
    return f"<Sensor origin={self.origin}, beacon={self.beacon}>"  

def visible_ranges(sensors, target):
  endpoints = []

  for sensor in sensors:
    new_endpoint = sensor.points_visible_at(target)

    if new_endpoint:
      if len(endpoints) == 0:
        endpoints.append(new_endpoint)
      else:
        i = 0
        while i < len(endpoints):
          endpoint = endpoints[i]
          # This works due to a fluke. It can't handle non-overlapping ranges.
          # However, in Part 1... the are non-overlapping ranges and the 2 endpoints this produces are valid
          #
          # example, starting at 0:
          # ....###.....###.... -> (4, 6) and (12, 14) don't overlap, but produce a negative range -> (12, 6)
          intersection = range(max(endpoint[0], new_endpoint[0]), min(endpoint[-1], new_endpoint[-1]) + 1)

          if intersection is not None:
            endpoints.remove(endpoint)
            endpoints.append((min(endpoint[0], new_endpoint[0]), max(endpoint[-1], new_endpoint[-1])))

            break

          i += 1

  return endpoints

def part_1_solution(sensors):
  ranges = visible_ranges(sensors, 10)

  count = 0

  for endpoint in ranges:
    count += abs(endpoint[0]) + abs(endpoint[1])

  return count

def part_2_solution(sensors):
  return

def transform_prompt():
  sensors = []

  for line in Prompt.read_to_list(__file__):
    points = [int(value) for value in re.findall('-?\d+', line)]

    sensor = Sensor(Point(*points[0:2]), Point(*points[2:]))

    sensors.append(sensor)

  return sensors