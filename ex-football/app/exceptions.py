class MaximumCapacityOfMaracanaExceededException(Exception):
    def __init__(self, msg: str = 'Capacidade de players no stadium excedida'):
        super().__init__(msg)