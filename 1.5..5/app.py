from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "secret_key"

def init_db():
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, description TEXT, price REAL)")
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)")
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product = c.fetchone()
    conn.close()
    return render_template('product.html', product=product)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price = float(request.form['price'])
        conn = sqlite3.connect('shop.db')
        c = conn.cursor()
        c.execute("INSERT INTO products (title, description, price) VALUES (?, ?, ?)",
                  (title, description, price))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        conn = sqlite3.connect('shop.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
        except sqlite3.IntegrityError:
            return "Користувач вже існує."
        conn.close()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('shop.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = c.fetchone()
        conn.close()
        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            return redirect(url_for('index'))
        else:
            return "Невірні дані."
    return render_template('login.html')

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart_items = []
    if 'cart' in session:
        conn = sqlite3.connect('shop.db')
        c = conn.cursor()
        for pid in session['cart']:
            c.execute("SELECT * FROM products WHERE id = ?", (pid,))
            product = c.fetchone()
            if product:
                cart_items.append(product)
        conn.close()
    return render_template('cart.html', cart=cart_items)

if __name__ == '__main__':
    app.run(debug=True)