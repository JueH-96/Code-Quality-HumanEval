def get_planets_between(planet1, planet2):
    order = ['Mercury', 'Venus', 'Earth', 'Mars', 
             'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    
    if planet1 not in order or planet2 not in order:
        return ()
    
    idx1 = order.index(planet1)
    idx2 = order.index(planet2)
    
    min_idx = min(idx1, idx2)
    max_idx = max(idx1, idx2)
    
    between_planets = order[min_idx + 1 : max_idx]
    return tuple(between_planets)

# Example usage:
# print(get_planets_between("Jupiter", "Neptune"))  # Output: ('Saturn', 'Uranus')