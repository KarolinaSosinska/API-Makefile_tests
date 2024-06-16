import math

class FunkcjaKwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print(f"Przy podanych współczynnikach funkcja kwadratowa ma postać = {self.a}*x^2+{self.b}*x+{self.c}")

    def rozwiaz(self):
        if self.a == 0 and self.b == 0:
            if self.c == 0:
                return "Liczba nieskończona"
            else:
                return "Zero rozwiązań"
        if self.a == 0 and self.b != 0:
            return f"Delta = 0 Funkcja liniowa, jedno miejsce zerowe x = {- self.c / self.b}"
        else:
            delta = self.b ** 2 - 4 * self.a * self.c
            if delta > 0:
                x1 = (-self.b - math.sqrt(delta)) / (2 * self.a)
                x2 = (-self.b + math.sqrt(delta)) / (2 * self.a)
                return f"Delta > 0 , dwa miejsca zerowe. x1 = {x1} , x2= {x2}"
            else:
                return "Delta < 0, brak miejsc zerowych"


def main():
    a = int(input("Podaj wartość współczynnika a : "))
    b = int(input("Podaj wartość współczynnika b : "))
    c = int(input("Podaj wartość współczynnika c : "))
    funkcja = FunkcjaKwadratowa(a, b, c)
    print(funkcja.rozwiaz())


if __name__ == "__main__":
    main()
