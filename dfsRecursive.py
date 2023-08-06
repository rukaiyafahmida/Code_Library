graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}



def dfs(visited, graph, node, output):
    if node not in visited:
        visited.add(node)
        output.append(node)
        for adj in graph[node]:
            dfs(visited, graph, adj, output)
    return output

def dfs_recursive(graph, node):
    visited = set()
    output = []
    return dfs(visited=visited, graph=graph, node=node, output=output)
    

print(dfs_recursive(graph,'5'))
