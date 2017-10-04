import re
import sys
import os.path

PATH = sys.argv[1]

def visit(arg, dirname, filenames):
  for filename in filenames:
    if re.search("\d{2,4}x\d{2,4}", filename):
      print dirname + "\\" + filename
      # os.remove(dirname + "\\" + filename)

os.path.walk(PATH, visit, None)