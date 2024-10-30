import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, node_colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node_colors[node] for node in tree.nodes()]
    labels = {node: data['label'] for node, data in tree.nodes(data=True)}
    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, with_labels=True)
    plt.show()

def color_gradient(n):
    return ['#%02x%02x%02x' % (int(255 * (i / n)), 0, int(255 * (1 - i / n))) for i in range(n)]

def bfs(tree_root):
    queue = deque([tree_root])
    visited = set()
    order = []
    while queue:
        node = queue.popleft()
        if node and node.id not in visited:
            visited.add(node.id)
            order.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return order

def dfs(tree_root):
    stack = [tree_root]
    visited = set()
    order = []
    while stack:
        node = stack.pop()
        if node and node.id not in visited:
            visited.add(node.id)
            order.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return order

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обхід в ширину
bfs_order = bfs(root)
bfs_colors = {node.id: color for node, color in zip(bfs_order, color_gradient(len(bfs_order)))}
draw_tree(root, bfs_colors)

# Обхід в глибину
dfs_order = dfs(root)
dfs_colors = {node.id: color for node, color in zip(dfs_order, color_gradient(len(dfs_order)))}
draw_tree(root, dfs_colors)
