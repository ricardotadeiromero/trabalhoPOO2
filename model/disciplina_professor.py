from dataclasses import dataclass


@dataclass
class DisciplinaProfessor:
    disciplina_nome: str
    professor_cpf: str  # Relaciona a disciplina ao CPF do professor

    def to_dict(self):
        return {
            "disciplina_nome": self.disciplina_nome,
            "professor_cpf": self.professor_cpf,  # Serializa o CPF do professor
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            disciplina_nome=data["disciplina_nome"],
            professor_cpf=data["professor_cpf"],  # Deserializa o CPF do professor
        )
