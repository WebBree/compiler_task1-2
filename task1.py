# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AHG1LmWdEy9I7StM6ca3dM7roqJ5WRpE
"""

def is_comment(line):
    # Check if a line is a comment
    return line.strip().startswith('//') or line.strip().startswith('#') or line.strip().startswith('/*')

# Read the code from a file
with open('your_code_file.txt', 'r') as file:
    code_lines = file.readlines()

# Initialize lists to store comments and non-comments
comments = []
non_comments = []

# Iterate through each line and classify as comment or non-comment
for line in code_lines:
    if is_comment(line):
        comments.append(line)
    else:
        non_comments.append(line)

# Print the results
print("Comments:")
for comment in comments:
    print(comment.strip())

print("\nNon-Comments:")
for non_comment in non_comments:
    print(non_comment.strip())