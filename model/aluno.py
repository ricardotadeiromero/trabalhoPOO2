
from dataclasses import asdict, dataclass
from model.pessoa import Pessoa


@dataclass
class Aluno(Pessoa):
    matricula: int

    def exibir(self):
        super().exibir()
        print(f"Tipo: Aluno\nMatrícula: {self.matricula}")

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
