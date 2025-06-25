from dataclasses import dataclass, field
from typing import List, Optional

from model.nota import Nota


@dataclass
class AtividadeAvaliativa:
    nome: str  # Adiciona o atributo 'nome'
    descricao: str
    disciplina_nome: str
    notas: List[Nota] = field(default_factory=list)

    def adicionar_nota(self, nota: Nota):
        self.notas.append(nota)

    def get_nota_do_aluno(self, matricula: int) -> Optional[Nota]:
        for nota in self.notas:
            if nota.aluno_matricula == matricula:
                return nota
        return None

    def remover_nota_do_aluno(self, matricula: int):
        self.notas = [nota for nota in self.notas if nota.aluno_matricula != matricula]

    def to_dict(self):
        return {
            "nome": self.nome,
            "descricao": self.descricao,
            "disciplina_nome": self.disciplina_nome,
            "notas": [nota.to_dict() for nota in self.notas],
        }

    @classmethod
    def from_dict(cls, data):
        notas = [Nota.from_dict(n) for n in data.get("notas", [])]
        return cls(data["nome"], data["descricao"], data["disciplina_nome"], notas)