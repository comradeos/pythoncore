import os
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def print_tree(node, level=0, x=0):
    node['X'] = x
    node['Y'] = level
    print('-' * level + node['Pin'] + f" ({node['X']}, {node['Y']})")
    for i, child in enumerate(node['Child']):
        print_tree(child, level + 1, i)

with open('tree.json') as f:
    data = json.load(f)

print('\n'*3)

print_tree(data)

print('\n'*3)