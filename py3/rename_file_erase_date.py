import os
import glob
import re

file_list = glob.glob("/*.xml")

for file_path in file_list:
    file_name_ext = os.path.basename(file_path)
    file_name, ext = os.path.splitext( os.path.basename(file_name_ext))
    dirname = os.path.dirname(file_path)
    new_name = re.sub(r'(\d{4})-(\d{2})-(\d{2})T(\d{2})-(\d{2})-(\d{2})', "", file_name)
    new_path = dirname + '/' + new_name + '.' + ext
    os.rename(file_path, new_path)
