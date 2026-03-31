def Strongest_Extension(class_name, extensions):
    """
    You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The 
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    """
    # Initialize variables to store the strongest extension and its strength
    strongest_extension = None
    max_strength = float('-inf')
    
    # Iterate through each extension
    for extension in extensions:
        # Calculate the number of uppercase and lowercase letters in the extension's name
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        
        # Calculate the strength of the current extension
        strength = cap_count - sm_count
        
        # Check if the current extension is stronger than the strongest found so far
        if strength > max_strength:
            # Update the strongest extension and its strength
            strongest_extension = extension
            max_strength = strength
    
    # Return the class name followed by the strongest extension's name
    return f'{class_name}.{strongest_extension}'