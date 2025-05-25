# app.py
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Ініціалізація бази даних
def init_db():
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()

init_db()
