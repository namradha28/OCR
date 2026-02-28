import os
import io
import json
import yaml
import pandas as pd
from dicttoxml import dicttoxml
from flask import Flask, render_template, request, jsonify, send_file
from PIL import Image
import pytesseract

app = Flask(__name__)

# Tesseract Configuration
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process-ocr', methods=['POST'])
def process_ocr():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    file = request.files['image']
    format_type = request.form.get('format', 'json').lower()
    
    try:
        img = Image.open(file.stream)
        text = pytesseract.image_to_string(img)
        
        data = {
            "status": "success",
            "filename": file.filename,
            "extracted_text": text.strip() if text.strip() else "[No text detected]"
        }
        
        if format_type == 'json':
            return jsonify(data)
        elif format_type == 'xml':
            xml_data = dicttoxml(data, custom_root='ocr_result', attr_type=False)
            return send_file(io.BytesIO(xml_data), mimetype='application/xml', as_attachment=True, download_name='result.xml')
        elif format_type == 'yaml':
            yaml_data = yaml.dump(data, default_flow_style=False)
            return send_file(io.BytesIO(yaml_data.encode()), mimetype='application/x-yaml', as_attachment=True, download_name='result.yaml')
        elif format_type == 'csv':
            df = pd.DataFrame([data])
            output = io.StringIO()
            df.to_csv(output, index=False)
            return send_file(io.BytesIO(output.getvalue().encode()), mimetype='text/csv', as_attachment=True, download_name='result.csv')
        else:
            return jsonify(data)
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/ai-agent', methods=['POST'])
def ai_agent():
    user_msg = request.json.get('message', '').lower()
    
    # Simple rule-based AI Agent for project context
    responses = {
        "status": "The OCR project is currently running smoothly. We've optimized it for performance using PIL and Tesseract 5.5.",
        "who": "This project was customized for Namradha Mani. It's a premium OCR solution with multi-format support.",
        "formats": "I can export your results in JSON, XML, YAML, and CSV. Just pick your favorite!",
        "hello": "Hello Namradha Mani! I'm your AI OCR Assistant. How can I help you today?",
        "hi": "Hi there! Ready to digitize some documents?",
        "help": "You can upload an image in the tool section, and I'll extract the text for you. You can then download it in various formats!"
    }
    
    response = "I'm not sure about that, but I can help you with OCR, project status, and export formats! Just ask."
    for key in responses:
        if key in user_msg:
            response = responses[key]
            break
            
    return jsonify({"reply": response})

if __name__ == '__main__':
    app.run(debug=False, port=5000)
