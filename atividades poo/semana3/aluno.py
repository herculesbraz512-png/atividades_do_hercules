class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
        self.faltas = 0

    def adicionar_nota(self, nota):
        if nota < 0 or nota > 10:
            return False
        self.notas.append(nota)
        return True
    
    def registrar_falta(self):
        self.faltas += 1

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0.0
        return sum(self.notas) / len(self.notas)
    
    def verificar_aprovacao(self, total_aulas):
        media = self.calcular_media()
        limite_faltas = 0.25 * total_aulas
        return media >= 7.0 and self.faltas <= limite_faltas
    
    def get_matricula(self):
        return self.matricula
    
    def set_matricula(self, matricula):
        if matricula.strip() == "":
            return False
        self.matricula = matricula
        return True

    def __str__(self):
        return f"{self.nome} ({self.matricula}) | Média {self.calcular_media():.2f} | Faltas {self.faltas}"
