from abc import ABC, abstractmethod

class Auth(ABC):
    @abstractmethod
    def iniciarSesion(self, usuario, password):
        pass

class Autenticacion(Auth):
    def iniciarSesion(self, usuario, password):
        print(f"Iniciando sesión con el usuario: {usuario} desde el autenticador base")

class DecoradorAuth(Auth):
    def __init__(self, auth: Auth):
        self._auth = auth

    def iniciarSesion(self, usuario, password):
        self._auth.iniciarSesion(usuario, password)

class SoporteGmail(DecoradorAuth):
    def iniciarSesion(self, usuario, password):
        print("[Gmail] Validando credenciales en Gmail...")
        super().iniciarSesion(usuario, password)
        print("[Gmail] Sesión iniciada exitosamente en Gmail.")

class SoporteFacebook(DecoradorAuth):
    def iniciarSesion(self, usuario, password):
        print("[Facebook] Validando credenciales en Facebook...")
        super().iniciarSesion(usuario, password)
        print("[Facebook] Sesión iniciada exitosamente en Facebook.")

autenticador = Autenticacion()

authgmail = SoporteGmail(autenticador)
authgmail.iniciarSesion("usuario1@gmail.com", "pass789")

authfacebook = SoporteFacebook(autenticador)
authfacebook.iniciarSesion("nombredeusuario123", "pass456")