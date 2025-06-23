from model.aluno import Aluno
from model.atividade_avaliativa import AtividadeAvaliativa
from model.disciplina import Disciplina
from model.nota import Nota
from model.professor import Professor
from model.turma import Turma
from repository.turma_repository import TurmaRepository


if __name__ == "__main__":
    repo = TurmaRepository("turma.json")

    turma = repo.carregar()
    if turma is None:
        turma = Turma(nome="Turma 2025")

    aluno1 = Aluno("Ricardo Romero", "123456789", "1990-01-01", 1001)
    professor1 = Professor("Alan Turing", "987654321", "1912-06-23", "Computação")
    disciplina1 = Disciplina("Matemática", 60)

    turma.adicionar_aluno(aluno1)
    turma.adicionar_disciplina(disciplina1, professor1)

    atividade = AtividadeAvaliativa("Prova 1", "Prova de matemática", disciplina1.nome)
    atividade.adicionar_nota(Nota(aluno1.matricula, 9.5))
    turma.adicionar_atividade(atividade)

    turma.adicionar_professor_a_disciplina("Matemática", professor1)

    repo.salvar(turma)

    # Para verificar:
    turma_salva = repo.carregar()
    turma_salva.listar_pessoas = lambda: [a.exibir() for a in turma_salva.alunos]  # só demo
    print("Alunos carregados:")
    for aluno in turma_salva.alunos:
        aluno.exibir()
