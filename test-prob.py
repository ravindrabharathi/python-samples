from fractions import Fraction

ux_red_count = 4
ux_black_count = 3
ux_count = ux_red_count + ux_black_count

uy_red_count = 5
uy_black_count = 4
uy_count = uy_red_count + uy_black_count

uz_red_count = 4
uz_black_count = 4
uz_count = uz_red_count + uz_black_count

px_red = Fraction(ux_red_count, ux_count)
px_black = Fraction(ux_black_count, ux_count)

print(px_red,px_black)

py_red = Fraction(uy_red_count, uy_count)
py_black = Fraction(uy_black_count, uy_count)
print(py_red,py_black)

pz_red = Fraction(uz_red_count, uz_count)
pz_black = Fraction(uz_black_count, uz_count)
print(pz_red,pz_black)

result = px_red * py_red * pz_black + \
         px_red * py_black * pz_red + \
         px_black * py_red * pz_red
print(result)
