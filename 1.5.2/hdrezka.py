from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']
        genre_id = request.form['genre']

        conn = sqlite3.connect("cinema.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO movies (title, year, genre_id) VALUES (?, ?, ?)", (title, year, genre_id))
        conn.commit()
        conn.close()

    conn = sqlite3.connect("cinema.db")
    cursor = conn.cursor()
    cursor.execute("SELECT m.title, m.year, g.name FROM movies m JOIN genres g ON m.genre_id = g.id")
    movies = cursor.fetchall()
    conn.close()

    return render_template_string('''
        <h1>Додати фільм</h1>
        <form method="POST">
            Назва: <input name="title"><br>
            Рік: <input name="year" type="number"><br>
            Жанр (ID): <input name="genre" type="number"><br>
            <input type="submit" value="Додати">
        </form>
        <h2>Список фільмів</h2>
        <ul>
        {% for title, year, genre in movies %}
            <li>{{ title }} ({{ year }}) — {{ genre }}</li>
        {% endfor %}
        </ul>
    ''', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)