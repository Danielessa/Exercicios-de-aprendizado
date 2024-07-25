''' Desenvolver um sistema para gerenciar uma biblioteca, incluindo cadastro de livros, membros e empréstimos.'''

class Biblioteca:
    usuarios = ['daniel', 'lucas', 'camila']
    livros = ['Percy jackson', 'Harry potter', 'The begging after the end']
    emprestimos = {}
    @classmethod
    def cadastrar_livro(cls):
        livro =  input('Nome do livro: ' )
        cls.livros.append(livro)
        menu()

    @classmethod
    def cadastrar_usuario(cls):
        usuario = input('Qual o seu nome ?\n')
        cls.usuarios.append(usuario)
        menu()

    @classmethod
    def emprestar_livro(cls):
        usuario = input('Nome de quem deseja o livro: ')
        if usuario in cls.usuarios:
            livro = input('Nome do livro desejado: ')
            if livro in cls.livros: 
                cls.emprestimos.update({usuario:livro})
        menu()

def menu():
    print("""
    ==========
    MENU
    ==========

    1 - Cadastro usuario
    2 - Cadastro Livro
    3 - Emprestar Livro
    4 - Sair
    """)

    a = input()

    if a == '1':
        Biblioteca.cadastrar_usuario()

    elif a == '2':
        Biblioteca.cadastrar_livro()

    elif a == '3':
        Biblioteca.emprestar_livro()

menu()