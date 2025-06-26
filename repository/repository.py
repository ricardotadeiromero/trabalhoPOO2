import json
from typing import Type, TypeVar, Generic

T = TypeVar('T')  # Generic type variable

class Repository(Generic[T]):
    def __init__(self, file_path: str, cls: Type[T]):
        self.file_path = file_path
        self.cls = cls  # Class type for deserialization

    def salvar(self, obj: T):
        objetos = self.listar()
        objetos.append(obj)
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump([o.to_dict() for o in objetos], file, ensure_ascii=False, indent=4)

    def carregar(self) -> list[T]:
        return self.listar()

    def carregar_por_id(self, id_valor) -> T | None:
        objetos = self.listar()
        for obj in objetos:
            if getattr(obj, 'id', None) == id_valor:
                return obj
        return None

    def atualizar(self, atributo: str, obj: T):
        objetos = self.listar()
        atualizado = False
        for i, existente in enumerate(objetos):
            if getattr(existente, atributo, None) == getattr(obj, atributo, None):
                objetos[i] = obj
                atualizado = True
                break
        if not atualizado:
            raise ValueError("Objeto não encontrado para atualização.")
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump([o.to_dict() for o in objetos], file, ensure_ascii=False, indent=4)

    def deletar_por_id(self, id_valor):
        objetos = self.listar()
        novos_objetos = [obj for obj in objetos if getattr(obj, 'id', None) != id_valor]
        if len(objetos) == len(novos_objetos):
            raise ValueError("Objeto não encontrado para exclusão.")
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump([o.to_dict() for o in novos_objetos], file, ensure_ascii=False, indent=4)

    def deletar(self, campo: str, valor):
        objetos = self.listar()
        novos_objetos = [obj for obj in objetos if getattr(obj, campo, None) != valor]
        if len(objetos) == len(novos_objetos):
            print(f"Objeto com {campo}={valor} não encontrado para exclusão.")
        else:
            print(f"Objeto com {campo}={valor} excluído com sucesso.")
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump([o.to_dict() for o in novos_objetos], file, ensure_ascii=False, indent=4)

    def listar(self) -> list[T]:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if isinstance(data, list):
                    return [self.cls.from_dict(item) for item in data]
                elif isinstance(data, dict) and data:
                    return [self.cls.from_dict(data)]
                return []
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []   
        except Exception as e:
            print(f"Erro ao listar objetos: {e}")
            return []

    def buscar_por_atributo(self, atributo: str, valor) -> list[T]:
        objetos = self.listar()
        lista = [obj for obj in objetos if getattr(obj, atributo, None) == valor]
        if lista:
            return lista[0]
        else:
            print(f"Nenhum objeto encontrado com {atributo} = {valor}")
    
    def buscar_por_atributo_parcial(self, atributo: str, valor: str) -> list[T]:
        objetos = self.listar()
        return [obj for obj in objetos if getattr(obj, atributo, "").lower().startswith(valor.lower())]