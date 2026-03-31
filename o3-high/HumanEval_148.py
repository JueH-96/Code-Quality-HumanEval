def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closest to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    # Ordered list of planets from closest to farthest from the Sun
    planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
    
    # Normalize input to lowercase for comparison
    p1 = planet1.strip().lower()
    p2 = planet2.strip().lower()
    
    # Validate planet names
    if p1 not in planets or p2 not in planets:
        return ()
    
    idx1 = planets.index(p1)
    idx2 = planets.index(p2)
    
    # Determine the slice of planets that lie between the two indices (exclusive)
    if idx1 < idx2:
        between = planets[idx1 + 1:idx2]
    elif idx2 < idx1:
        between = planets[idx2 + 1:idx1]
    else:  # Same planet provided twice
        between = []
    
    # Convert back to capitalized names as in the examples
    return tuple(name.capitalize() for name in between)