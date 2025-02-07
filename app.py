from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze_cv', methods=['POST'])
def analyze_cv():
    data = request.json
    cv_text = data.get("cv_text", "")
    word_count = len(cv_text.split())
    return jsonify({"word_count": word_count, "message": "Analyse réussie !"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
