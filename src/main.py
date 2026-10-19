from pathlib import Path

archivo = Path("datos/productos.txt")
lineas= archivo.read_text(encoding="utf-8").splitlines()

print("=== Inventario tienda Don Pedro ===")
for linea in lineas[2:]:
    print("-", linea)
