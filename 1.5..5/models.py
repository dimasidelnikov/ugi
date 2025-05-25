@app.route('/product/<int:product_id>')
def product(product_id):
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product = c.fetchone()
    conn.close()
    return render_template('product.html', product=product)
