#!/usr/bin/env python3

import base64
import gzip
import json
from PIL import Image
from pyzbar import pyzbar
try:
    import cv2  # repli optionnel (OpenCV) ; pyzbar suffit dans 95% des cas
except Exception:
    cv2 = None

def decode_qr_from_image(image_path):
    try:
        image = Image.open(image_path)
        qr_codes = pyzbar.decode(image)

        if qr_codes:
            for qr_code in qr_codes:
                return qr_code.data.decode('utf-8')

        if cv2 is not None:
            img = cv2.imread(image_path)
            if img is not None:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                qr_codes = pyzbar.decode(gray)
                if qr_codes:
                    for qr_code in qr_codes:
                        return qr_code.data.decode('utf-8')

        return None

    except Exception:
        return None

def decode_base64_data(base64_string):
    try:
        base64_string = base64_string.strip().replace('\n', '').replace('\r', '').replace(' ', '')
        decoded_data = base64.b64decode(base64_string)
        return decoded_data
        
    except Exception:
        return None

def decompress_gzip(data):
    try:
        decompressed = gzip.decompress(data)
        result = decompressed.decode('utf-8')
        return result
    except Exception:
        return None

def parse_qr_to_json(decoded_text):
    try:
        lines = decoded_text.strip().split('\n')
        
        json_structure = {
            "main_barcode": {
                "font-size": 21,
                "font-family": "ARIAL.ttf",
                "elements": {
                    "barcode": {
                        "barcode": "",
                        "barcode_height": 136,
                        "barcode_module_width": 3,
                        "coords": {"x": 130, "y": 20}
                    },
                    "text": {
                        "text": "",
                        "coords": {"x": 247, "y": 168}
                    }
                }
            },
            "sub_barcode": {
                "font-size": 14,
                "font-family": "ARIAL.ttf",
                "elements": {
                    "barcode": {
                        "barcode": "",
                        "barcode_height": 40,
                        "barcode_module_width": 2,
                        "coords": {"x": 486, "y": 863}
                    },
                    "text": {
                        "text": "",
                        "coords": {"x": 486, "y": 851}
                    }
                }
            },
            "expediteur": {
                "font-family": "ARIAL.ttf",
                "font-size": 13,
                "elements": {
                    "name": {"text": "", "coords": {"x": 45, "y": 242}},
                    "address": {"text": "", "coords": {"x": 45, "y": 268}},
                    "post": {"text": "", "coords": {"x": 45, "y": 297}},
                    "city": {"text": "", "coords": {"x": 45, "y": 311}}
                }
            },
            "destinataire": {
                "font-family": "ARIAL.ttf",
                "font-size": 19,
                "elements": {
                    "name": {"text": "", "coords": {"x": 39, "y": 410}},
                    "address": {"text": "", "coords": {"x": 39, "y": 453}},
                    "service": {"text": "", "coords": {"x": 39, "y": 498}},
                    "city": {"text": "", "coords": {"x": 39, "y": 520}}
                }
            },
            "meta": {
                "font-family": "ARIAL.ttf",
                "font-size": 14,
                "elements": {
                    "expedition": {"text": "", "coords": {"x": 57, "y": 662}},
                    "date": {"text": "", "coords": {"x": 217, "y": 662}},
                    "poids": {"text": "", "coords": {"x": 58, "y": 728}},
                    "volume": {"text": "", "coords": {"x": 218, "y": 728}},
                    "colis": {"text": "", "font-size": 15, "coords": {"x": 360, "y": 728}}
                }
            },
            "identification": {
                "font-family": "ARIALBD.ttf",
                "font-size": 40,
                "elements": {
                    "ag": {"text": "", "coords": {"x": 496, "y": 268}},
                    "n": {"font-size": 33, "text": "", "coords": {"x": 462, "y": 322}},
                    "t": {"font-size": 33, "text": "", "coords": {"x": 457, "y": 368}},
                    "package": {"text": "", "font-size": 63, "coords": {"x": 406, "y": 412}},
                    "service": {"font-size": 49, "text": "", "coords": {"x": 407, "y": 486}}
                }
            }
        }
        
        def get_line(index):
            return lines[index].strip() if index < len(lines) else ""
        
        if len(lines) > 2:
            json_structure["identification"]["elements"]["ag"]["text"] = get_line(2)
            
        if len(lines) > 3:
            json_structure["identification"]["elements"]["n"]["text"] = get_line(3)
            
        if len(lines) > 4:
            json_structure["identification"]["elements"]["service"]["text"] = get_line(4)
            
        if len(lines) > 5:
            json_structure["identification"]["elements"]["t"]["text"] = get_line(5)
            
        if len(lines) > 6:
            json_structure["identification"]["elements"]["package"]["text"] = get_line(6)
            
        if len(lines) > 9:
            barcode_value = get_line(9)
            json_structure["main_barcode"]["elements"]["barcode"]["barcode"] = barcode_value
            
        if len(lines) > 10:
            json_structure["main_barcode"]["elements"]["text"]["text"] = get_line(10)
            
        if len(lines) > 12:
            colis1 = get_line(11)
            colis2 = get_line(12)
            json_structure["meta"]["elements"]["colis"]["text"] = f"{colis1} / {colis2}"
            
        if len(lines) > 13:
            json_structure["meta"]["elements"]["volume"]["text"] = get_line(13)
            
        if len(lines) > 14:
            json_structure["meta"]["elements"]["date"]["text"] = get_line(14)
            
        if len(lines) > 15:
            json_structure["meta"]["elements"]["poids"]["text"] = get_line(15)
            
        if len(lines) > 16:
            sub_barcode_value = get_line(16)
            json_structure["sub_barcode"]["elements"]["text"]["text"] = sub_barcode_value
            json_structure["sub_barcode"]["elements"]["barcode"]["barcode"] = sub_barcode_value
            
        if len(lines) > 20:
            json_structure["meta"]["elements"]["expedition"]["text"] = get_line(20)
            
        if len(lines) > 21:
            json_structure["expediteur"]["elements"]["name"]["text"] = get_line(21)
            
        if len(lines) > 23:
            json_structure["expediteur"]["elements"]["address"]["text"] = get_line(23)
            
        if len(lines) > 26:
            fr_code = get_line(25)
            postal_code = get_line(26)
            json_structure["expediteur"]["elements"]["post"]["text"] = f"{fr_code} {postal_code}"
            
        if len(lines) > 27:
            json_structure["expediteur"]["elements"]["city"]["text"] = get_line(27)
            
        if len(lines) > 28:
            json_structure["destinataire"]["elements"]["name"]["text"] = get_line(28)
            
        if len(lines) > 30:
            json_structure["destinataire"]["elements"]["address"]["text"] = get_line(30)
            
        if len(lines) > 33:
            fr_dest = get_line(32)
            service_code = get_line(33)
            json_structure["destinataire"]["elements"]["service"]["text"] = f"{fr_dest}  {service_code}"
            
        if len(lines) > 34:
            json_structure["destinataire"]["elements"]["city"]["text"] = get_line(34)
        
        return json_structure
        
    except Exception:
        return None


def decode_qr(image_path):
    qr_data = decode_qr_from_image(image_path)
    if not qr_data:
        print("❌ Impossible de décoder le QR code.")
        return
    
    decoded_data = decode_base64_data(qr_data)
    if not decoded_data:
        print("❌ Impossible de décoder les données base64.")
        return
    
    final_result = decompress_gzip(decoded_data)
    if not final_result:
        print("❌ Impossible de décompresser les données.")
        return
    
    json_structure = parse_qr_to_json(final_result)
    if json_structure:
        return json.dumps(json_structure, indent=4, ensure_ascii=False)
    else:
        print("❌ Impossible de générer la structure JSON.")