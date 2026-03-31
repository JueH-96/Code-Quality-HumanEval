def Strongest_Extension(class_name, extensions):
    def strength(extension):
        return sum(1 if c.isupper() else -1 for c in extension)

    strongest = max((strength(ext), ext) for ext in extensions)[1]
    return f'{class_name}.{strongest}'