            self.cartas.append(carta)
            return True
        return False
    def borrarCarta(self,nombreDeCarta):
        for contador,carta in self.cartas:
            if carta.nombre == nombreDeCarta:
                cartaEliminada = self.cartas.pop(contador)
                return cartaEliminada
        return None

    def elixirPromedio(self):
        if self.cartas:
            cantidad = len(self.cartas)
            sumaDeElixir = sum(carta.elixir for carta in self.cartas)
            promedio = sumaDeElixir / cantidad
            return promedio
        return 0
    def porcentajeDeVictorias(self):
        partidasJugadas = self.victorias + self.derrotas
        if partidasJugadas > 0:
            porcentaje = self.victorias / partidasJugadas * 100
            return porcentaje
        return 0

class Jugador:
    maximoDeMazos = 10
    def __init__(self, nombre,tag):
        self.nombre=nombre
        self.tag=tag
        self.mazos=[]
    def agregarMazo(self,mazo):
        if len(self.mazos)<self.maximoDeMazos:
            self.mazos.append(mazo)
            return True
        return False
    def borrarMazo(self,numeroDeMazo):
        if numeroDeMazo >= 0 and numeroDeMazo < len(self.mazos):
            mazo = self.mazos.pop(numeroDeMazo)
            return mazo
        return None