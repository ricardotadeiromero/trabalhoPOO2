from dataclasses import asdict, dataclass, field
from typing import List
from model.pessoa import Pessoa


@dataclass
class Professor(Pessoa):
    area: str
    disciplinas_ministradas: List[str] = field(default_factory=list)  # nomes das disciplinas

    def ministrar_disciplina(self, nome_disciplina: str):
        if nome_disciplina not in self.disciplinas_ministradas:
            self.disciplinas_ministradas.append(nome_disciplina)

    def exibir(self):
        super().exibir()
        print(f"Tipo: Professor\nÁrea: {self.area}")
        if not self.disciplinas_ministradas:
            print("Nenhuma disciplina ministrada pelo professor.")
        else:
            print("Disciplinas ministradas:")
            for d in self.disciplinas_ministradas:
                print(f"- {d}")

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)