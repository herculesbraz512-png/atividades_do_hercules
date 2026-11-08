from aluno import Aluno

aluno1 = Aluno("Maria Silva", "2024001")
aluno2 = Aluno("João Souza", "2024002")
aluno3 = Aluno("Ana Lima", "2024003")

alunos = [aluno1, aluno2, aluno3]

aluno1.adicionar_nota(8.5)
aluno1.adicionar_nota(7.0)

aluno2.adicionar_nota(5.5)

for i in range(2):
    aluno1.registrar_falta()

for i in range(6):
    aluno2.registrar_falta()

if not aluno1.adicionar_nota(11):
    print("Nota inválida: use um valor entre 0 e 10.")

if not aluno2.adicionar_nota(-2):
    print("Nota inválida: use um valor entre 0 e 10.")

if not aluno3.set_matricula("   "):
    print("Matrícula inválida: não pode ser vazia.")

for aluno in alunos:
    print(aluno)
    if aluno.verificar_aprovacao(40):
        print("   Situação: aprovado")
    else:
        print("   Situação: reprovado")

maior_media = None

for aluno in alunos:
    if maior_media is None or aluno.calcular_media() > maior_media.calcular_media():
        maior_media = aluno
if maior_media is not None:
    print(f"Maior média: {maior_media.nome} ({maior_media.calcular_media():.2f})")
