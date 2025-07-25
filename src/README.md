# Cómo usar el script split_readme_sections.py

Este script permite dividir el archivo `README.md` principal en archivos individuales, uno por cada sección marcada con `###`, y genera una tabla de contenidos con enlaces a cada archivo generado.

## Pasos para usar el script

1. **Ubicación del script:**
   - El script `split_readme_sections.py` debe estar en el directorio raíz del proyecto.
   - El archivo `README.md` debe estar también en el directorio raíz.

2. **Ejecución:**
   - Abre una terminal en la raíz del proyecto.
   - Ejecuta el siguiente comando:
     ```bash
     python3 split_readme_sections.py
     ```

3. **Resultado:**
   - Se creará (o actualizará) la carpeta `docs/` en la raíz del proyecto.
   - Dentro de `docs/` se generarán archivos `.md` numerados, uno por cada sección del README.
   - Se generará un archivo `00_TableofContents.md` con enlaces a cada sección.

4. **Notas:**
   - No se genera archivo de sección para la tabla de contenidos.
   - Si editas el README.md, puedes volver a ejecutar el script para actualizar los archivos.

## Ejemplo de uso

```bash
python3 split_readme_sections.py
```

Luego revisa la carpeta `docs/` para ver los archivos generados.
