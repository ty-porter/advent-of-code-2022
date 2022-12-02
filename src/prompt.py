class Prompt:
  def read(solution_path):
    f = open(solution_path.replace("solution.py", "prompt.txt"), "r")
    string = f.read()
    array = string.split("\n")

    return array
