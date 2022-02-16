# 1. Ahora generamos un error porque config.txt es un directorio
#def main():
#    try:
#        configuration = open('config.txt')
#    except FileNotFoundError:
#        print("Couldn't find the config.txt file!")


# 2. Para controlar todas las exepciones usamos "Exception"
# pero esto es poco útil porque no nos da información sobre el tipo de error de nuestro código
#def main():
#    try:
#        configuration = open('config.txt')
#    except Exception:
#        print("Couldn't find the config.txt file!")


# 3. Correjimos para tener info del tipo de error
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

if __name__ == '__main__':
    main()