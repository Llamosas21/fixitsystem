# Modelo para consolas PS3
class PS3ConsolaModel:
    def __init__(self, numero_serie, estado, cliente_id):
        self.modelo = 'PS3'
        self.numero_serie = numero_serie
        self.estado = estado
        self.cliente_id = cliente_id

    def to_dict(self):
        return {
            'modelo': self.modelo,
            'numero_serie': self.numero_serie,
            'estado': self.estado,
            'cliente_id': self.cliente_id
        }
