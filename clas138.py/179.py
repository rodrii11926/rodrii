desde enumeración importar Enum, automático


clase Palo(Enum):
    aprobar
clase PaloEs(Palo):
    ORO = auto()
    COPA = auto()
    ESPADA = auto()
    BASTO = auto()
clase PaloFr(Palo):
    TREBOL = auto()
    DIAMANTE = auto()
    ESPADA = auto()
    CORAZONES = auto()
clase Numero(Enum):
    aprobar
clase NumeroEs(Numero):
    AS=1
    DOS=2
    TRES=3
    CUATRO=4
    CINCO=5
    SEIS=6
    SIETE=7
    OCHO=8
    NUEVE=9
    SOTA=10
    CABALLO=11
    REY=12
clase NumeroFr(Numero):
    A=1
    DOS=2
    TRES=3
    CUATRO=4
    CINCO=5
    SEIS=6
    SIETE=7
    OCHO=8
    NUEVE=9
    DIEZ=10
    J=11
    Q=12
    K=13
Carta de clase:
    def __init__(self,tipo,numero):
        self.tipo=tipo
        self.numero=numero
nueveDeEspada=Carta(PaloEs.ESPADA,NumeroEs(9))
print(nueveDeEspada.tipo.nombre, nueveDeEspada.numero.nombre)

importar json
data = {"nombre": "Gabriel", "edad": 24, "ciudad": "Buenos Aires"}

json_str = json.dumps(datos)
con open("datos.json","w",encoding="utf-8") como archivo:
    archivo.write(json_str)
print("cadena de json",json_str)
# Convertir una cadena JSON a un diccionario
datos2 = json.loads(json_str)
print("diccionario de python",data2['nombre'])
