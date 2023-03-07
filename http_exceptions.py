from fastapi import HTTPException,status


class UsuarioNoExisteException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail='El usuario no existe')
class UsuarioMaximoCuentasException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail='El usuario ya tiene 5 cuentas')  
class UsuarioEmailDuplicadoException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail='El correo electrónico ya está registrado')

class UsuarioSinCuentasException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail='El usuario no tiene cuentas')
