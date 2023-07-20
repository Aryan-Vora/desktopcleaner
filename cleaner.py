import os
import shutil
current_dir = os.path.dirname(os.path.realpath(__file__))
result_dir = os.path.join(current_dir, 'cleaner')
i = 0
files = []
while os.path.exists(result_dir):
    result_dir += str(i)
    i += 1
os.makedirs(result_dir)

files = os.listdir(current_dir)
for file in files:
    if file == "cleaner.py" or os.path.isdir(file) or file[0] == ".":
        continue
    else:
        shutil.move(file, result_dir)
