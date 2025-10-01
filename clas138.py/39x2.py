importar csv
importar json
Clase Persona:
    def __init__(self,nombre,edad,esEstudiante):
            self.name=nombre
                    self.age=edad
                            self.isStudent=esEstudiante
                                def __str__(auto):
                                        return "nombre: "+self.name + ",edad: " + self.age + ",es estudiante: " + self.isStudent
                                        personas = []

                                        con open('data.csv','r') como archivo:
                                            lector = csv.reader(archivo)
                                                para la fila en el lector:
                                                        persona = Persona(fila[0],fila[1],fila[2])
                                                                personas.append(persona)
                                                                personas.pop(0)
                                                                para persona en personas:
                                                                    imprimir(persona.__str__())
                                                                    "'
                                                                    {
                                                                      "nombre": "John Doe",
                                                                        "edad": 30,
                                                                          "isStudent": falso
                                                                          }

                                                                          nombre, edad, es estudiante
                                                                          Juan Pérez, 30 años, falso
                                                                          "'importar csv
                                                                          importar json
                                                                          Clase Persona:
                                                                              def __init__(self,nombre,edad,esEstudiante):
                                                                                      self.name=nombre
                                                                                              self.age=edad
                                                                                                      self.isStudent=esEstudiante
                                                                                                          def __str__(auto):
                                                                                                                  return "nombre: "+self.name + ",edad: " + self.age + ",es estudiante: " + self.isStudent
                                                                                                                  personas = []

                                                                                                                  con open('data.csv','r') como archivo:
                                                                                                                      lector = csv.reader(archivo)
                                                                                                                          para la fila en el lector:
                                                                                                                                  persona = Persona(fila[0],fila[1],fila[2])
                                                                                                                                          personas.append(persona)
                                                                                                                                          personas.pop(0)
                                                                                                                                          para persona en personas:
                                                                                                                                              imprimir(persona.__str__())
                                                                                                                                              "'
                                                                                                                                              {
                                                                                                                                                "nombre": "John Doe",
                                                                                                                                                  "edad": 30,
                                                                                                                                                    "isStudent": falso
                                                                                                                                                    }

                                                                                                                                                    nombre, edad, es estudiante
                                                                                                                                                    Juan Pérez, 30 años, falso
                                                                                                                                                    "'