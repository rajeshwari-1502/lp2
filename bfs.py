graph={
    '0' : ['1','2'],
    '1' : ['3','4'],
    '2' : ['5'],
    '3' : [],
    '4' : ['8'],
    '5' : [],
    '8' : []
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m, end = " ")
        
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                

print('BFS - ')
bfs(visited, graph, '0')