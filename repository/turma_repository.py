import json
from typing import Optional
from model.turma import Turma


class TurmaRepository:
    def __init__(self, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo

    def salvar(self, turma: Turma):
        with open(self.caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump(turma.to_dict(), f, indent=4, ensure_ascii=False)

    def carregar(self) -> Optional[Turma]:
        try:
            with open(self.caminho_arquivo, "r", encoding="utf-8") as f:
                data = json.load(f)
                return Turma.from_dict(data)
        except FileNotFoundError:
            return None