
categorias= ("A","B","C","D","E")

def validar_categoria(categoria):
    if categoria.upper() in categorias:
        print("Categoria valida.")
    else:
        print("Categoria invalida.")
