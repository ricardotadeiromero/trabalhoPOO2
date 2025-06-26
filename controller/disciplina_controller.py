

from service.disciplina_service import DisciplinaService


class DisciplinaController:
    def __init__(self, disciplina_service):
        self.disciplina_service = disciplina_service

    def cadastrar_disciplina(self):
        nome = input("Digite o nome da disciplina: ")
        carga_horaria = input("Digite a carga horária da disciplina: ")
        dados_disciplina = {
            "nome": nome,
            "carga_horaria": int(carga_horaria),
        }
        return self.disciplina_service.criar_disciplina(dados_disciplina)
    
    def listar_disciplinas(self):
        disciplinas = self.disciplina_service.listar_disciplinas()
        if disciplinas:
            print("\nDisciplinas cadastradas:")
            for disciplina in disciplinas:
                print(f"Nome: {disciplina.nome}, Carga Horária: {disciplina.carga_horaria}")
        else:
            print("Nenhuma disciplina cadastrada.")

    def buscar_disciplina(self):
        nome = input("Digite o nome da disciplina: ")
        disciplina = self.disciplina_service.obter_disciplina_por_nome(nome)
        if disciplina:
            print(f"Disciplina encontrada: {disciplina.nome}, Carga Horária: {disciplina.carga_horaria}")
        else:
            print("Disciplina não encontrada.")

    def excluir_disciplina(self):
        nome = input("Digite o nome da disciplina a ser excluída: ")
        self.disciplina_service.deletar_disciplina(nome)
        

    def menu(self):
        while True:
            print("\nMenu de Disciplinas:")
            print("1. Cadastrar Disciplina")
            print("2. Listar Disciplinas")
            print("3. Buscar Disciplina")
            print("4. Excluir Disciplina")
            print("5. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_disciplina()
            elif opcao == "2":
                self.listar_disciplinas()
            elif opcao == "3":
                self.buscar_disciplina()
            elif opcao == "4":
                self.excluir_disciplina()
            elif opcao == "5":
                break
            else:
                print("Opção inválida. Tente novamente.")
