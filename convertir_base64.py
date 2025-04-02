import base64
import os

# Ruta a la imagen original (ajusta según sea necesario)
ruta_imagen = r"C:\Users\pablo\Downloads\Captura de pantalla 2025-04-03 001500.png"

# Obtener nombre base sin extensión
nombre_base = os.path.splitext(os.path.basename(ruta_imagen))[0]

# Ruta del archivo .txt de salida (mismo directorio que la imagen)
directorio = os.path.dirname(ruta_imagen)
ruta_salida = os.path.join(directorio, f"{nombre_base}.txt")

# Leer imagen y codificar en base64
with open(ruta_imagen, "rb") as img_file:
    base64_string = base64.b64encode(img_file.read()).decode('utf-8')

# Guardar en .txt
with open(ruta_salida, "w", encoding='utf-8') as txt_file:
    txt_file.write(base64_string)

print(f"✅ Imagen convertida y guardada en:\n{ruta_salida}")
