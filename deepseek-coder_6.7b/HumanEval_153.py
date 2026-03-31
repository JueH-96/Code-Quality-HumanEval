def Strongest_Extension(class_name, extensions):
    strongest = None
    max_strength = 0
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strength = cap - sm
        if (strength > max_strength) or ((strength == max_strength) and (strongest is None)):
            strongest = ext
            max_strength = strength
    return f"{class_name}.{strongest}"