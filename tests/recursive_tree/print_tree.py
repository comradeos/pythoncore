import os
import json
import matplotlib.pyplot as plt
import networkx as nx

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






# Создание графа
G = nx.DiGraph()

# Добавление узлов и ребер
G.add_edge('Start', 'Step 1')
G.add_edge('Step 1', 'Step 2')
G.add_edge('Step 2', 'End')

# Рисование графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold')

# Сохранение графа в PNG
plt.savefig("block_diagram.png")