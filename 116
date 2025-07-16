from datetime import date

objeto = {
    "nombre": "Gabriel",
    "edad": 23,
    "ciudad": "buenos aires",
}
objeto["cumple"]=date(2001,6,11)
hoy = date.today()
objeto["edad"] = (
    hoy.year - objeto["cumple"].year
)
def cumpleHoy(fechaDeHoy,
              fechaDeNacimiento):
    mismoMes = (
        fechaDeHoy.month 
        == fechaDeNacimiento.month
    )
    mismoDia = (fechaDeHoy.day 
                == fechaDeNacimiento.day
    )
    return mismoMes and mismoDia

objeto2 = dict(nombre = "andres", 
               edad = 21, 
               ciudad = "buenos aires",
               cumple = date(2004,2,25))
listaDeDiccionarios = [
    objeto,
    objeto2,
    {
        "nombre":"pablo",
        "edad":55,
        "ciudad":"buenos aires",
        "cumple":date(1969,11,24),
        "hijos":(objeto,objeto2)
    }
]
print("quien es el primer elemento?",
      listaDeDiccionarios[0]["nombre"])