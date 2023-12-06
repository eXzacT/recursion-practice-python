#!/usr/bin/env python3
import os
import shutil
import sys

day = sys.argv[1]

# Get the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Create a new directory based on the project name
new_project_path = os.path.join(script_dir, day)
print(f'Trying to create: {new_project_path}')
os.makedirs(new_project_path, exist_ok=True)

# Copy all files from the template directory to the new project directory
for filename in os.listdir(os.path.join(script_dir, 'src/template')):
    shutil.copy2(os.path.join(script_dir, 'src/template',
                 filename), new_project_path)

# Replace placeholders in all files
for filename in os.listdir(new_project_path):
    with open(os.path.join(new_project_path, filename), 'r+') as file:
        file_contents = file.read()
        file_contents = file_contents.replace('{{day}}', day)
        file.seek(0)
        file.write(file_contents)
        file.truncate()

print(f'Project \'{day}\' created successfully from template \'src/template\'')
