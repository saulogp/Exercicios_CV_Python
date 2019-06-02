l = float(input("Largura da parede: "))
a = float(input("Altura da parede: "))
area = l * a
t = area / 2
print("Sua parede tem a dimensão de {}x{} e a sua área é de {}m².".format(l, a, area))
print("Para pintar essa parede, você precisará de {}l de tinta.".format(t))
