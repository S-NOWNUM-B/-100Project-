from math import *

class Triangles:
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def Plo_Rav_Bed(self):
        S = 1/2 * (self.c * self.h)
        return f"Площадь равнобедренного треугольника равна - {S}"

    def Plo_Rav_Sto(self):
        S = sqrt(3)/4 * (self.a ** 2)
        return f"Площадь равносторонего треугольника равна - {S}"

    def Plo_Raz_Tr(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            s = (self.a + self.b + self.c) / 2
            S = sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
            return f"Площадь разностороннего треугольника равна - {S}"
        else:
            return "Ошибка: треугольник с такими сторонами не существует"

tr1 = Triangles(2, 5, 3, 7)
tr2 = Triangles(2, 4, 1, 7)
tr3 = Triangles(1, 1, 1, 2)

print(tr1.Plo_Rav_Bed())
print(tr2.Plo_Rav_Sto())
print(tr3.Plo_Raz_Tr())