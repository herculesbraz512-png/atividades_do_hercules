class Televisao:
    def __init__(self, marca, polegadas):
        self.marca = marca
        self.polegadas = polegadas
        self.ligada = False
        self.canal = 1
        self.volume = 10

    def ligar(self):
        if self.ligada:
            return False
        self.ligada = True
        return True
    def desligar(self):
        if not self.ligada:
            return False
        self.ligada = False
        return True

    def aumentar_volume(self, quantidade):
        if not self.ligada or quantidade <= 0 or self.volume == 100:
            return False
        novo_volume = min(100, self.volume + quantidade)
        if novo_volume == self.volume:
            return False
        self.volume = novo_volume
        return True

    def diminuir_volume(self, quantidade):
        if not self.ligada or quantidade <= 0 or self.volume == 0:
            return False
        novo_volume = max(0, self.volume - quantidade)
        if novo_volume == self.volume:
            return False
        self.volume = novo_volume
        return True

    def trocar_canal(self, canal):
        if not self.ligada or canal < 1 or canal > 100:
            return False
        if canal == self.canal:
            return False
        self.canal = canal
        return True

    def __str__(self):
        if self.ligada:
            return f'{self.marca} {self.polegadas}" | Ligada | Canal {self.canal} | Volume {self.volume}'
        return f'{self.marca} {self.polegadas}" | Desligada'
