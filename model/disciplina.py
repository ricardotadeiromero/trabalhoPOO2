from dataclasses import asdict, dataclass


@dataclass
class Disciplina:
    nome: str
    carga_horaria: int

    def __post_init__(self):
        if self.carga_horaria <= 0:
            raise ValueError("Carga horária inválida. Deve ser maior que zero.")

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
