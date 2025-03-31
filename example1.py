# Leer x cantidad de edad y calcular la media

class Edad:
    def __init__(self, edades):
        self.edades = edades

    def calcular_media(self):
        return sum(self.edades) / len(self.edades)
    
    def mostrar_media(self):
        media = self.calcular_media()
        print(f"La media de las edades es: {media:.2f}")

def main():
    edades = []

    while True:
        try:
            edad = int(input("Ingrese una edad (-1 para terminar): "))
            if edad == -1:
                break
            edades.append(edad)
        except ValueError:
            print("Ingrese un numero valido")

    if (not edades):
        print("No se ingresaron edades")
        return
    else:
        edad_obj = Edad(edades)
        print(edad_obj.mostrar_media())

if __name__ == "__main__":
    main()