def exibir_menu():
    print ("\n====== ESTOQUE De ALUNOS ======")
    print ("1 - adicionar aluno")
    print ("2 - atualizar nota")
    print ("3 - remover aluno")
    print ("4 - exibir alunos e notas")
    print ("5 - exibir media")
    print ("0 - sair")
    print ("====== ESTOQUE De ALUNOS ======")

def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem).replace(",", "."))
            if 0 <= nota <= 10:
                return nota
            else:
                print ("a nota deve estar entre 0 e 10")
        except ValueError:
            print ("digite um numero valido: ")

def ler_quatro_notas():
    notas = []
    for i in range(4):
        nota = ler_nota(f"Digite a nota {i}: ")
        notas.append(nota)
    return notas

def adicionar_aluno(alunos, nome, notas):
    nome = nome.strip().title()
    if nome in alunos:
        print("ja tem o aluno, use atualizar")
    else:
        alunos[nome] = notas
        print("aluno adicionado")

def atualizar_nota(alunos, nome, notas):
    nome = nome.strip().title()
    if nome in alunos:
        alunos[nome] = notas
        print("notas atualizadas")
    else:
        print("aluno não encontrado")

def remover_aluno(alunos, nome):
    nome = nome.strip().title()
    if nome in alunos:
        del alunos[nome]
        print("aluno removido")
    else:
        print("aluno não encontrado")

def calcular_media(notas):
    if notas:
        return sum(notas) / len(notas)
    else:
        return 0

def exibir_alunos(alunos):
    if not alunos:
        print("nenhum aluno cadastrado")
    else:
        print("\n====== ALUNOS E NOTAS ======")
        for nome, notas in alunos.items():
            print(f"\nAluno: {nome}")
            print(f"nota1: {notas[0]}")
            print(f"nota2: {notas[1]}")
            print(f"nota3: {notas[2]}")
            print(f"nota4: {notas[3]}")

def exibir_media(alunos):
    if not alunos:
        print("nenhum aluno cadastrado")
    else:
        print("\n====== MEDIA DOS ALUNOS ======")
        for nome, notas in alunos.items():
            media = calcular_media(notas)
            print(f"{nome}: {media:.2f}")

def main():

    alunos = {}
    while True:
        exibir_menu()
        opcao = input("escolha uma opção: ")
        if opcao == "1":
            nome = input("nome do aluno: ").strip().title()
            if nome == "":
                print("o nome não pode ficar vazio")
                continue
            notas = ler_quatro_notas()
            adicionar_aluno(alunos, nome, notas)
        elif opcao == "2":
            nome = input("nome do aluno: ")
            notas = ler_quatro_notas()
            atualizar_nota(alunos, nome, notas)
        elif opcao == "3":
            nome = input("nome do aluno: ")
            remover_aluno(alunos, nome)
        elif opcao == "4":
            exibir_alunos(alunos)
        elif opcao == "5":
            exibir_media(alunos)
        elif opcao == "0":
            print("programa encerrado")
            break
        else:
            print("opção invalida")

main()