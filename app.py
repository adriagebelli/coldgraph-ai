import os
from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    company_name = data.get('company_name', '')
    
    prompt = f'Crea un missatge de cold emailing hiperpersonalitzat per a l\'empresa {company_name} basat en analítica predictiva i operatius públics.'
    
    try:
        response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=300
        )
        result = response.choices[0].message.content
        return jsonify({'success': True, 'email': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)