from aluno import Aluno

alunos = []

while True:
    nome = input("Digite o nome do aluno: ").strip()
    if nome == "":
        break
    matricula = input("Digite a matrícula: ").strip()
    aluno = Aluno(nome, matricula)
    alunos.append(aluno)

if len(alunos) >= 1:
    alunos[0].notas.append(8.5)
    alunos[0].notas.append(7.0)
    alunos[0].faltas = 2
if len(alunos) >= 2:
    alunos[1].notas.append(5.5)
    alunos[1].faltas = 6
if len(alunos) >= 3:
    alunos[2].faltas = 0

for aluno in alunos:
    print("\n", aluno.nome, f"({aluno.matricula})")
    print("Notas:", aluno.notas)
    print("Faltas:", aluno.faltas)
    if len(aluno.notas) > 0:
        media = sum(aluno.notas) / len(aluno.notas)
        print(f"Média: {media:.2f}")
    else:
        print("Média: sem notas")

mais_faltas = None

for aluno in alunos:
    if mais_faltas is None or aluno.faltas > mais_faltas.faltas:
        mais_faltas = aluno

if mais_faltas is not None:
    print("\nMais faltas:", mais_faltas.nome, f"({mais_faltas.faltas})")
else:
    print("\nNenhum aluno cadastrado.")