from dataclasses import asdict, dataclass


@dataclass
class Nota:
    aluno_matricula: int
    valor: float

    def __post_init__(self):
        if not (0.0 <= self.valor <= 10.0):
            raise ValueError("Valor inválido. A nota deve estar entre 0 e 10.")

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
