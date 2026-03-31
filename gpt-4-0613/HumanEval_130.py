def tri(n):
    if n < 0:
        return []
    elif n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2]
    else:
        tri_list = [1, 3, 2]
        for i in range(3, n + 1):
            if i % 2 == 0:
                tri_list.append(1 + i / 2)
            else:
                tri_list.append(tri_list[i - 1] + tri_list[i - 2] + tri_list[i - 3])
        return tri_list