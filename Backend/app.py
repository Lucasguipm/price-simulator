from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.amazon_utils import extract_asin, get_amazon_product_details
from services.history_service import generate_price_history

app = Flask(__name__)
CORS(app)

@app.route('/api/analyze', methods=['POST'])
def analyze_product():
    data = request.get_json()
    product_url = data.get('url') if data else None

    if not product_url:
        return jsonify({"error": "URL do produto é obrigatória."}), 400

    # 1. Valida a URL e extrai o ASIN
    asin = extract_asin(product_url)
    if not asin:
        return jsonify({"error": "URL da Amazon inválida ou ASIN não encontrado."}), 400

    # 2. Faz o Web Scraping dos dados reais da página
    product_details = get_amazon_product_details(product_url)
    if not product_details:
        return jsonify({"error": "Não foi possível acessar as informações do produto na Amazon."}), 500

    # 3. Gera o histórico de preços com base no preço atual raspado
    price_history = generate_price_history(product_details["current_price"])

    # 4. Retorna o payload completo para o Front-end
    return jsonify({
        "asin": asin,
        "title": product_details["title"],
        "image_url": product_details["image_url"],
        "current_price": product_details["current_price"],
        "history": price_history
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)