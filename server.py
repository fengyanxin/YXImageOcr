import cv2
import numpy as np
import pytesseract
from flask import Flask, request, jsonify, send_from_directory, make_response
from PIL import Image
import io
import base64
import os
import uuid

app = Flask(__name__, static_folder='.')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    return response

LANG_MAP = {
    'chi_sim': 'chi_sim',
    'chi_tra': 'chi_tra',
    'eng': 'eng',
    'jpn': 'jpn',
}

@app.route('/ocr', methods=['OPTIONS'])
@app.route('/ocr/url', methods=['OPTIONS'])
def handle_options():
    response = make_response()
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    return response

def preprocess_image(img_array):
    import sys
    sys.stdout.flush()
    print(f"Input image shape: {img_array.shape}", flush=True)
    
    img = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    print(f"Grayscale shape: {img.shape}", flush=True)
    
    h, w = img.shape
    if h > 3000:
        new_w = int(w * 1000 / h * 1.5)
        new_h = int(1000 * 1.5)
        img = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_CUBIC)
        print(f"Resized to: {img.shape}")
    elif h < 1000:
        img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        print(f"Resized 2x to: {img.shape}")
    
    img = cv2.bilateralFilter(img, 9, 75, 75)
    
    print(f"Output shape: {img.shape}", flush=True)
    return img

def preprocess_image_simple(img_array):
    img = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    return img

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/ocr', methods=['POST'])
def ocr():
    data = request.json
    image_data = data.get('image')
    lang = data.get('lang', 'chi_sim')
    
    if not image_data:
        return jsonify({'error': 'No image provided'}), 400
    
    try:
        print(f"Received image data length: {len(image_data)}", flush=True)
        
        if image_data.startswith('data:image'):
            header, image_data = image_data.split(',', 1)
        
        image_bytes = base64.b64decode(image_data)
        print(f"Decoded bytes length: {len(image_bytes)}", flush=True)
        
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            return jsonify({'error': 'Failed to decode image'}), 400
        
        print(f"Image shape: {img.shape}", flush=True)
        
        processed = preprocess_image(img)
        
        lang_code = LANG_MAP.get(lang, 'chi_sim')
        
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(processed, lang=lang_code, config=custom_config)
        
        return jsonify({'text': text.strip()})
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/ocr/url', methods=['POST'])
def ocr_url():
    data = request.json
    url = data.get('url')
    lang = data.get('lang', 'chi_sim')
    
    if not url:
        return jsonify({'error': 'No URL provided'}), 400
    
    try:
        import requests as req
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        response = req.get(url, timeout=30, headers=headers)
        response.raise_for_status()
        
        nparr = np.frombuffer(response.content, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            return jsonify({'error': 'Failed to download image'}), 400
        
        processed = preprocess_image(img)
        
        lang_code = LANG_MAP.get(lang, 'chi_sim')
        
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(processed, lang=lang_code, config=custom_config)
        
        return jsonify({'text': text.strip()})
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting OCR server on http://localhost:5001")
    app.run(host='0.0.0.0', port=5001, debug=False, threaded=True)
