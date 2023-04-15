from pathlib import Path

base = Path.home()
guia = Path(base, 'Barcelona', 'sagrada_familia.txt')
guia2 = guia.with_name('la_Pedrera.txt')
print(guia)
print(guia2)
print(guia.parent)
print(guia.parent.parent)
print(base)
for txt in Path(guia).glob("**/*.txt"):
    print(txt)


guia3 = Path('Europa', 'España', 'Barcelona', 'Sagrada_familia')
en_europa = guia3.relative_to(Path('Europa'))
en_espania = guia3.relative_to(Path('Europa', 'España'))
print(en_europa)
print(en_espania)