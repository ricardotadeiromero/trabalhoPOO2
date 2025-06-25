# -*- coding: utf-8 -*-
from model.aluno import Aluno
from model.atividade_avaliativa import AtividadeAvaliativa
from model.disciplina import Disciplina
from model.nota import Nota
from model.professor import Professor
from model.turma import Turma
from repository.repository import Repository


def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar aluno")
    print("2. Adicionar disciplina")
    print("3. Adicionar professor")
    print("4. Adicionar professor a disciplina")
    print("5. Adicionar atividade avaliativa")
    print("6. Listar alunos")
    print("7. Listar disciplinas")
    print("8. Listar professores")
    print("9. Listar atividades avaliativas")
    print("10. Salvar e sair")


if __name__ == "__main__":
    repo = Repository("turma.json", Turma)

    turma = repo.carregar()
    if turma is None:
        turma = Turma(nome="Turma 2025")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            cpf = input("CPF do aluno: ")
            data_nascimento = input("Data de nascimento (YYYY-MM-DD): ")
            matricula = int(input("Número de matrícula: "))
            aluno = Aluno(nome, cpf, data_nascimento, matricula)
            turma.adicionar_aluno(aluno)
            print(f"Aluno {nome} adicionado com sucesso!")

        elif opcao == "2":
            nome_disciplina = input("Nome da disciplina: ")
            carga_horaria = int(input("Carga horária: "))
            disciplina = Disciplina(nome_disciplina, carga_horaria)
            turma.adicionar_disciplina(disciplina)
            print(f"Disciplina {nome_disciplina} adicionada com sucesso!")

        elif opcao == "3":
            nome_professor = input("Nome do professor: ")
            cpf_professor = input("CPF do professor: ")
            data_nascimento_professor = input("Data de nascimento (YYYY-MM-DD): ")
            especialidade = input("Especialidade: ")
            professor = Professor(nome_professor, cpf_professor, data_nascimento_professor, especialidade)
            turma.adicionar_professor(professor)
            print(f"Professor {nome_professor} adicionado com sucesso!")

        elif opcao == "4":  # Adicionar professor a disciplina
            if not turma.disciplinas_professores:
                print("Nenhuma disciplina cadastrada. Cadastre uma disciplina primeiro.")
                continue

            print("Disciplinas disponíveis:")
            for i, dp in enumerate(turma.disciplinas_professores):
                print(f"{i + 1}. {dp.disciplina_nome}")  # Corrigido para acessar o atributo diretamente

            disciplina_index = int(input("Escolha o número da disciplina: ")) - 1
            if disciplina_index < 0 or disciplina_index >= len(turma.disciplinas_professores):
                print("Opção inválida.")
                continue

            if not turma.professores:
                print("Nenhum professor cadastrado. Cadastre um professor primeiro.")
                continue

            print("Professores disponíveis:")
            for i, professor in enumerate(turma.professores):
                print(f"{i + 1}. {professor.nome} (CPF: {professor.cpf})")

            professor_index = int(input("Escolha o número do professor: ")) - 1
            if professor_index < 0 or professor_index >= len(turma.professores):
                print("Opção inválida.")
                continue

            disciplina = turma.disciplinas_professores[disciplina_index].disciplina_nome
            cpf_professor = turma.professores[professor_index].cpf
            turma.adicionar_professor_a_disciplina(disciplina, cpf_professor)
            print(f"Professor {professor.nome} adicionado à disciplina {disciplina} com sucesso!")

        elif opcao == "5":
            nome_atividade = input("Nome da atividade: ")
            descricao = input("Descrição da atividade: ")
            nome_disciplina = input("Disciplina relacionada: ")
            atividade = AtividadeAvaliativa(nome_atividade, descricao, nome_disciplina)
            matricula_aluno = int(input("Matrícula do aluno: "))
            nota = float(input("Nota do aluno: "))
            atividade.adicionar_nota(Nota(matricula_aluno, nota))
            turma.adicionar_atividade(atividade)
            print(f"Atividade {nome_atividade} adicionada com sucesso!")

        elif opcao == "6":
            print("Alunos cadastrados:")
            for aluno in turma.alunos:
                aluno.exibir()

        elif opcao == "7":  # Listar disciplinas
            print("Disciplinas cadastradas:")
            if not turma.disciplinas_professores:
                print("Nenhuma disciplina cadastrada.")
            else:
                for dp in turma.disciplinas_professores:
                    professor = next((p for p in turma.professores if p.cpf == dp.professor_cpf), None)
                    professor_nome = professor.nome if professor else "Professor não encontrado"
                    print(f"Disciplina: {dp.disciplina_nome}, Professor: {professor_nome}")

        elif opcao == "8":  # Listar professores
            print("Professores cadastrados:")
            if not turma.professores:
                print("Nenhum professor cadastrado.")
            else:
                for professor in turma.professores:
                    disciplinas = [dp.disciplina_nome for dp in turma.disciplinas_professores if dp.professor_cpf == professor.cpf]
                    print(f"Nome: {professor.nome}, CPF: {professor.cpf}, Especialidade: {professor.especialidade}")
                    if disciplinas:
                        print("Disciplinas ministradas:")
                        for disciplina in disciplinas:
                            print(f"- {disciplina}")
                    else:
                        print("Nenhuma disciplina ministrada.")

        elif opcao == "9":
            print("Atividades avaliativas cadastradas:")
            for atividade in turma.atividades:
                print(f"Nome: {atividade.nome}, Descrição: {atividade.descricao}, Disciplina: {atividade.disciplina_nome}")

        elif opcao == "10":
            repo.salvar(turma)
            print("Turma salva com sucesso! Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")
