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
