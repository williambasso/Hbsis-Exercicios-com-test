class CaracteresCpfExcedidosException(Exception):
    def __init__(self, msg: str = 'Caracteres excedidos'):
        super().__init__(msg)