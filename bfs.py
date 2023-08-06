graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}



def bfs(graph, node):
    visited = []
    queue = []

    queue.append(node)
    # curr = node
    while queue:
        curr = queue.pop()
        visited.append(curr)
        for adj in graph[curr]:
            if adj not in visited:
                queue.append(adj)
    return visited
    



print(bfs(graph,'5'))
