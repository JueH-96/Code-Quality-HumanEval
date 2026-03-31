def odd_count(lst):
    out = []
    for s in lst:
        count = sum(1 for ch in s if int(ch) % 2 == 1)
        tmpl = f"the number of odd elements in the string {count} of the input."
        out.append(tmpl.replace("i", str(count)))
    return out