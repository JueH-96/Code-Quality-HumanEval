def pluck(arr):
    if not arr: return []
    even_nodes = [(i, v) for i, v in enumerate(arr) if v % 2 == 0]
    if not even_nodes: return []
    smallest_even = min(even_nodes, key=lambda x: (x[1], x[0]))
    return list(smallest_even)