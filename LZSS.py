class CompresorLZSS:
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size

    def comprimir(self, datos):
        buffer = ""
        comprimido = []  #Lista para almacenar los tokens comprimidos
        i = 0  #Índice para recorrer los datos de entrada

        while i < len(datos):
            mejor_longitud = 0  #Longitud de la mejor coincidencia encontrada
            mejor_posicion = 0  #Posición de la mejor coincidencia en el buffer

            #Buscar la coincidencia más larga en el buffer
            for j in range(1, len(buffer) + 1):
                longitud = 0
                #Comparar caracteres mientras coincidan y no excedan límites
                while (i + longitud < len(datos) and 
                       j + longitud <= len(buffer) and 
                       buffer[-j + longitud] == datos[i + longitud] and
                       longitud < self.buffer_size):
                    longitud += 1
                
                #Actualizar si encontramos una coincidencia más larga
                if longitud > mejor_longitud:
                    mejor_longitud = longitud
                    mejor_posicion = j

            #Codificar como referencia si la coincidencia es mayor a 1
            if mejor_longitud > 1:
                comprimido.append((0, mejor_posicion - 1, mejor_longitud))
                buffer += datos[i:i+mejor_longitud]
                i += mejor_longitud
            else:
                #Codificar como literal si no hay coincidencia suficiente
                comprimido.append((1, datos[i]))
                buffer += datos[i]
                i += 1

            #Mantener el tamaño del buffer
            buffer = buffer[-self.buffer_size:]

        return comprimido

    def descomprimir(self, comprimido):
        buffer = ""  #Buffer para almacenar datos descomprimidos recientemente
        descomprimido = ""

        for token in comprimido:
            if token[0] == 1:  #Si es un token literal
                descomprimido += token[1]  #Añadir el carácter literal
                buffer += token[1]  #Actualizar el buffer
            else:  #Si es una referencia
                posicion, longitud = token[1], token[2]
                inicio = len(buffer) - posicion - 1
                #Copiar caracteres desde el buffer
                for _ in range(longitud):
                    caracter = buffer[inicio]
                    descomprimido += caracter
                    buffer += caracter
                    inicio += 1

            #Mantener el tamaño del buffer
            buffer = buffer[-self.buffer_size:]

        return descomprimido

def main():
    #Abrir el archivo de registro
    with open("LZSS.log", "w") as log_file:
        #Pedir tamaño del buffer
        while True:
            try:
                buffer_size = int(input("Ingrese el tamaño del buffer (2-255): "))
                if 2 <= buffer_size <= 255:
                    break
                else:
                    print("El tamaño del buffer debe estar entre 2 y 255.")
                    log_file.write("El tamaño del buffer debe estar entre 2 y 255.\n")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
                log_file.write("Por favor, ingrese un número entero válido.\n")

        #Registrar el tamaño del buffer
        log_file.write(f"Tamaño del buffer: {buffer_size}\n")

        #Pedir mensaje a comprimir
        mensaje = input("Ingrese el mensaje a comprimir: ")

        #Crear compresor y comprimir
        compresor = CompresorLZSS(buffer_size)
        comprimido = compresor.comprimir(mensaje)

        #Descomprimir para verificar
        descomprimido = compresor.descomprimir(comprimido)

        #Guardar resultados en el archivo de registro
        log_file.write(f"\nMensaje original: {mensaje}\n")
        log_file.write(f"Mensaje comprimido: {comprimido}\n")
        log_file.write(f"Mensaje descomprimido: {descomprimido}\n")
        log_file.write(f"Compresión correcta: {mensaje == descomprimido}\n")

    print("Los resultados han sido guardados en 'LZSS.log'")

if __name__ == "__main__":
    main()