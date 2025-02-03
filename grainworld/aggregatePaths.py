import numpy as np
import pandas as pd
from collections import deque

df1 = pd.read_csv('testAdjacency.csv', index_col=0)
df2 = pd.DataFrame(0, index=df1.index, columns=df1.columns)


def shortest_path_bfs(df, start, target):
    if start == target:
        return 0

    queue = deque([(start, 0)])
    visited = set()

    while queue:
        node, distance = queue.popleft()

        for neighbor, connected in df.loc[node].items():
            if connected == 1 and neighbor not in visited:
                if neighbor == target:
                    return distance + 1
                queue.append((neighbor, distance + 1))
                visited.add(neighbor)

    return 0


for row_label in df1.index:
    for col_label in df1.columns:
        df2.loc[row_label, col_label] = shortest_path_bfs(df1, row_label, col_label)

df2.to_csv('testCentrality.csv')
