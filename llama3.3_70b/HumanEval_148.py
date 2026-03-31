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
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # Check if both planet1 and planet2 are in the list of planets
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    # Get the indices of planet1 and planet2 in the list of planets
    idx1 = planets.index(planet1)
    idx2 = planets.index(planet2)
    
    # Swap indices if idx1 is greater than idx2 to ensure we get all planets between them
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
    
    # Return a tuple of planets between planet1 and planet2 (exclusive) in the correct order
    return tuple(planets[idx1+1:idx2])