#!/usr/bin/env python3
import os
import shutil
import sys

filename_arg = sys.argv[1]
filename = filename_arg+".py"

# Get path of this script and add the filename argument
script_dir = os.path.dirname(os.path.realpath(__file__))
src_path = os.path.join(script_dir, 'src', filename)
test_path = os.path.join(script_dir, 'src', '__tests__', "test_"+filename)
template_src = os.path.join(script_dir, 'template', 'src_file.py')
template_test = os.path.join(script_dir, 'template', 'test_file.py')

# Copy files from template dir and place the source file in src, and test file in src/__tests__
shutil.copy(template_src, src_path)
shutil.copy(template_test, test_path)

# Then replace "filename" with the argument that was passed
with open(test_path, 'r+') as file:
    file_contents = file.read()
    file_contents = file_contents.replace("filename", filename_arg)
    file.seek(0)
    file.write(file_contents)
    file.truncate()

print(f"Created {filename} in src and __tests__")
