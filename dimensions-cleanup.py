import re
import sys
import os.path

PATH = sys.argv[1]

os.chdir(PATH)
for root, dirs, files in os.walk(".", topdown = False):
   for filename in files:
    if re.search("\d{2,4}x\d{2,4}", filename):
      print(os.path.join(root,filename))
      # os.remove(dirname + "\\" + filename)
  #  for name in dirs:
  #     print(os.path.join(root, name))
