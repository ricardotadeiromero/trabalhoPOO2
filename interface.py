
from controller.aluno_controller import AlunoController
from controller.professor_controller import ProfessorController
from controller.turma_controller import TurmaController
from controller.disciplina_controller import DisciplinaController
from service.turma_service import TurmaService
from service.aluno_service import AlunoService
from service.professor_service import ProfessorService
from service.disciplina_service import DisciplinaService
from repository.repository import Repository
from model.aluno import Aluno
from model.professor import Professor
from model.turma import Turma
from model.disciplina import Disciplina

aluno_repository = Repository("alunos.json", Aluno)
professor_repository = Repository("professores.json", Professor)
turma_repository = Repository("turmas.json", Turma)
disciplina_repository = Repository("disciplinas.json", Disciplina)

aluno_service = AlunoService(aluno_repository)
professor_service = ProfessorService(professor_repository)
disciplina_service = DisciplinaService(disciplina_repository)
turma_service = TurmaService(turma_repository)

aluno_controller = AlunoController(aluno_service)
professor_controller = ProfessorController(professor_service)
turma_controller = TurmaController(turma_service, aluno_service, professor_service, disciplina_service)
disciplina_controller = DisciplinaController(disciplina_service)

def exibir_menu():
    print("\nMenu:")
    print("1. Gerenciar Alunos")
    print("2. Gerenciar Professores")
    print("3. Gerenciar Turmas")
    print("4. Gerenciar Disciplinas")
    print("5. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            aluno_controller.menu()
        elif opcao == "2":
            professor_controller.menu()
        elif opcao == "3":
            turma_controller.menu()
        elif opcao == "4":
            disciplina_controller.menu()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()