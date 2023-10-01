# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")

define l = Character("Luz")


# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg room 

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    # show eileen happy

    show luz feliz

    # Presenta las líneas del diálogo.

    l "Bienvenidos a Saujilandia. El lugar donde tus sueños pueden hacerse realidad."
    with Dissolve(0.5)
    pause 0.2

    scene bg calle noche

    show luz picara at left

    l "Estaré encantada de caminar contigo en este viaje, ¡a darlo todo! y más jeje"

    

    # Finaliza el juego:

    return
