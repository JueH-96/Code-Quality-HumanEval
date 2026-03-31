def Strongest_Extension(class_name, extensions):
    max_strength = -float('inf')
    best_extension = None
    for ext in extensions:
        cap = sum(1 for char in ext if char.isupper())
        sm = sum(1 for char in ext if char.islower())
        strength = cap - sm
        if strength > max_strength:
            max_strength = strength
            best_extension = ext
    return f"{class_name}.{best_extension}"