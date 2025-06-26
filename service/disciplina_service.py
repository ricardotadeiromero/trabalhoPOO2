# services/disciplina_service.py
from model.disciplina import Disciplina

class DisciplinaService:
    def __init__(self, disciplina_repository):
        self.disciplina_repository = disciplina_repository

    def criar_disciplina(self, dados):
        disciplina = Disciplina.from_dict(dados)
        self.disciplina_repository.salvar(disciplina)
        return disciplina

    def obter_disciplina_por_nome(self, nome: str):
        return self.disciplina_repository.buscar_por_atributo("nome", nome)


    def deletar_disciplina(self, nome: str):
        return self.disciplina_repository.deletar("nome", nome)

    def listar_disciplinas(self):
        return self.disciplina_repository.listar()
