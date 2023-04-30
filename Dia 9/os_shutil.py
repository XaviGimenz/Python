import os
import shutil
import send2trash

print(os.getcwd())

archivo = open('curso.txt', 'w')
archivo.write('texto de prueba')
archivo.close()

ruta = '/Users/xaviergimenez/Desktop'
for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'en la carpeta {carpeta}')
    print(f'las subcarpetas son')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('los archivos son')
    for arch in archivo:
        print(f'\t{archivo}')
    print('\n')
print(os.listdir())
send2trash.send2trash('curso.txt')
# shutil.move('curso.txt', '/Users/xaviergimenez/Desktop')
