class Prompt:
  def read(solution_path):
    f = open(solution_path.replace("solution.py", "prompt.txt"), "r")
    return f.read()

  def read_to_list(solution_path):
    f = open(solution_path.replace("solution.py", "prompt.txt"), "r")
    string = f.read()
    array = string.split("\n")

    return array
