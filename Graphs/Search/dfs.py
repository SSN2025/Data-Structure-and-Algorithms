import numpy as np
def dfs(graph,visit,i=0):
    visit[i]=1
    print(i)
    for j in range(graph[i].size):
        if(visit[j]==0 and graph[i][j] == 1):
            dfs(graph,visit,j)



graph = np.array([
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
])

visit = np.zeros(len(graph))

dfs(graph,visit)