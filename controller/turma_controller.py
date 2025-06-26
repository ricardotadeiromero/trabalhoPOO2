from model.atividade_avaliativa import AtividadeAvaliativa
from service.aluno_service import AlunoService
from service.disciplina_service import DisciplinaService
from service.professor_service import ProfessorService
from service.turma_service import TurmaService


class TurmaController:
    def __init__(self, turma_service, aluno_service, professor_service, disciplina_service):
        self.turma_service = turma_service
        self.aluno_service = aluno_service
        self.professor_service = professor_service
        self.disciplina_service = disciplina_service
        
    def criar_turma(self):
        nome = input("Nome da turma: ")

        dados = {
            "nome": nome
        }
        self.turma_service.criar_turma(dados)
        print("Turma criada com sucesso!")

    def listar_turmas(self):
        turmas = self.turma_service.listar_turmas()
        if not turmas:
            print("Nenhuma turma encontrada.")
            return
        for turma in turmas:
            print(f"- Nome: {turma.nome}")

    def adicionar_aluno(self):
        matricula = input("Matrícula do aluno: ")
        aluno = self.aluno_service.obter_aluno_por_matricula(matricula)
        if not aluno:
            print("Aluno não encontrado.")
            return
        nome_turma = input("Nome da turma: ")
        turma = self.turma_service.adicionar_aluno(nome_turma, aluno)
        if turma:
            print("Aluno adicionado com sucesso à turma.")
        else:
            print("Turma não encontrada.")

    def listar_alunos(self):
        nome_turma = input("Nome da turma: ")
        alunos = self.turma_service.listar_alunos(nome_turma)
        if not alunos:
            print("Nenhum aluno encontrado ou turma inexistente.")
            return
        print("Alunos da turma:")
        for aluno in alunos:
            print(f"- {aluno['nome']} (Matrícula: {aluno['matricula']})")

    def deletar_turma(self):
        nome_turma = input("Nome da turma a deletar: ")
        self.turma_service.deletar_turma(nome_turma)
             
    
    def adicionar_disciplina(self):
        nome_turma = input("Nome da turma: ")
        nome_disciplina = input("Nome da disciplina: ")
        disciplina = self.disciplina_service.obter_disciplina_por_nome(nome_disciplina)
        if not disciplina:
            print("Disciplina não encontrada.")
            return
        professor_cpf = input("CPF do professor (opcional, deixe em branco se não houver): ")
        if professor_cpf:
            professor = self.professor_service.obter_professor_por_cpf(professor_cpf)
            if not professor:
                print("Professor não encontrado.")
                return
            turma = self.turma_service.adicionar_disciplina(nome_turma, disciplina, professor)
        else:
            turma = self.turma_service.adicionar_disciplina(nome_turma, disciplina)
    
    def adicionar_professor(self):
        nome_turma = input("Nome da turma: ")
        cpf_professor = input("CPF do professor: ")
        professor = self.professor_service.obter_professor_por_cpf(cpf_professor)
        if not professor:
            print("Professor não encontrado.")
            return
        turma = self.turma_service.adicionar_professor(nome_turma, professor)
        if turma:
            print("Professor adicionado com sucesso à turma.")
        else:
            print("Turma não encontrada.")
    
    def adicionar_atividade(self):
        nome_turma = input("Nome da turma: ")
        nome_atividade = input("Nome da atividade: ")
        descricao = input("Descrição da atividade: ")
        nome_disciplina = input("Disciplina relacionada: ")
        disciplina = self.disciplina_service.obter_disciplina_por_nome(nome_disciplina)
        if not disciplina:
            print("Disciplina não encontrada.")
            return
        if not self.turma_service.obter_turma_por_nome(nome_turma):
            print("Turma não encontrada.")
            return
        disciplinas = self.turma_service.listar_disciplinas_professores(nome_turma)
        for dp,_ in disciplinas:
            if dp == nome_disciplina:
                break
            else:
                print("Disciplina não encontrada na turma.")
                return
        atividade = AtividadeAvaliativa(nome_atividade, descricao, nome_disciplina)
        self.turma_service.adicionar_atividade(nome_turma, atividade)
        print("Atividade adicionada com sucesso à turma.")
    
    def adicionar_professor_a_disciplina(self):
        nome_turma = input("Nome da turma: ")
        nome_disciplina = input("Nome da disciplina: ")
        cpf_professor = input("CPF do professor: ")
        self.professor_service.adicionar_disciplina(cpf_professor, nome_disciplina)
        turma = self.turma_service.adicionar_professor_a_disciplina(nome_turma, nome_disciplina, cpf_professor)
        if turma:
            print("Professor adicionado à disciplina com sucesso.")
        else:
            print("Turma ou disciplina não encontrada.")

    def adicionar_nota(self):
        nome_turma = input("Nome da turma: ")
        matricula_aluno = input("Matrícula do aluno: ")
        nome_atividade = input("Nome da atividade: ")
        nota = float(input("Nota do aluno: "))
        self.turma_service.adicionar_nota(nome_turma, matricula_aluno, nome_atividade, nota)
    
    def remover_nota(self):
        nome_turma = input("Nome da turma: ")
        matricula_aluno = input("Matrícula do aluno: ")
        nome_atividade = input("Nome da atividade: ")
        self.turma_service.remover_nota(nome_turma, matricula_aluno, nome_atividade)
        print("Nota removida com sucesso.")

    def remover_aluno(self):
        nome_turma = input("Nome da turma: ")
        matricula = input("Matrícula do aluno a remover: ")
        turma = self.turma_service.remover_aluno(nome_turma, matricula)
        if turma:
            print("Aluno removido com sucesso da turma.")
        else:
            print("Turma não encontrada ou aluno não encontrado na turma.")
    
    def listar_disciplinas(self):
        nome_turma = input("Nome da turma: ")
        disciplinas = self.turma_service.listar_disciplinas_professores(nome_turma)
        if not disciplinas:
            print("Nenhuma disciplina encontrada ou turma inexistente.")
            return
        print("Disciplinas da turma:")
        for disciplina, professor in disciplinas:
            print(f"- {disciplina} (Professor CPF: {professor})")

    def listar_professores(self):
        nome_turma = input("Nome da turma: ")
        professores = self.turma_service.listar_professores(nome_turma)
        if not professores:
            print("Nenhum professor encontrado ou turma inexistente.")
            return
        print("Professores da turma:")
        for professor in professores:
            print(f"- {professor['nome']} (CPF: {professor['cpf']})")
        
    def listar_atividades(self):
        nome_turma = input("Nome da turma: ")
        atividades = self.turma_service.listar_atividades(nome_turma)
        if not atividades:
            print("Nenhuma atividade encontrada ou turma inexistente.")
            return
        print("Atividades da turma:")
        for atividade in atividades:
            print(f"- Nome: {atividade['nome']}, Descrição: {atividade['descricao']}, Disciplina: {atividade['disciplina_nome']}")
    def listar_notas(self):
        nome_turma = input("Nome da turma: ")
        matricula_aluno = input("Matrícula do aluno: ")
        nome_atividade = input("Nome da atividade: ")
        nota = self.turma_service.obter_nota_do_aluno(nome_turma, matricula_aluno, nome_atividade)
        if nota:
            print(f"Nota do aluno {matricula_aluno} na atividade {nome_atividade}: {nota.valor}")
        else:
            print("Nota não encontrada ou aluno não inscrito na atividade.")
    def remover_disciplina(self):
        nome_turma = input("Nome da turma: ")
        nome_disciplina = input("Nome da disciplina a remover: ")
        turma = self.turma_service.remover_disciplina(nome_turma, nome_disciplina)
        if turma:
            print("Disciplina removida com sucesso da turma.")
        else:
            print("Turma ou disciplina não encontrada.")
    def remover_professor(self):
        nome_turma = input("Nome da turma: ")
        cpf_professor = input("CPF do professor a remover: ")
        turma = self.turma_service.remover_professor(nome_turma, cpf_professor)
        if turma:
            print("Professor removido com sucesso da turma.")
        else:
            print("Turma não encontrada ou professor não encontrado na turma.")
    def remover_atividade(self):
        nome_turma = input("Nome da turma: ")
        nome_atividade = input("Nome da atividade a remover: ")
        turma = self.turma_service.remover_atividade(nome_turma, nome_atividade)
        if turma:
            print("Atividade removida com sucesso da turma.")
        else:
            print("Turma ou atividade não encontrada.")
    

    def menu(self):
        opcoes = {
            "1": ("Criar turma", self.criar_turma),
            "2": ("Listar turmas", self.listar_turmas),
            "3": ("Adicionar aluno à turma", self.adicionar_aluno),
            "4": ("Listar alunos da turma", self.listar_alunos),
            "5": ("Deletar turma", self.deletar_turma),
            "6": ("Adicionar disciplina à turma", self.adicionar_disciplina),
            "7": ("Adicionar professor à turma", self.adicionar_professor),
            "8": ("Adicionar atividade à turma", self.adicionar_atividade),
            "9": ("Adicionar professor a disciplina", self.adicionar_professor_a_disciplina),
            "10": ("Adicionar nota", self.adicionar_nota),
            "11": ("Remover nota", self.remover_nota),
            "12": ("Remover aluno da turma", self.remover_aluno),
            "13": ("Listar disciplinas da turma", self.listar_disciplinas),
            "14": ("Listar professores da turma", self.listar_professores),
            "15": ("Listar atividades da turma", self.listar_atividades),
            "16": ("Listar nota do aluno em atividade", self.listar_notas),
            "17": ("Remover disciplina da turma", self.remover_disciplina),
            "18": ("Remover professor da turma", self.remover_professor),
            "19": ("Remover atividade da turma", self.remover_atividade),
            "0": ("Sair", None)
        }
        while True:
            print("\n--- Menu Turma ---")
            for k, v in sorted(opcoes.items(), key=lambda x: int(x[0]) if x[0].isdigit() else x[0]):
                print(f"{k} - {v[0]}")
            escolha = input("Escolha uma opção: ")
            if escolha == "0":
                print("Saindo do menu de turmas.")
                break
            acao = opcoes.get(escolha)
            if acao and acao[1]:
                try:
                    acao[1]()
                except Exception as e:
                    print(f"Erro ao executar a ação: {e}")
            else:
                print("Opção inválida.")
