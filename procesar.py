import csv
import html

# Configuración del número de WhatsApp y mensaje predeterminado
NUMERO_WA = "50248502382"
MENSAJE_WA = "Hola, me gustaría realizar un pedido del catálogo DIPROSA."
URL_WA = f"https://wa.me/{NUMERO_WA}?text={html.escape(MENSAJE_WA)}"

def generar_catalogo():
    productos_html = ""
    
    # Leer el archivo catalogo.csv
    with open('catalogo.csv', mode='r', encoding='utf-8-sig') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            nombre = html.escape(fila.get('Producto', ''))
            precio = html.escape(fila.get('Precio', ''))
            imagen = html.escape(fila.get('Imagen', ''))
            
            # Generar tarjeta para cada producto
            productos_html += f'''
            <div class="card">
                <img src="{imagen}" alt="{nombre}" loading="lazy" onerror="this.src='https://via.placeholder.com/150?text=Sin+Imagen'">
                <h3>{nombre}</h3>
                <p class="precio">Q {precio}</p>
            </div>
            '''

    # Plantilla completa de la página Web HTML
    html_contenido = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Catálogo DIPROSA</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #121212;
            color: #ffffff;
            margin: 0;
            padding: 20px;
        }}
        h1 {{
            text-align: center;
            color: #f1c40f;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
            gap: 15px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        .card {{
            background-color: #1e1e1e;
            border-radius: 8px;
            padding: 10px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }}
        .card img {{
            width: 100%;
            height: 140px;
            object-fit: cover;
            border-radius: 5px;
        }}
        .card h3 {{
            font-size: 0.9em;
            margin: 10px 0 5px 0;
            height: 2.8em;
            overflow: hidden;
        }}
        .precio {{
            color: #2ecc71;
            font-weight: bold;
            font-size: 1.1em;
            margin: 5px 0;
        }}
        /* Botón flotante de WhatsApp */
        .whatsapp-btn {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #25d366;
            color: white;
            padding: 14px 22px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: bold;
            font-size: 16px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.4);
            z-index: 1000;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .whatsapp-btn:hover {{
            background-color: #1ebc57;
        }}
    </style>
</head>
<body>

    <h1>Catálogo DIPROSA</h1>
    
    <div class="grid">
        {productos_html}
    </div>

    <!-- Botón de WhatsApp -->
    <a href="{URL_WA}" class="whatsapp-btn" target="_blank" rel="noopener noreferrer">
        💬 Pedir por WhatsApp
    </a>

</body>
</html>
'''

    # Guardar la salida directamente en index.html
    with open('index.html', 'w', encoding='utf-8') as archivo_salida:
        archivo_salida.write(html_contenido)

    print("¡Catálogo e index.html generados exitosamente!")

if __name__ == '__main__':
    generar_catalogo()
