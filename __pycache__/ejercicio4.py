from api.library import *

def main():
    #aplicacion de diccionarios
    persona = {
        "datospersonales":{
        "nombre":"Dubian",
        "apellidos":"Uriana",
        "edad": 25
        },

        "salarial": {
            "salario": 200000,
            "subtransporte":50000,
            "subalimentacion":60000

        }

    },


   # print (persona["nombre"]" " + persona["apellidos"])
   # persona["nombre"] = "Blass"
   #print (f"{persona['nombre'])
   print (f"nombre:{persona['datospersonales']['nombre']} {persona'datospersonales})


if __name__== "__main__":
    main()