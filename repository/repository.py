import json
from typing import Type, TypeVar, Generic

T = TypeVar('T')  # Generic type variable

class Repository(Generic[T]):
    def __init__(self, file_path: str, cls: Type[T]):
        self.file_path = file_path
        self.cls = cls  # Class type for deserialization

    def salvar(self, obj: T):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(obj.to_dict(), file, ensure_ascii=False, indent=4)

    def carregar(self) -> T:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return self.cls.from_dict(data)
        except FileNotFoundError:
            return None