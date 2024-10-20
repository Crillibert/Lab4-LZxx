import os

# Función para codificar usando LZ78 en formato <índice, entrada>
def lz78_encode(text):
    dictionary = {}
    data = []
    current_word = ""
    dict_size = 1

    for char in text:
        new_word = current_word + char
        if new_word not in dictionary:
            if current_word == "":
                data.append(f"<0,{char}>")
            else:
                data.append(f"<{dictionary[current_word]},{char}>")
            dictionary[new_word] = dict_size
            dict_size += 1
            current_word = ""
        else:
            current_word = new_word

    if current_word != "":
        data.append(f"<{dictionary[current_word]},>")

    return data

# Función para decodificar usando LZ78
def lz78_decode(encoded_data):
    dictionary = {}
    dict_size = 1
    decoded_text = ""

    for entry in encoded_data:
        # Extraer índice y carácter
        index, char = entry[1:-1].split(',')
        index = int(index)

        if index == 0:
            new_entry = char
        else:
            new_entry = dictionary[index] + char

        decoded_text += new_entry
        dictionary[dict_size] = new_entry
        dict_size += 1

    return decoded_text

# Función para guardar en un archivo log
def guardar_en_log(log_name, text, encoded_data):
    with open(log_name, 'a') as log_file:
        log_file.write("Texto original: " + text + "\n")
        log_file.write("Codificación LZ78: " + str(encoded_data) + "\n\n")

# Función para leer el archivo de texto
def leer_archivo_txt(file_name):
    with open(file_name, 'r') as file:
        return file.read()

# Función principal
def main():
    while True:
        print("\nOpciones:")
        print("1. Codificar archivo .txt con LZ78")
        print("2. Decodificar usando archivo log")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            txt_file = input("Introduce el nombre del archivo .txt (incluyendo extensión): ")
            if not os.path.exists(txt_file):
                print("Archivo no encontrado.")
                continue

            log_file = input("Introduce el nombre para el archivo log (incluyendo extensión): ")
            texto = leer_archivo_txt(txt_file)

            # Codificar
            codificacion = lz78_encode(texto)
            print("\nTexto original:\n", texto)
            print("\nCodificación LZ78:\n", codificacion)

            # Guardar en log
            guardar_en_log(log_file, texto, codificacion)
            print("\nCodificación guardada en log:", log_file)

        elif opcion == '2':
            log_file = input("Introduce el nombre del archivo log (incluyendo extensión): ")
            if not os.path.exists(log_file):
                print("Archivo log no encontrado.")
                continue

            # Leer archivo log
            with open(log_file, 'r') as log:
                contenido = log.readlines()

            # Extraer la codificación del log
            codificacion_str = contenido[-2].replace("Codificación LZ78: ", "").strip()
            codificacion = eval(codificacion_str)  # Convertir string a lista de tuplas

            # Decodificar
            texto_decodificado = lz78_decode(codificacion)
            print("\nTexto decodificado:\n", texto_decodificado)

        elif opcion == '3':
            print("Saliendo...")
            break

        else:
            print("Opción no válida, intenta nuevamente.")

if __name__ == "__main__":
    main()
