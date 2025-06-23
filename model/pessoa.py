from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    cpf: str
    dt_nasc: str

    def exibir(self):
        print(f"Nome: {self.nome}\nCPF: {self.cpf}\nData de Nascimento: {self.dt_nasc}")