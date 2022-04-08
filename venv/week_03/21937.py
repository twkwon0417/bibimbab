a, b = map(int, input().split())

graph = {}
aa = set()

for _ in range(b):
    x, y = map(int, input().split())
    if y not in graph.keys():
        graph[y] = {x}
    else:
        graph[y].add(x)

X = int(input())


def dfs(tree, num):
    try:
        for val in tree[num]:
            if val:
                aa.add(val)
                dfs(tree, val)
    except KeyError:
        pass


dfs(graph, X)
print(len(aa))
