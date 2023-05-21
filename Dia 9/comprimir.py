import zipfile

mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

mi_zip.write('mi_textpo_A.txt')
mi_zip.write('mi_texto_b.txt')

mi_zip.close()