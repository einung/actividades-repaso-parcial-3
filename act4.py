class Empleado:
    BONIFICACION_GENERAL = 300

    def __init__(self, nombre, antiguedad, salario_base):
        self._nombre = nombre
        self._antiguedad = antiguedad
        self._salario_base = salario_base

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def antiguedad(self):
        return self._antiguedad

    @antiguedad.setter
    def antiguedad(self, valor):
        self._antiguedad = valor

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, valor):
        self._salario_base = valor

    @classmethod
    def calcular_bonificacion_general(cls):
        return cls.BONIFICACION_GENERAL

    def calcular_bonificacion_antiguedad(self):
        return self._antiguedad * 100

    def calcular_bonificacion_total(self):
        return self.calcular_bonificacion_general() + self.calcular_bonificacion_antiguedad()

empleado = Empleado("Juan Pérez", 5, 1500)

print(f"Nombre del empleado: {empleado.nombre}")
print(f"Antigüedad: {empleado.antiguedad} años")
print(f"Salario base: ${empleado.salario_base}")

bonificacion_general = Empleado.calcular_bonificacion_general()
print(f"Bonificación general: ${bonificacion_general}")

bonificacion_antiguedad = empleado.calcular_bonificacion_antiguedad()
print(f"Bonificación por antigüedad: ${bonificacion_antiguedad}")

bonificacion_total = empleado.calcular_bonificacion_total()
print(f"Bonificación total: ${bonificacion_total}")