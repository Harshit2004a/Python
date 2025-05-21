# Program to Calculate the Edge Cover of a Graph

def edge_cover(graph):
    covered = set()
    cover = set()
    for u in graph:
        if u not in covered:
            for v in graph[u]:
                if v not in covered:
                    cover.add((u, v))
                    covered.add(u)
                    covered.add(v)
                    break
    return cover

if __name__ == "__main__":
    graph = {
        0: {1, 2},
        1: {0, 2},
        2: {0, 1, 3},
        3: {2}
    }
    result = edge_cover(graph)
    print("Edge Cover:")
    for edge in result:
        print(edge)

# Code by Harshit