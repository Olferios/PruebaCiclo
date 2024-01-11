from util import validar_opcion

def menu_principal():
    print("----------- Menú Principal-----------")
    print("1. Administrasdor de generos")
    print("2. Administrador de actores")
    print("3. Administrador de formatos")
    print("4. Gestor de informes")
    print("5. Gestor peliculas")
    print("6. Sañir")       
    op=validar_opcion("Opcion: ",1,6)
    return op

def menu_generos():
    print("----------- Menú Generos-----------")
    print("1. Crear genero")
    print("2. listar genero")
    print("3. Salir")
    op=validar_opcion("Opcion: ",1,3)
    return op
    
    
def menu_actores():
    print("----------- Menú actores-----------")
    print("1. Crear crear actor")
    print("2. listar actores")
    print("3.salir")
    
    op=validar_opcion("Opcion: ",1,3)
    return op

def menu_formatos():
    print("----------- Menú formatos-----------")
    print("1. Crear formato")
    print("2. Listar formato")
    print("3. Salir")
    
    op=validar_opcion("Opcion: ",1,3)
    return op

def menu_informes():
    print("----------- Menú Aulas-----------")
    print("1. Listar pelicula de un gnero especifico")
    print("2. Listar pelicula donde el protagonista sea silvestre")
    print("3. Buscar pelicula y monstrar siopsos y acotres")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_peliculas():
    print("----------- Menú Reportes-----------")
    print("1. Agregar pelicula")
    print("2. Editar peliocula")
    print("3. Eliminar pelicula")
    print("4. Eliminar actor")
    print("6. Listar todas peiculas")
    print("7. Salir")
    
    op=validar_opcion("Opcion: ",1,7)
    return op