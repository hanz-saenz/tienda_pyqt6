# Tienda Virtual - PyQt6

## Descripción
Esta es una aplicación de escritorio para una tienda virtual desarrollada con **Python** y **PyQt6**. Permite a los usuarios registrarse, iniciar sesión, gestionar categorías, marcas y productos, y asociar fotos a los productos. La aplicación utiliza **SQLite** como base de datos y almacena las rutas de las imágenes en una carpeta local. PyQt6 proporciona una interfaz moderna y profesional.

### Funcionalidades
- Registro e inicio de sesión con autenticación segura (contraseñas hasheadas con `bcrypt`).
- Gestión de categorías: crear y listar.
- Gestión de marcas: crear y listar.
- Gestión de productos: crear, asociar categorías y marcas, y subir fotos.
- Visualización de imágenes de productos en la interfaz.

## Requisitos
- Python 3.8 o superior
- Dependencias:
  - `PyQt6`: Para la interfaz gráfica.
  - `bcrypt`: Para hashear contraseñas.
  - `Pillow`: Para manejar imágenes.
- Sistema operativo: Windows, macOS o Linux.

## Estructura del Proyecto
```
tienda_pyqt6/
├── images/           # Carpeta para almacenar fotos de productos
├── tienda.db        # Base de datos SQLite
├── main.py          # Punto de entrada principal
├── database.py      # Lógica de base de datos
├── auth.py          # Lógica de autenticación
└── gui.py           # Interfaz gráfica con PyQt6
```

## Instalación
1. Clona o descarga el repositorio:
   ```bash
   git clone <URL-del-repositorio>
   cd tienda_pyqt6
   ```
2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Crea la carpeta `images/` en el directorio raíz:
   ```bash
   mkdir images
   ```

## Ejecución
1. Asegúrate de estar en el directorio del proyecto y que el entorno virtual esté activado (si lo usas).
2. Ejecuta la aplicación:
   ```bash
   python main.py
   ```
3. La aplicación se abrirá en una ventana de login. Regístrate, inicia sesión y usa el menú principal para gestionar categorías, marcas y productos.

## Despliegue
Para distribuir la aplicación como un ejecutable independiente:
1. Instala PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Genera el ejecutable:
   ```bash
   pyinstaller --add-data "images;images" --onefile main.py
   ```
3. Encuentra el ejecutable en la carpeta `dist/`.
4. Copia la carpeta `images/` y el archivo `tienda.db` (si existe) a la misma carpeta que el ejecutable.
5. Ejecuta el archivo `.exe` (Windows) o el binario correspondiente (Linux/macOS).

## Notas Adicionales
- **Seguridad**: Las contraseñas se almacenan hasheadas con `bcrypt`. Para producción, considera usar una base de datos más robusta (como PostgreSQL) y autenticación con tokens.
- **Imágenes**: Las fotos de los productos deben estar en formatos `.png`, `.jpg` o `.jpeg` y se almacenan en la carpeta `images/`.
- **Base de datos**: Si `tienda.db` no existe, se creará automáticamente al iniciar la aplicación.
- **Pruebas**: Implementa pruebas unitarias y de integración para `database.py` y `auth.py` usando `unittest` o `pytest`. Para pruebas de GUI, considera `pytest-qt`.
- **Diseño**: Usa Qt Designer para crear interfaces más complejas visualmente.

## Contribuciones
Si deseas contribuir, crea un *pull request* con tus cambios. Asegúrate de incluir pruebas para cualquier nueva funcionalidad.

