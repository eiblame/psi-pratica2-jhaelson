from models import Autor, Livro
def popular_banco(session):
    a1 = Autor(nome="Machado de Assis", pais="Brasil")
    a2 = Autor(nome="J.K. Rowling", pais="Reino Unido")
    a3 = Autor(nome="Clarice Lispector", pais="Brasil")

    l1 = Livro(titulo="Memórias Póstumas de Brás Cubas", ano=1881, autor=a1)
    l2 = Livro(titulo="Dom Casmurro", ano=1899, autor=a1)

    l3 = Livro(titulo="Harry Potter e a Pedra Filosofal", ano=1997, autor=a2)
    l4 = Livro(titulo="Harry Potter e a Câmara dos Segredos", ano=1998, autor=a2)
    l5 = Livro(titulo="Harry Potter e o Prisioneiro de Azkaban", ano=1999, autor=a2)

    l6 = Livro(titulo="A Hora da Estrela", ano=1977, autor=a3)

    session.add_all([a1, a2, a3, l1, l2, l3, l4, l5, l6])
    session.commit()