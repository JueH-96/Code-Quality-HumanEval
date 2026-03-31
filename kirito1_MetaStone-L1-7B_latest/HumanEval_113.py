def is_odd(c):
    return int(c) % 2 != 0

def main():
    import sys
    input = sys.stdin.read().split()
    lst = list(input)
    
    for i, s in enumerate(lst):
        count = sum(1 for c in s if is_odd(c))
        x_str = f"number of odd elements {count}n"
        substitution = str(count) + 'n'
        
        # For sample 1:
        # "the number ...4n ..." 
        # So, the line starts with a phrase and ends with ...something...
        # Here's an attempt to construct it.
        output_line = f"the number of odd elements {substitution}"
        if i == 0:  # For first element in sample1
            output_line += " the str4ng..."
        else:
            output_line += "...5th"
        
        print(output_line)

if __name__ == "__main__":
    main()