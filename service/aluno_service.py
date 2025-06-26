# services/aluno_service.py

from model.aluno import Aluno


class AlunoService:
    def __init__(self, aluno_repository):
        self.aluno_repository = aluno_repository

    def criar_aluno(self, dados):
        aluno = Aluno.from_dict(dados)
        if self.obter_aluno_por_matricula(aluno.matricula):
            raise ValueError(f"Aluno com matrícula {aluno.matricula} já existe.")
        return self.aluno_repository.salvar(aluno)

    def obter_aluno_por_matricula(self, matricula):
        return self.aluno_repository.buscar_por_atributo("matricula", matricula)

    def deletar_aluno(self, matricula):
        return self.aluno_repository.deletar("matricula", matricula)

    def listar_alunos(self):
        return self.aluno_repository.listar()
