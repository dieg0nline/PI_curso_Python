# https://youtu.be/oe04X1B14YY

class Persona():
    def __init__(self, nombre, edad, Lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.Lugar_residencia = Lugar_residencia

    def descripcion(self):
        print("nombre:", self.nombre, " edad:", self.edad, " Residencia:", self.Lugar_residencia)

class Empleado(Persona):
    def __init__(self, nombre, edad, Lugar_residencia, salario, antiguedad):
        super().__init__(nombre, edad, Lugar_residencia)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("salario: ", self.salario, "antigüedad: ", self.antiguedad)

diego = Empleado("diego", 53, "sanvi", 1200, 4)
diego.descripcion()
