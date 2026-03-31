def Strongest_Extension(class_name, extensions):
    """Return the strongest extension for a given class.
    
    Strength of an extension is defined as:
        strength = (number of uppercase letters) - (number of lowercase letters)
    
    If multiple extensions share the highest strength, the first occurring
    one in the list is chosen.
    """
    best_strength = float('-inf')
    best_ext = None

    for ext in extensions:
        cap = sum(1 for ch in ext if ch.isupper())
        sm = sum(1 for ch in ext if ch.islower())
        strength = cap - sm

        if strength > best_strength:
            best_strength = strength
            best_ext = ext

    # If no extension provided, just return the class name
    if best_ext is None:
        return class_name
    return f"{class_name}.{best_ext}"