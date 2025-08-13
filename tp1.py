gclass Suma:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def mostrar(self):
        print(f"La suma es: {self.a + self.b}")


if __name__ == "__main__":
    Suma(5, 7).mostrar()