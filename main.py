from flask import Flask, request, render_template_string, redirect, url_for
import uuid

app = Flask(__name__)

pages = {}

@app.route('/')
def index():
    return render_template_string('''
    <h1>创建可编辑页面</h1>
    <form action="/create" method="post">
        <textarea name="content" rows="10" cols="50" placeholder="输入页面内容"></textarea><br>
        <input type="submit" value="创建页面">
    </form>
    ''')

@app.route('/create', methods=['POST'])
def create():
    content = request.form['content']
    page_id = str(uuid.uuid4())
    pages[page_id] = content
    return redirect(url_for('edit', page_id=page_id))

@app.route('/edit/<page_id>', methods=['GET', 'POST'])
def edit(page_id):
    if request.method == 'POST':
        pages[page_id] = request.form['content']
    
    content = pages.get(page_id, '')
    page_url = url_for('view', page_id=page_id, _external=True)
    
    return render_template_string('''
    <h1>编辑页面</h1>
    <form method="post">
        <textarea name="content" rows="10" cols="50">{{ content }}</textarea><br>
        <input type="submit" value="保存更改">
    </form>
    <p>页面 URL: <input type="text" value="{{ page_url }}" readonly style="width: 100%; padding: 5px;"></p>
    <p>您可以复制上面的 URL 并分享给他人。</p>
    ''', content=content, page_url=page_url)

@app.route('/view/<page_id>')
def view(page_id):
    content = pages.get(page_id, '页面不存在')
    return render_template_string('''
    <h1>查看页面</h1>
    <div>{{ content | safe }}</div>
    ''', content=content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
