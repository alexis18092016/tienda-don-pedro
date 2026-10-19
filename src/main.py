from pathlib import Path

archivo = Path("datos/productos.txt")
lineas = archivo.read_text(encoding="utf-8").splitlines()

total = 0
valor = 0

print("=== Inventario Tienda Don Pedro ===")
for linea in lineas[2:]:
    if linea.strip():
        print("-", linea)
        precio = int(linea.split("$")[1].replace(".", ""))
        total += 1
        valor += precio

print("Total de productos:", total)
print("Valor del inventario: $" + str(valor))