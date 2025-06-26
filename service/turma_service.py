
from model.nota import Nota
from model.turma import Turma


class TurmaService:
    def __init__(self, turma_repository):
        self.turma_repository = turma_repository

    def criar_turma(self, dados):
        turma = Turma.from_dict(dados)
        if self.obter_turma_por_nome(turma.nome):
            print(f"Turma com nome {turma.nome} já existe.")
            return None
        return self.turma_repository.salvar(turma)

    def obter_turma_por_nome(self, nome_turma):
        return self.turma_repository.buscar_por_atributo("nome", nome_turma)

    def deletar_turma(self, nome_turma):
        return self.turma_repository.deletar("nome",nome_turma)

    def adicionar_aluno(self, nome_turma, aluno):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            turma.adicionar_aluno(aluno)
            self.turma_repository.atualizar("nome", turma)
            return turma
        return None
    
    def remover_aluno(self, nome_turma, matricula):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            turma.remover_aluno_por_matricula(matricula)
            self.turma_repository.atualizar("nome", turma)
            return turma
        return None

    def remover_professor(self, nome_turma, cpf_professor):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            for professor in turma.professores:
                if professor.cpf == cpf_professor:
                    turma.professores.remove(professor)
                    break
            self.turma_repository.atualizar("nome", turma)
            return turma
        return None

    def remover_disciplina(self, nome_turma, nome_disciplina):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            for dp in turma.disciplinas_professores:
                if dp.disciplina_nome == nome_disciplina:
                    turma.disciplinas_professores.remove(dp)
                    break
            self.turma_repository.atualizar("nome", turma)
            return turma
        return None

    def remover_atividade(self, nome_turma, nome_atividade):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            for atividade in turma.atividades:
                if atividade.nome == nome_atividade:
                    turma.atividades.remove(atividade)
                    break
            self.turma_repository.atualizar("nome", turma)
            return turma
        return None
    
    def adicionar_nota(self, nome_turma, matricula_aluno, nome_atividade, nota):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            atividade = self.obter_atividade(nome_turma, nome_atividade)
            if atividade:
                nota_class = Nota(matricula_aluno, nota)
                for atividade in turma.atividades:
                    if atividade.nome == nome_atividade:
                        atividade.adicionar_nota(nota_class)
                        self.turma_repository.atualizar("nome", turma)
                        break
                return turma
        return None
    def remover_nota(self, nome_turma, matricula_aluno, nome_atividade):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            atividade = self.obter_atividade(nome_turma, nome_atividade)
            if atividade:
                for atividade in turma.atividades:
                    if atividade.nome == nome_atividade:
                        atividade.remover_nota_do_aluno(matricula_aluno)
                        self.turma_repository.atualizar("nome", turma)
                        return turma
                return turma
        return None
    
    def obter_nota_do_aluno(self, nome_turma, matricula_aluno, nome_atividade):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            atividade = self.obter_atividade(nome_turma, nome_atividade)
            if atividade:
                return atividade.get_nota_do_aluno(matricula_aluno)
        return None
    def obter_atividade(self, nome_turma, nome_atividade):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            for atividade in turma.atividades:
                if atividade.nome == nome_atividade:
                    return atividade
        return None
    def adicionar_disciplina(self, nome_turma, disciplina, professor=None):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            turma.adicionar_disciplina(disciplina, professor)
            self.turma_repository.atualizar("nome", turma)
            return turma
        return None

    def adicionar_professor_a_disciplina(self, nome_turma, nome_disciplina, cpf_professor):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            turma.adicionar_professor_a_disciplina(nome_disciplina, cpf_professor)
            self.turma_repository.atualizar("nome", turma)
            return turma
        return None
    
    def adicionar_professor(self, nome_turma, professor):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            turma.adicionar_professor(professor)
            self.turma_repository.atualizar("nome", turma)
            return turma
        return None

    def adicionar_atividade(self, nome_turma, atividade):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            turma.adicionar_atividade(atividade)
            self.turma_repository.atualizar("nome", turma)
            return turma
        return None

    def obter_atividades(self, nome_turma):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            return turma.atividades
        return None

    def obter_alunos(self, nome_turma):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            return turma.alunos
        return None

    def obter_disciplinas(self, nome_turma):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            return turma.disciplinas
        return None

    def obter_professores(self, nome_turma):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            return turma.professores
        return None

    def salvar_turma(self, nome_turma):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            self.turma_repository.salvar(turma)
            return turma
        return None

    def listar_disciplinas_professores(self, nome_turma):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            return [(dp.disciplina_nome, dp.professor_cpf) for dp in turma.disciplinas_professores]
        return None

    def listar_professores(self, nome_turma):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            return [(professor.nome, professor.cpf, professor.especialidade) for professor in turma.professores]
        return None

    def listar_alunos(self, nome_turma):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            return [aluno.to_dict() for aluno in turma.alunos]
        return None

    def listar_atividades(self, nome_turma):
        turma = self.turma_repository.buscar_por_atributo("nome", nome_turma)
        if turma:
            return [atividade.to_dict() for atividade in turma.atividades]
        return None
    
    def listar_turmas(self):
        return self.turma_repository.listar()
    