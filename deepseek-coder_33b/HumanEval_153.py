def Strongest_Extension(class_name, extensions):
    strength = lambda ext: sum([-1 if c.isupper() else 1 for c in ext])
    strongest_ext = max(extensions, key=strength)
    return class_name + '.' + strongest_ext