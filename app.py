from src.calculate_price import get_total
from src.dictionary import Dictionary
from src.concatenate_letters import concatenate_letters
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/costs', methods=['POST'])
def calculate_costs():
    costs = {'socks': 5, 'shoes': 60, 'sweater': 30}
    try:
        data = request.get_json()

        item_list = data.get('items', [])
        tax = data.get('tax', 0.0)

        total = get_total(costs, item_list, tax)

        return jsonify({'total': total}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/concatenate', methods=['POST'])
def concatenate():
    try:
        data = request.get_json()

        words = data.get('words', [])

        result = concatenate_letters(words)

        return jsonify({'concatenated': result}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

d = Dictionary()

@app.route('/dictionary/newentry', methods=['POST'])
def add_entry():
    try:
        data = request.get_json()

        word = data.get('word')
        description = data.get('description')

        if not word or not description:
            return jsonify({'error': 'Both word and description are required.'}), 400

        d.newentry(word, description)

        return jsonify({'message': f'Entry for "{word}" added successfully.'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/dictionary/look', methods=['GET'])
def look_up_word():
    try:
        word = request.args.get('word')

        if not word:
            return jsonify({'error': 'Word parameter is required.'}), 400

        result = d.look(word)

        return jsonify({'word': word, 'description': result}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/health', methods=['GET'])
def health_check():
    
    return jsonify({
        'status': 'OK',
        'message': 'Service is up and running'
    }), 200
    

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)