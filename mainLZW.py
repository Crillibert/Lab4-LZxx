import LZW
print("--------------------------------------------------")
nombre = input("Ingrese nombre del archivo txt a comprimir: \n")
print("--------------------------------------------------")
try:
    print("--------------------------------------------------")
    LZW.codificacionLZW(nombre)
    print("--------------------------------------------------")
except:
    print("El archivo no existe:")
print("--------------------------------------------------")
nombre = input("Ingrese nombre del archivo a descomprimir: \n")
print("--------------------------------------------------")
try:
    print("--------------------------------------------------")
    LZW.decodificacionLZW(nombre)
    print("--------------------------------------------------")
except:
    print("--------------------------------------------------")
    print("El archivo no existe:")
    print("--------------------------------------------------")