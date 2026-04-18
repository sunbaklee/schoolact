from flask import Flask, request, render_template_string, redirect, url_for
import sqlite3

app = Flask(__name__)

# --- 1. 데이터베이스 초기화 함수 ---
def init_db():
    conn = sqlite3.connect('phonebook.db') # phonebook.db 파일 생성 (없으면)
    c = conn.cursor()
    # contacts라는 이름의 테이블(표) 생성
    c.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# --- 2. 웹 화면 구성 (HTML 템플릿) ---
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>전화번호부 서버</title>
    <style>
        body { font-family: sans-serif; max-width: 500px; margin: 50px auto; }
        form { background: #f4f4f4; padding: 15px; border-radius: 5px; }
        input { margin: 5px 0; padding: 5px; width: 90%; }
        button { padding: 5px 15px; background: #28a745; color: white; border: none; cursor: pointer; }
        ul { list-style-type: none; padding: 0; }
        li { background: #eee; margin: 5px 0; padding: 10px; display: flex; justify-content: space-between; }
        a { color: red; text-decoration: none; font-size: 0.9em; }
    </style>
</head>
<body>
    <h2>📞 나의 전화번호부</h2>
    
    <form action="/add" method="POST">
        이름: <input type="text" name="name" required placeholder="예: 홍길동"><br>
        번호: <input type="text" name="phone" required placeholder="예: 010-1234-5678"><br>
        <button type="submit">연락처 저장</button>
    </form>

    <hr>

    <ul>
        {% for contact in contacts %}
            <li>
                <span><strong>{{ contact[1] }}</strong> ({{ contact[2] }})</span>
                <a href="/delete/{{ contact[0] }}">[삭제]</a>
            </li>
        {% else %}
            <li>저장된 연락처가 없습니다.</li>
        {% endfor %}
    </ul>
</body>
</html>
'''

# --- 3. 웹 서버 라우팅 (기능 구현) ---

# 메인 화면: DB에서 데이터를 읽어와서 화면에 보여줍니다 (Read)
@app.route('/')
def index():
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    c.execute('SELECT * FROM contacts') # 모든 연락처 가져오기
    contacts = c.fetchall()
    conn.close()
    
    return render_template_string(HTML_TEMPLATE, contacts=contacts)

# 연락처 추가 기능: 폼에서 데이터를 받아 DB에 저장합니다 (Create)
@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']
    
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    c.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index')) # 저장이 끝나면 메인 화면으로 돌아감

# 연락처 삭제 기능: 특정 ID의 데이터를 DB에서 지웁니다 (Delete)
@app.route('/delete/<int:id>')
def delete_contact(id):
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    c.execute('DELETE FROM contacts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

# --- 4. 서버 실행 ---
if __name__ == '__main__':
    init_db() # 프로그램 시작 시 DB 준비
    print("웹 서버가 시작됩니다! 브라우저에서 http://127.0.0.1:5000 으로 접속하세요.")
    app.run(debug=True, port=5000)
