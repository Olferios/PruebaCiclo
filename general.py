import json

genero = {}
actor = {}
formato = {}
pelicula={}

def cargar_datos():
    global genero, actor, formato,pelicula
    try:
        with open("generos.json", "r") as file:
            genero = json.load(file)
    except FileNotFoundError:
        genero = {}

    try:
        with open("actores.json", "r") as file:
            actor = json.load(file)
    except FileNotFoundError:
        actor = {}

    try:
        with open("formatos.json", "r") as file:
            formato = json.load(file)
    except FileNotFoundError:
        formato = {}
    
    try:
        with open("peliculas.json", "r") as file:
            pelicula = json.load(file)
    except FileNotFoundError:
        pelicula = {}


def guardar_datos():
    with open("generos.json", "w") as file:
        json.dump(genero, file, indent=2)

    with open("actores.json", "w") as file:
        json.dump(actor, file, indent=2)

    with open("formatos.json", "w") as file:
        json.dump(formato, file, indent=2)

    with open("peliculas.json", "w") as file:
        json.dump(pelicula, file, indent=2)

cargar_datos()

def crear_genero():
    global genero
    id_genero = input("Ingrese id genero: ")
    nombre_genero = input("Ingrese nombre genero: ")

    dic_genero = {
        id_genero: {
            "id": id_genero,
            "nombre": nombre_genero
        }
    }

    genero.update(dic_genero)
    guardar_datos()

def listar_genero():
    print("Lista de generos:")
    for id_genero, datos_genero in genero.items():
        print(f"ID: {id_genero}, Nombre: {datos_genero['nombre']}")

def crear_actor():
    global actor
    id_actor = input("Ingrese id actor: ")
    nombre_actor = input("Ingrese nombre actor: ")

    dic_actor = {
        id_actor: {
            "id": id_actor,
            "nombre": nombre_actor
        }
    }

    actor.update(dic_actor)
    guardar_datos()

def listar_actor():
    print("Lista de actores:")
    for id_actor, datos_actor in actor.items():
        print(f"ID: {id_actor}, Nombre: {datos_actor['nombre']}")

def crear_formatos():
    global formato
    id_formato = input("Ingrese id formato: ")
    nombre_formato = input("Ingrese nombre formato: ")

    dic_formato = {
        id_formato: {
            "id": id_formato,
            "nombre": nombre_formato
        }
    }

    formato.update(dic_formato)
    guardar_datos()

def listar_formato():
    print("Lista de formatos:")
    for id_formato, datos_formato in formato.items():
        print(f"ID: {id_formato}, Nombre: {datos_formato['nombre']}") 

def agregar_pelicula():
    id_pelicula = input("Ingrese id película: ")
    nombre_pelicula = input("Ingrese nombre película: ")
    duracion_pelicula = int(input("Ingrese duración película: "))
    sinopsis_pelicula = input("Ingrese sinopsis película: ")
    bus_id_genero = input("Ingrese id genero: ")
    bus_id_actor = input("Ingrese id actor: ")
    bus_id_formato = input("Ingrese id formato: ")


    if bus_id_genero in genero:
        resultado_id_genero = genero[bus_id_genero]
        resultado_nombre_genero = resultado_id_genero["nombre"]


        if bus_id_actor in actor:
            resultado_id_actor = actor[bus_id_actor]
            resultado_nombre_actor = resultado_id_actor["nombre"]


            if bus_id_formato in formato:
                resultado_id_formato = formato[bus_id_formato]
                resultado_nombre_formato = resultado_id_formato["nombre"]


                dic_pelicula = {
                    id_pelicula: {
                        "id": id_pelicula,
                        "nombrePel": nombre_pelicula,
                        "duracion": duracion_pelicula,
                        "sinopsis": sinopsis_pelicula,
                        resultado_id_genero["id"]: {
                            "idGen": resultado_id_genero["id"],
                            "nombreGen": resultado_nombre_genero
                        },
                        resultado_id_actor["id"]: {
                            "idAct": resultado_id_actor["id"],
                            "nombreAct": resultado_nombre_actor
                        },
                        resultado_id_formato["id"]: {
                            "idFor": resultado_id_formato["id"],
                            "nombrefor": resultado_nombre_formato
                        }
                    }
                }

                # Actualizar el diccionario de películas
                pelicula.update(dic_pelicula)
                guardar_datos()
            else:
                print("No se encontró el id de formato. Por favor, regístrelo antes.")
        else:
            print("No se encontró el id de actor. Por favor, regístrelo antes.")
    else:
        print("No se encontró el id de género. Por favor, regístrelo antes.")

#def editar_pelicula():

def eliminar_pelicula():
    dato=input("ingrese id de pelicula a eliminar")
    if dato in pelicula:
        del pelicula[dato]
        print("la pelicula ha sido eliminada")
        guardar_datos()
    else:
        print("la pelicula ingresada no esta")

def eliminar_actor():
    datoPelicula=input("ingrese id pelicula a buscar")
    if datoPelicula in pelicula:
        datoActor=input("ingrese id del actor a eliminar")
        if datoActor in pelicula[datoPelicula]:
            del pelicula[datoPelicula][datoActor]
            guardar_datos()
        else:
            print("no se encontro id")
    else:
        print("no se encontro pelicuyla")
    

def buscar_pelicula():
    datoBuscar = input("Ingrese ID de la película a buscar: ")
    if datoBuscar in pelicula:
        datos_pelicula = pelicula[datoBuscar]
        print(f"\nInformación de la película con ID {datoBuscar}:")
        print(f"ID: {datos_pelicula['id']}")
        print(f"Nombre: {datos_pelicula['nombrePel']}")
        print(f"Duración: {datos_pelicula['duracion']} minutos")
        print(f"Sinopsis: {datos_pelicula['sinopsis']}")
    else:
        print("Película no encontrada")

def listar_peliculas():
    if pelicula:
        print("\nLista de películas:")
        for id_pelicula, datos_pelicula in pelicula.items():
            print(f"\nID: {id_pelicula}")
            print(f"Nombre: {datos_pelicula['nombrePel']}")
            print(f"Duración: {datos_pelicula['duracion']} minutos")
            print(f"Sinopsis: {datos_pelicula['sinopsis']}")
            
            print("\nGénero:")
            
    else:
        print("No hay películas registradas.")

def buscar_peliculas_por_genero():
    genero_buscado=input("ingrese genero buscado")
    for peliculaid,peliculainfo in pelicula.items():
        if peliculainfo["genero"]["idGen"]==genero_buscado:
            print("ID:", peliculainfo["id"])
            print("Nombre:", peliculainfo["nombrePel"])
            break

def mostrar_informacion_pelicula():
    buscar_nombre_pel = input("Ingrese el nombre de la película: ")
    for pelicula_id, info_pelicula in pelicula.items():
        if info_pelicula["nombrePel"] == buscar_nombre_pel:
            id_actor = info_pelicula["actor"]["idAct"]
            nombre_actor = info_pelicula["actor"]   ["nombreAct"]
            print("ID del actor:", id_actor)
            print("Nombre del actor:", nombre_actor)
            return  
    
    print("Película no encontrada")




