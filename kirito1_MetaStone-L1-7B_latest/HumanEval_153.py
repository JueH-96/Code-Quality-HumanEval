def Strongest_Extension(class_name, extensions):
    strongest_ext = None
    max_strength = -float('inf')
    
    for ext in extensions:
        cap = 0
        sm = 0
        for c in ext:
            if c.isupper():
                cap += 1
            elif c.islower():
                sm += 1
        
        strength = cap - sm
        
        if strongest_ext is None or strength > max_strength:
            strongest_ext = ext
            max_strength = strength
    
    return f"{class_name}.{strongest_ext}"