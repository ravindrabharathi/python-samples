regex_pattern = r"^(?=[MDCLXVI])M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"
# M{0,3} is to satisfy !>=4000
#ref https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/ch06s09.html
#solution for https://www.hackerrank.com/challenges/validate-a-roman-number/problem
import re
print(str(bool(re.match(regex_pattern, input()))))