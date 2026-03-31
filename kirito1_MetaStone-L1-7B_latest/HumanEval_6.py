def calculate_max_depth(s):
    depth = 0
    max_d = 0
    for c in s:
        if c == '(':
            depth += 1
            if depth > max_d:
                max_d = depth
        else:
            depth -= 1
    return max_d

def your_function(s):
    groups = s.split()
    result = []
    for group in groups:
        current_depth = 0
        max_depth_group = 0
        for c in group:
            if c == '(':
                current_depth += 1
                if current_depth > max_depth_group:
                    max_depth_group = current_depth
            else:
                current_depth -= 1
        result.append(max_depth_group)
    return result