from general import*
from util import*
from menus import*
#bootstrap


# funtions
def genero():      
    limpiar_pantalla()
    op=menu_generos()
    if op==1:
        crear_genero()
        input("Clic cualquier teclas [continuar]: ")
    if op==2:
        listar_genero()
        input("Clic cualquier teclas [continuar]: ")
       
       
def actores():
    limpiar_pantalla()
    op=menu_actores()    
    if op==1:
        crear_actor()
        input("Clic cualquier teclas [continuar]: ")
    if op==2:
        listar_actor()
        input("Clic cualquier teclas [continuar]: ")
   
    
def formatos():
    limpiar_pantalla()    
    op=menu_formatos()
    if op==1:
        crear_formatos()
        input("Clic cualquier teclas [continuar]: ")
    if op==2:
        listar_formato()
        input("Clic cualquier teclas [continuar]: ")
      
        

def peliculas():
    limpiar_pantalla()    
    op=menu_peliculas()
    if op==1:
        agregar_pelicula()
    if op==3:
        eliminar_pelicula()
    if op==4:
        eliminar_actor()
    if op==5:
        buscar_pelicula()
    if op==6:
        listar_peliculas()


def informes():
    limpiar_pantalla()    
    op=menu_informes()
    if op==1:
        buscar_peliculas_por_genero()
    if op==3:
        mostrar_informacion_pelicula()

    

#start
while True: 
    limpiar_pantalla()
    op=menu_principal()
    if  op==1:
        genero()
    elif op==2:
        actores()
    elif op==3:
        formatos()
    elif op==4:
        informes()
    elif op==5:
        peliculas()
    elif op==6:
        print("Saliendo")
        break
