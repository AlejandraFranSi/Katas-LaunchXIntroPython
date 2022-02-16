# 1. Tratamos de abrir un archivo inexistente y obtenemos un traceback que nos da información sobre el error
# El traceback nos dice en qué líneas se encuentran los problemas y qué tipo de error se presenta
#open("/path/to/mars.jpg")

# 2. Generamos una función que abre un archivo inexistente, por lo que se genera un error de tipo FileNotFound
#def main():
#    open("/path/to/mars.jpg")

# 3. Tratamos de solucionar el problema con un bloque try/except
try:
     open('config.txt')
except FileNotFoundError:
     print("Couldn't find the config.txt file!")

if __name__ == '__main__':
    main()

# 4.1.  Si necesitamos acceder al error asociado a la excepción usamos 'except as'
try:
     open("mars.jpg")
except FileNotFoundError as err:
     print("got a problem trying to read the file:", err)

# 4.2 
try:
     open("config.txt")
except OSError as err:
     if err.errno == 2:
         print("Couldn't find the config.txt file!")
     elif err.errno == 13:
         print("Found config.txt but couldn't read it")