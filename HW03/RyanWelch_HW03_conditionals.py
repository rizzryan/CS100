# Ryan Welch
# CS100 2017F Section 105
# HW 03 Conditionals, September 21, 2017

a = 3
b = 4
c = 5

if a < b:
    print('Okay. {} is less than {}.'.format(a, b))
else:
    print('Not okay. {} is not less than {}.'.format(a, b))

if c < b:
    print('Okay. {} is less than {}.'.format(c, b))
else:
    print('Not okay. {} is not less than {}.'.format(c, b))
    
if a + b == c:
    print('Okay. {} + {} = {}.'.format(a, b, c))
else:
    print('Not okay. {} + {} != {}.'.format(a, b, c))

if (a**a + b**b) == (c**c):
    print('Okay. ({})^2  + ({})^2 = ({})^2.'.format(a, b, c))
else:
    print('Not okay. ({})^2  + ({})^2 != ({})^2.'.format(a, b, c))