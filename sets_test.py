
def merge_the_tools(string, k):
    # your code goes here
    for part in zip(*[iter(string)] * k):
        d = dict()
        d1=[d.setdefault(c, c) for c in part if c not in d]
        print(''.join(d1))


s1=merge_the_tools("AABCAAADA", 3)
