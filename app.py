from flask import Flask, render_template, request, redirect, jsonify, url_for, make_response
import string
import random
import sqlite3
import logging
from urllib.parse import urlparse

app = Flask(__name__)

# 设置日志记录
logging.basicConfig(level=logging.INFO)

# 数据库初始化
def init_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS urls
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  original_url TEXT NOT NULL,
                  short_code TEXT NOT NULL UNIQUE)''')
    conn.commit()
    conn.close()

init_db()

# 生成短码
def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

# 主页
@app.route('/')
def index():
    return render_template('index.html')

# 生成短链接
@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.json['url']
    short_code = generate_short_code()
    
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("INSERT INTO urls (original_url, short_code) VALUES (?, ?)", (original_url, short_code))
    conn.commit()
    conn.close()
    
    short_url = url_for('redirect_to_url', short_code=short_code, _external=True)
    return jsonify({'short_url': short_url})

# 重定向
@app.route('/<short_code>')
def redirect_to_url(short_code):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("SELECT original_url FROM urls WHERE short_code = ?", (short_code,))
    result = c.fetchone()
    conn.close()
    
    if result:
        original_url = result[0]
        logging.info(f"Redirecting {short_code} to {original_url}")
        
        # 检查URL是否有协议前缀，如果没有则添加
        parsed_url = urlparse(original_url)
        if not parsed_url.scheme:
            original_url = "https://" + original_url
        
        # 使用渲染模板方式，适配微信
        return render_template('redirect.html', url=original_url)
    else:
        logging.warning(f"URL not found for short code: {short_code}")
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
