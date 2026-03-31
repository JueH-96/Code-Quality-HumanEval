def Strongest_Extension(class_name, extensions):
    strengths = [(ext, sum(1 for c in ext if c.isupper()) - sum(1 for c in ext if c.islower())) for ext in extensions]
    strongest_extension = max(strengths, key=lambda x: x[1])[0]
    return f'{class_name}.{strongest_extension}'