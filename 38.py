class Clase:
        def __init__(self, atributo):
                #init va con dos guiones bajos al inicio y al final
                        self.atributo = atributo

      def metodo(self):
 return "El atributo es: " + self.atributo
                             
 def imprimir(self):
  print("Imprimiendo: " + self.atributo )

  instancia = Clase("valor")
print(instancia.metodo() )
  instancia.imprimir()
 #ejercicio: crear una clase que sume dos numeros y los muestre por pantalla