from pathlib import Path, PureWindowsPath

carpeta = Path('/Users/xaviergimenez/Desktop/prueba/prueba.txt')

print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)
if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("El archivo existe")

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)
print('hola')