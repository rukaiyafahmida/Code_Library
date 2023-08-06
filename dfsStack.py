graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}



def dfs(graph, node):
    visited = []
    stack = []
    stack.append(node)
    while stack:
        curr = stack.pop()
        visited.append(curr)
        for adj in graph[curr]:
            if adj not in visited and adj not in stack:
                stack.append(adj)
    return visited
    



print(dfs(graph,'5'))
