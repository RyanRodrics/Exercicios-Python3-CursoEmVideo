# Ex011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

w = float(input('Qual a largura da parede (m)? '))
h = float(input('Qual a altura da parede (m)? '))
A = w * h
t = A / 2
print('Com {}m x {}m, a área da parede é {:.2f}m², então será necessário {:.2f} litros de tinta'.format(w, h, A, t))
