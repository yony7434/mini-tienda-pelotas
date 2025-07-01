# Mini Tienda Virtual de Pelotas de Fútbol

Una aplicación web Flask que simula una tienda virtual de pelotas de fútbol.

## Características

- Catálogo de productos con imágenes
- Carrito de compras con sesión
- Interfaz responsiva con Bootstrap
- Diseño moderno con tema verde y negro
- Manejo de cantidades y eliminación de productos

## Tecnologías

- Backend: Flask (Python)
- Frontend: HTML5 + Bootstrap 5
- Estilos: CSS personalizado
- JavaScript para interactividad

## Requisitos

- Python 3.8+
- Flask
- Flask-Session

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/yony7434/mini-tienda-pelotas.git
cd mini-tienda-pelotas
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecutar la aplicación:
```bash
python app.py
```

## Uso

1. Visitar la página principal para ver el catálogo
2. Agregar productos al carrito
3. Ver y gestionar el carrito de compras
4. Actualizar cantidades o eliminar productos

## Estructura del Proyecto

```
mini-tienda-pelotas/
├── app.py              # Aplicación Flask
├── requirements.txt    # Dependencias
├── static/
│   └── css/
│       └── style.css
└── templates/
    ├── base.html
    ├── index.html
    └── cart.html
```

## Licencia

MIT License
