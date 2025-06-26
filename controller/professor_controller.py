
from service.professor_service import ProfessorService


class ProfessorController:
    def __init__(self, professor_service: ProfessorService):
        self.professor_service = professor_service

    def cadastrar_professor(self):
        nome = input("Nome: ")
        dt_nasc = input("Data de Nascimento (YYYY-MM-DD): ")
        cpf = input("CPF: ")
        especialidade = input("Especialidade: ")
        dados_professor = {
            "nome": nome,
            "dt_nasc": dt_nasc,
            "cpf": cpf,
            "especialidade": especialidade
        }
        return self.professor_service.criar_professor(dados_professor)
    
    def listar_professores(self):
        professores = self.professor_service.listar_professores()
        if professores:
            print("\nProfessores cadastrados:")
            for professor in professores:
                print(f"Nome: {professor.nome}, CPF: {professor.cpf}, Especialidade: {professor.especialidade}")
        else:
            print("Nenhum professor cadastrado.")
    def buscar_professor(self):
        cpf = input("Digite o CPF do professor: ")
        professor = self.professor_service.obter_professor_por_cpf(cpf)
        if professor:
            print(f"Professor encontrado: {professor.nome}, Especialidade: {professor.especialidade}")
        else:
            print("Professor não encontrado.")
            
    def excluir_professor(self):
        cpf = input("Digite o CPF do professor a ser excluído: ")
        self.professor_service.deletar_professor(cpf)

    
    def menu(self):
        while True:
            print("\n--- Menu Professor ---")
            print("1. Cadastrar Professor")
            print("2. Listar Professores")
            print("3. Buscar Professor por CPF")
            print("4. Excluir Professor")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_professor()
            elif opcao == "2":
                professores = self.listar_professores()
                for prof in professores:
                    print(f"Nome: {prof.nome}, CPF: {prof.cpf}, Especialidade: {prof.especialidade}")
            elif opcao == "3":
                self.buscar_professor()
            elif opcao == "4":
                self.excluir_professor()
            elif opcao == "5":
                print("Saindo do menu.")
                break
            else:
                print("Opção inválida. Tente novamente.")


    