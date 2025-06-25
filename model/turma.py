from dataclasses import dataclass, field
from typing import List, Optional, Dict
from model.aluno import Aluno
from model.atividade_avaliativa import AtividadeAvaliativa
from model.disciplina import Disciplina
from model.disciplina_professor import DisciplinaProfessor
from model.professor import Professor


@dataclass
class Turma:
    nome: str
    alunos: List[Aluno]
    disciplinas_professores: List[Dict[str, str]]  # Relaciona disciplina_nome e professor_cpf
    atividades: List[AtividadeAvaliativa]
    professores: List[Professor]

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

    def adicionar_professor_a_disciplina(self, nome_disciplina: str, cpf_professor: str):
        # Verifica se o professor existe
        professor = next((p for p in self.professores if p.cpf == cpf_professor), None)
        if not professor:
            print(f"Professor com CPF {cpf_professor} não encontrado.")
            return

        # Adiciona a relação disciplina-professor
        for dp in self.disciplinas_professores:
            if dp.disciplina_nome == nome_disciplina:  # Corrigido para acessar o atributo diretamente
                dp.professor_cpf = cpf_professor  # Atualiza o CPF do professor na disciplina
                professor.ministrar_disciplina(nome_disciplina)
                print(f"Professor {professor.nome} associado à disciplina {nome_disciplina}.")
                return

        print(f"Disciplina {nome_disciplina} não encontrada.")

    def adicionar_professor(self, professor: Professor):
        self.professores.append(professor)
        print(f"Professor {professor.nome} adicionado à turma {self.nome} com sucesso!")

    # Métodos para atividades
    def adicionar_atividade(self, atividade: AtividadeAvaliativa):
        self.atividades.append(atividade)

    # Serialização e desserialização
    def to_dict(self):
        return {
            "nome": self.nome,
            "alunos": [aluno.to_dict() for aluno in self.alunos],
            "disciplinas_professores": [dp.to_dict() for dp in self.disciplinas_professores],  # Converte para dicionários
            "atividades": [atividade.to_dict() for atividade in self.atividades],
            "professores": [professor.to_dict() for professor in self.professores]
        }

    @classmethod
    def from_dict(cls, data):
        alunos = [Aluno.from_dict(a) for a in data.get("alunos", [])]
        disciplinas_professores = [DisciplinaProfessor.from_dict(dp) for dp in data.get("disciplinas_professores", [])]
        atividades = [AtividadeAvaliativa.from_dict(a) for a in data.get("atividades", [])]
        professores = [Professor.from_dict(p) for p in data.get("professores", [])]
        return cls(data["nome"], alunos, disciplinas_professores, atividades, professores)