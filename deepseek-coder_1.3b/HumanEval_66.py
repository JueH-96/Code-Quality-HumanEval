def digitSum(s):
        return sum([ord(c) - 87 if c.isupper() else ord(c) for c in s])      # ASCII value of "A" is 65 and a uppercase letter's equivalent (ascii code minus 'a') = 90-64=25