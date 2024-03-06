from flask import Flask, render_template
import pyautogui
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ativar_automacao', methods=['POST'])
def ativar_automacao():
    pyautogui.click(838, 38, duration=5)
    pyautogui.write('dólar')  # Certifique-se de ajustar 'dólar' para o que você precisa
    time.sleep(10)
    return 'Automação ativada com sucesso!'

if __name__ == '_main_':
    app.run(debug=True)