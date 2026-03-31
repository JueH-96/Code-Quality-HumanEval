def sort_even(l: list):
    evens = l[::2]
    sorted_evens = sorted(evens)
    new_list = []
    even_ptr = 0
    for i in range(len(l)):
        if i % 2 == 0:
            new_list.append(sorted_evens[even_ptr])
            even_ptr += 1
        else:
            new_list.append(l[i])
    return new_list