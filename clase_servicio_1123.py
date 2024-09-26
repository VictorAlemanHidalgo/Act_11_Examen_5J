# Victor Aleman Hidalgo, 5-J
# Zona de la clase
class Servicio1123:
    ID_servicio = 0
    Nombre = ""
    Descripcion = ""
    Precio = 0.00
    Tipo = ""
    Horario = ""
    Ubicacion = ""

    # Zona de funciones
    def datos1123(self):
        print(f"Id del servicio: {self.ID_servicio}")
        print(f"Nombre del servicio: {self.Nombre}")
        print(f"Descripcion del servicio: {self.Descripcion}")
        print(f"Precio del servicio: {self.Precio}")
        print(f"Tipo del servicio: {self.Tipo}")
        print(f"Horario del servicio: {self.Horario}")
        print(f"Ubicacion del servicio: {self.Ubicacion}")

    def Listar_Horario1123(self):
        Horario1123 = ["8:00 am - 6:00 pm", "4:00 am - 6:00 pm", "2:00 am - 6:00 pm", "8:00 am - 8:00 pm", "8:00 am - 7:00 pm", "8:00 am - 12:00 pm", "6:00 am - 6:00 pm"]
        print(Horario1123)
        for servicio1123 in Horario1123:
            print(servicio1123)

    def Tupla_ID_Servicios1123(self):
        id_Servicios1123 = (1251, 2343, 2363, 2353, 4545, 3423, 2423)
        print(id_Servicios1123)
        for materia in id_Servicios1123:
            print(materia)
        
    def Diccionario_servicio_precio1123(self):
        Servicios1123 = {
            "Consultoria": 145.25,
            "Diseño de estrategia de marketing": 250.00,
            "Diseño de contenido": 200.00,
            "Mentoria Grupal": 150.00,
            "Mentoria Personal": 200.00,
            "Taller presencial": 120.00,
            "Taller virtual": 100.00
        }
        print(Servicios1123)
        for nombreServicio1123, precio1123 in Servicios1123.items():
            print(f"Servicio: {nombreServicio1123}, precio: {precio1123} pesos")

    def altas1123(self):
        print("La operacion se realizo correctamente.")

    def bajas1123(self):
        print("La operacion no se realizo correctamente.")

# Zona de objetos
obj1123 = Servicio1123()

# Zona de uso de objetos
obj1123.ID_servicio = 1
obj1123.Nombre = "Consultoria"
obj1123.Descripcion = "Sesion de 90 minutos para abordar un tema en particular en el que necesitan apoyo para resolver alguna situacion."
obj1123.Precio = 145.25
obj1123.Tipo = "Aprendizaje"
obj1123.Horario = "8:00 am - 6:00 pm"
obj1123.Ubicacion = "Virtual"

print("Datos")
obj1123.datos1123()
print("Lista de horarios")
obj1123.Listar_Horario1123()
print("Tupla de ID's")
obj1123.Tupla_ID_Servicios1123()
print("Diccionario de servicios con precio")
obj1123.Diccionario_servicio_precio1123()
obj1123.altas1123()
obj1123.bajas1123()