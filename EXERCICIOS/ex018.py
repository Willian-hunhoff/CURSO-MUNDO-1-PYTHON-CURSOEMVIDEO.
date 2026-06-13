from math import cos, tan, sin, radians
ang = float(input("digite o angulo desejado para o calculo: "))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print("O angulo de {} graus tem o SENO de {:.2f} " .format(ang, seno))
print("o angulo de {} graus tem o COSSENO de {:.2f} " .format(ang, cosseno))
print("o angulo de {} graus tem a TANGENTE de {:.2f} " .format(ang, tangente))
