from sqlalchemy import select
from models import Autor, Livro
def listar_livros(session):
    res = session.scalars(select(Livro))
    for livro in res:
        print(f"- {livro.titulo} ({livro.ano}) — {livro.autor.nome}")
        
def livros_por_autor(session, nome_autor):
    busca = select(Livro).join(Livro.autor).where(Autor.nome == nome_autor)
    res = session.scalars(busca)
    encontrados = list(res)
    if not encontrados:
        print(f"Nenhum livro encontrado para {nome_autor}")
        return
    for l in encontrados:
        print(f"- {l.titulo} — {l.ano}")


def buscar_livros(session, trecho):
    busca = select(Livro).where(Livro.titulo.ilike(f"%{trecho}%"))
    res = session.scalars(busca)
    for livro in res:
        print(f"- {livro.titulo} ({livro.ano}) — {livro.autor.nome}")


def listar_autores_com_quantidade(session):
    res = session.scalars(select(Autor))
    for aut in res:
        print(f"{aut.nome}: {len(aut.livros)} livro(s)")


def detalhes_livro(session, titulo):
    livro = session.scalar(select(Livro).where(Livro.titulo == titulo))
    if not livro:
        print("Livro não encontrado.")
        return
    print(f"Título: {livro.titulo}")
    print(f"Ano: {livro.ano}")
    print(f"Autor: {livro.autor.nome}")
    print(f"País do autor: {livro.autor.pais}")