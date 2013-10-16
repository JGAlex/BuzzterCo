__author__="t4r0"
__date__ ="$14-oct-2013 16:53:32$"

class pruebas():
    
    def pruebaIndice(self):
        print("Hola clase!")
        "Este es un ejemplo de indices fuera de rango"
        arreglo = ["ejemplo1", "ejemplo2", "ejemplo3"]
        i = 0
        for i in range(6):
            print(arreglo[i])
        return
    
    def errorCapturado(self):
        arreglo = ["ejemplo1", "ejemplo2", "ejemplo3"]
        i = 0
        try:
            for i in range(6):
                print(arreglo[i])
        except Exception:
            print("Error, el indice esta fuera del rango")