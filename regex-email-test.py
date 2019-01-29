#sol for

###
# ^ => Marks the beginning < => match char '<' A-Za-z+ => match following
# pattern : 'A-Za-z' or 'A-Za-zzz' or 'A-Za-zzzzzzzzzzzzzzzzzzz'
# (should be enclosed inside [] for the given problem) @ => Match character '@' [A-Za-z]+ => same as above .
#  => matches ANY CHARACTER (here it should have been . which matches only dot/period)
#  [A-Za-z]{1,3} => combination of alphabets whose length should be atleast
# 1 and max 3 '>' => match char '>' $ => marks the ending
#####



import re
n = int(input())
pattern = r"^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$"
for i in range(n):
    name,email = input().split(" ")
    if re.match(pattern,email):
        print(name,email)
