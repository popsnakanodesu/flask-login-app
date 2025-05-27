from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == 'johotaro2025':
            return "ログイン成功！🎉"
        else:
            return "パスワードが違います！"
    return '''
        <h2>ログイン画面</h2>
        <form method="post">
            パスワード: <input name="password" type="password">
            <button type="submit">ログイン</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
