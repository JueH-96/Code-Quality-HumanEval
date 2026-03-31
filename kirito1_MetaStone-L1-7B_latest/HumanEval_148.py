def bf(planet1, planet2):
    order = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", 
             "Saturn", "Uranus", "Neptune")
    # Create a dictionary to map each planet name to its index for quick lookup
    planet_to_index = {p: idx for idx, p in enumerate(order)}
    
    # Check if both planets are valid
    if planet1 not in planet_to_index or planet2 not in planet_to_index:
        return ()
    
    i = planet_to_index[planet1]
    j = planet_to_index[planet2]
    
    low = min(i, j)
    high = max(i, j)
    
    # Collect planets whose index is strictly between low and high
    result = [p for idx, p in enumerate(order) if low < idx < high]
    
    return tuple(result)