
from service.aluno_service import AlunoService


class AlunoController:
    def __init__(self, aluno_service: AlunoService):
        self.aluno_service = aluno_service

    def cadastrar_aluno(self):
        nome = input("Digite o nome do aluno: ")
        dt_nasc = input("Digite a data de nascimento (YYYY-MM-DD): ")
        cpf = input("Digite o CPF do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        dados_aluno = {
            "nome": nome,
            "dt_nasc": dt_nasc,
            "cpf": cpf,
            "matricula": matricula
        }
        return self.aluno_service.criar_aluno(dados_aluno)

    def listar_alunos(self):
        alunos = self.aluno_service.listar_alunos()
        if alunos:
            print("\nAlunos cadastrados:")
            for aluno in alunos:
                print(f"Nome: {aluno.nome}, Matrícula: {aluno.matricula}, CPF: {aluno.cpf}, Data de Nascimento: {aluno.dt_nasc}")
        else:
            print("Nenhum aluno cadastrado.")

    def buscar_aluno(self):
        matricula = input("Digite a matrícula do aluno: ")
        aluno = self.aluno_service.obter_aluno_por_matricula(matricula)
        if aluno:
            print(f"Aluno encontrado: {aluno.nome}, Matrícula: {aluno.matricula}")
        else:
            print("Aluno não encontrado.")

    def excluir_aluno(self):
        matricula = input("Digite a matrícula do aluno a ser excluído: ")
        self.aluno_service.deletar_aluno(matricula)
        

    def menu(self):
        while True:
            print("\nMenu de Alunos:")
            print("1. Cadastrar Aluno")
            print("2. Listar Alunos")
            print("3. Buscar Aluno")
            print("4. Excluir Aluno")
            print("5. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_aluno()
            elif opcao == "2":
                self.listar_alunos()
            elif opcao == "3":
                self.buscar_aluno()
            elif opcao == "4":
                self.excluir_aluno()
            elif opcao == "5":
                break
            else:
                print("Opção inválida. Tente novamente.")
