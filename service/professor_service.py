# services/professor_service.py
from model.professor import Professor

class ProfessorService:
    def __init__(self, professor_repository):
        self.professor_repository = professor_repository

    def criar_professor(self, dados):
        professor = Professor.from_dict(dados)
        self.professor_repository.salvar(professor)
        return professor

    def obter_professor_por_cpf(self, cpf: str):
        return self.professor_repository.buscar_por_atributo("cpf", cpf)

    def deletar_professor(self, cpf: str):
        return self.professor_repository.deletar("cpf", cpf)
    
    def adicionar_disciplina(self, cpf_professor, disciplina):
        professor = self.professor_repository.buscar_por_atributo("cpf", cpf_professor)
        if professor:
            professor.ministrar_disciplina(disciplina)
            self.professor_repository.atualizar("cpf", professor)
            return professor
        return None

    def listar_professores(self):
        return self.professor_repository.listar()
