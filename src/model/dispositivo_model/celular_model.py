class CelularModel:
    def __init__(self, marca, modelo, numero_serie, estado, cliente_id):
        self.marca = marca
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.estado = estado
        self.cliente_id = cliente_id

    def to_dict(self):
        return {
            'marca': self.marca,
            'modelo': self.modelo,
            'numero_serie': self.numero_serie,
            'estado': self.estado,
            'cliente_id': self.cliente_id
        }
