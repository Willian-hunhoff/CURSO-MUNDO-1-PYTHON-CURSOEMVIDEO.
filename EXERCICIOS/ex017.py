from math import hypot
catop = float(input("escreva qual cateto oposto do seu triangulo "))
catad = float(input("escreva qual o cateto adjacente do seu triangulo "))
hip = hypot(catop, catad)
print ("se o cateto oposto é {:.2f} e o cateto adjascente é {:.2f} entao a hipotenusa é = a {:.2f}" .format(catop, catad, hip))
