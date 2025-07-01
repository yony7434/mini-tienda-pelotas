from flask import Flask, render_template, request, jsonify, session
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'  # Debería ser reemplazada con una clave segura en producción
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Datos de productos (simulados)
PRODUCTS = [
    {
        'id': 1,
        'name': 'Pelota Adidas',
        'price': 399.99,
        'image': '/static/images/pelota1.jpg',
        'description': 'Pelota oficial de competición, diseño clásico',
        'color': 'Blanco y negro'
    },
    {
        'id': 2,
        'name': 'Pelota Strike',
        'price': 499.99,
        'image': '/static/images/pelota2.jpg',
        'description': 'Pelota de alta resistencia, diseño moderno',
        'color': 'Rojo y Negro'
    },
    {
        'id': 3,
        'name': 'Pelota Puma Future',
        'price': 599.99,
        'image': '/static/images/pelota3.jpg',
        'description': 'Pelota profesional con tecnología Grip',
        'color': 'Blanco, azul , verde y naranja'
    },
    {
        'id': 4,
        'name': 'Pelota Adidas Modelo 2',
        'price': 299.99,
        'image': '/static/images/pelota4.jpg',
        'description': 'Pelota de entrenamiento, excelente relación calidad-precio',
        'color': 'Blanco, azul y naranga'
    }
]

@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    quantity = int(request.form.get('quantity', 1))
    product = next((p for p in PRODUCTS if p['id'] == int(product_id)), None)
    
    if not product:
        return jsonify({
            'success': False,
            'message': 'Producto no encontrado'
        }), 404

    if 'cart' not in session:
        session['cart'] = []
    
    existing_item = next((item for item in session['cart'] if item['id'] == product['id']), None)
    if existing_item:
        existing_item['quantity'] = min(existing_item.get('quantity', 1) + quantity, 10)  # Límite de 10 unidades
    else:
        product['quantity'] = min(quantity, 10)  # Límite de 10 unidades
        session['cart'].append(product)
    
    session.modified = True
    return jsonify({
        'success': True,
        'message': f'Se agregaron {quantity} unidades al carrito'
    })

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total = sum(item['price'] * item.get('quantity', 1) for item in cart_items)
    return render_template('cart.html', cart=cart_items, total=total)

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    if 'cart' not in session:
        return jsonify({
            'success': False,
            'message': 'Carrito no encontrado'
        }), 404

    session['cart'] = [item for item in session['cart'] if item['id'] != product_id]
    session.modified = True
    return jsonify({
        'success': True,
        'message': 'Producto eliminado del carrito'
    })

if __name__ == '__main__':
    app.run(debug=True)
