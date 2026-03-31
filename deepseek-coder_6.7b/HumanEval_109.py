def move_one_ball(arr):
    if len(arr) == 0: return True
    count = 0
    for i in range(len(arr)):
        if arr[i] > arr[(i+1)%len(arr)]: count += 1
    return count <= 1