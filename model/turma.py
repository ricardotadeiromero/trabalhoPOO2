from dataclasses import dataclass, field
from typing import List, Optional
from model.aluno import Aluno
from model.atividade_avaliativa import AtividadeAvaliativa
from model.disciplina import Disciplina
from model.disciplina_professor import DisciplinaProfessor
from model.professor import Professor


@dataclass
class Turma:
    nome: str
    alunos: List[Aluno] = field(default_factory=list)
    disciplinas_professores: List[DisciplinaProfessor] = field(default_factory=list)
    atividades: List[AtividadeAvaliativa] = field(default_factory=list)

    # Métodos para adicionar/remover alunos
    def adicionar_aluno(self, aluno: Aluno):
        if all(a.matricula != aluno.matricula for a in self.alunos):
            self.alunos.append(aluno)

    def remover_aluno_por_matricula(self, matricula: int):
        self.alunos = [a for a in self.alunos if a.matricula != matricula]

    # Métodos para disciplinas e professores
    def adicionar_disciplina(self, disciplina: Disciplina, professor: Optional[Professor] = None):
        dp = DisciplinaProfessor(disciplina.nome, professor)
        self.disciplinas_professores.append(dp)
        if professor:
            professor.ministrar_disciplina(disciplina.nome)

    def adicionar_professor_a_disciplina(self, nome_disciplina: str, professor: Professor):
        for dp in self.disciplinas_professores:
            if dp.disciplina_nome == nome_disciplina:
                dp.professor = professor
                professor.ministrar_disciplina(nome_disciplina)
                print(f"Professor {professor.nome} associado à disciplina {nome_disciplina}")
                return
        print(f"Disciplina {nome_disciplina} não encontrada.")

    # Métodos para atividades
    def adicionar_atividade(self, atividade: AtividadeAvaliativa):
        self.atividades.append(atividade)

    # Serialização e desserialização
    def to_dict(self):
        return {
            "nome": self.nome,
            "alunos": [aluno.to_dict() for aluno in self.alunos],
            "disciplinas_professores": [dp.to_dict() for dp in self.disciplinas_professores],
            "atividades": [atividade.to_dict() for atividade in self.atividades],
        }

    @classmethod
    def from_dict(cls, data):
        alunos = [Aluno.from_dict(a) for a in data.get("alunos", [])]
        disciplinas_professores = [DisciplinaProfessor.from_dict(dp) for dp in data.get("disciplinas_professores", [])]
        atividades = [AtividadeAvaliativa.from_dict(a) for a in data.get("atividades", [])]
        return cls(data["nome"], alunos, disciplinas_professores, atividades)