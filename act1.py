class CuentaBancaria:
    def __new__(cls, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], int):
            instance = super().__new__(cls)
            instance.numero_cuenta = args[0]
            instance.saldo = 0
            instance.tipo_cuenta = "No especificado"
            return instance
        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], (int, float)):
            instance = super().__new__(cls)
            instance.numero_cuenta = args[0]
            instance.saldo = args[1]
            instance.tipo_cuenta = "No especificado"
            return instance
        elif len(args) == 3 and isinstance(args[0], int) and isinstance(args[1], (int, float)) and isinstance(args[2], str):
            instance = super().__new__(cls)
            instance.numero_cuenta = args[0]
            instance.saldo = args[1]
            instance.tipo_cuenta = args[2]
            return instance
        else:
            raise ValueError("Argumentos inválidos para crear una cuenta bancaria.")

    @classmethod
    def con_numero_cuenta(cls, numero_cuenta):
        return cls(numero_cuenta)

    @classmethod
    def con_numero_y_saldo(cls, numero_cuenta, saldo):
        return cls(numero_cuenta, saldo)

    @classmethod
    def con_numero_saldo_y_tipo(cls, numero_cuenta, saldo, tipo_cuenta):
        return cls(numero_cuenta, saldo, tipo_cuenta)

    def __str__(self):
        return (f"CuentaBancaria(Numero: {self.numero_cuenta}, Saldo: {self.saldo}, Tipo: {self.tipo_cuenta})")

cuenta1 = CuentaBancaria.con_numero_cuenta(12345)
cuenta2 = CuentaBancaria.con_numero_y_saldo(67890, 5000.0)
cuenta3 = CuentaBancaria.con_numero_saldo_y_tipo(11223, 10000.0, "Ahorros")

print(cuenta1)
print(cuenta2)
print(cuenta3)

