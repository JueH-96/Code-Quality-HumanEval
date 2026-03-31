def Strongest_Extension(class_name, extensions):
    best_strength = None
    best_extension = None
    
    for ext in extensions:
        cap = sum(1 for ch in ext if ch.isupper())
        sm = sum(1 for ch in ext if ch.islower())
        strength = cap - sm
        
        if best_strength is None or strength > best_strength:
            best_strength = strength
            best_extension = ext
            
    return f"{class_name}.{best_extension}"