# Generador de Códigos QR :computer:

Aplicación de escritorio en Python con interfaz gráfica (Tkinter) para generar códigos QR y guardarlos como imágenes .png.

Permite ingresar texto o una URL, elegir la ruta de salida y generar el archivo fácilmente.

## Requisitos 

- Python 3.13 o superior
- pip (incluido con Python)

### Verificar versión instalada:
```
python --version
```

## Instalación

1. Clonar el repositorio:
```
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```
2. Instalar dependencias:
```
pip install -r requirements.txt
```

## Ejecución

Desde la raíz del proyecto:
```
python qr.py
```

## Uso de la interfaz

1. Escribir el texto o URL en el primer campo.
2. Elegir el nombre o ruta del archivo de salida (.png).
- Puedes usar el botón "Elegir ruta...".
3. Presionar "Generar QR".
4. El archivo se guardará en la ubicación indicada.

## Estructura del proyecto

```
/
│── qr.py
│── requirements.txt
│── README.md
```
- qr.py → Código principal de la aplicación.
- requirements.txt → Dependencias del proyecto.
- README.md → Documentación del proyecto.

## Troubleshooting

### Error:
```
ModuleNotFoundError: No module named 'qrcode'
```
### Solución:
Ejecutar nuevamente:
```
pip install -r requirements.txt
```
Si el problema persiste, verificar que estás usando la misma versión de Python donde instalaste las dependencias.
