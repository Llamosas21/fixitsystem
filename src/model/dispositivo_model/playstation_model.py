# Modelo para dispositivos PlayStation (PS3, PS4, PS5)
class PlayStationModel:
    def __init__(self, modelo, numero_serie, estado, cliente_id):
        self.modelo = modelo  # PS3, PS4, PS5
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
