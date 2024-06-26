from flask import Flask, request, jsonify
from service.convert_service import convert_yt_to_text, convert_audio_to_text
from service.summary_service import summarize_text
from service.translate_service import translate_text

def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False  # Configura Flask para que no use ASCII para JSON


    @app.route('/')
    def home():
        return 'Hello, World!'

    @app.route('/convert', methods=['POST'])
    def convert():
        try:
            url = request.json['url']
            if url is None:
                return jsonify({"error": "URL is required"}), 400
            
            result = convert_yt_to_text(url)
            return jsonify(result), 200
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @app.route('/demo', methods=['POST'])
    def demo():
        try:
            url = request.json['url']
            if url is None:
                return jsonify({"error": "URL is required"}), 400
            
            result = {
                "url": url,
                "message": "Si origin\u00f3 despu\u00e9s de la Segunda Guerra Mundial con la prueba de Turin, y el t\u00e9rmino fue acu\u00f1ado en 1956. Actualmente, abarca subcampos como el reconocimiento de voz, el diagn\u00f3stico de enfermedades y la creaci\u00f3n de arte. La IA ha impulsado estudios sobre \u00e9tica y robotica, abordando c\u00f3mo deben comportarse estas tecnolog\u00edas en distintos \u00e1mbitos. La IA se clasifica en d\u00e9bil, que realiza tareas espec\u00edficas y general, que superar\u00eda las capacidades humanas a\u00fan en desarrollo. Ejemplos contempor\u00e1neos incluyen asistentes virtuales, traductores autom\u00e1ticos, sistemas de recomendaci\u00f3n y veh\u00edculos aut\u00f3nomos. La IA sigue evolucionando, creando nuevas herramientas como Sivium, una plataforma laboral automatizada lanzada en 2023.",
                "lang": "es"
            }
            return jsonify(result), 200
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/file', methods=['POST'])
    def whisper():
        try:
            file = request.files['file']
            if file is None:
                return jsonify({"error": "File is required"}), 400
            result = convert_audio_to_text(file)
            return jsonify(result), 200
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/summarize', methods=['POST'])
    def summarize():
        try:
            text = request.json['text']
            if text is None:
                return jsonify({"error": "Text is required"}), 400
            
            result = summarize_text(text)
            return jsonify(result), 200
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/translate', methods=['POST'])
    def translate():
        try:
            text = request.json['text']
            language = request.json['language']
            if text is None or language is None:
                return jsonify({"error": "Text and language are required"}), 400
            
            result = translate_text(text, language)
            return jsonify(result), 200
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()