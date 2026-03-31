def fibfib(n, cache={0:0, 1:0, 2:1}):
    if n not in cache:
        cache[n] = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
    return cache[n]