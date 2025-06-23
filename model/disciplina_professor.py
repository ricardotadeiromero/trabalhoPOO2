from dataclasses import dataclass
from typing import Optional

from model.professor import Professor


@dataclass
class DisciplinaProfessor:
    disciplina_nome: str
    professor: Optional[Professor] = None

    def to_dict(self):
        return {
            "disciplina_nome": self.disciplina_nome,
            "professor": self.professor.to_dict() if self.professor else None,
        }

    @classmethod
    def from_dict(cls, data):
        professor = Professor.from_dict(data["professor"]) if data.get("professor") else None
        return cls(data["disciplina_nome"], professor)
