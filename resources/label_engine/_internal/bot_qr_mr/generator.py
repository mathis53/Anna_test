import io
import os 
from PIL import Image, ImageDraw, ImageFont
import json
from barcode import Code128
from barcode.writer import ImageWriter

def generate_barcode_to_buffer(code_a_encoder, hauteur_barres_px, largeur_module_px, dpi=300):
    largeur_module_mm = (largeur_module_px / dpi) * 25.4
    hauteur_barres_mm = (hauteur_barres_px / dpi) * 25.4

    options_writer = {
        'module_width': largeur_module_mm,
        'module_height': hauteur_barres_mm,
        'font_size': 0,
        'text_distance': 0,
        'quiet_zone': 0,
        'dpi': dpi,
        'write_text': False
    }

    try:
        code128_barcode = Code128(code_a_encoder, writer=ImageWriter())
        buffer = io.BytesIO()
        code128_barcode.write(buffer, options=options_writer)
        buffer.seek(0)
        
        return buffer

    except Exception as e:
        return None


def generate_from_json(json_data, template_path="template.png", output_path="label.png"):
    try:
        if isinstance(json_data, str):
            structured_data = json.loads(json_data)
        else:
            structured_data = json_data
            
        text_font_color = "black"
        
        img = Image.open(template_path)
        draw = ImageDraw.Draw(img)

        if structured_data:
            item_counter = 0
            for section_name, section_data in structured_data.items():
                section_font_size_raw = section_data.get("font-size")
                section_font_family = section_data.get("font-family")
                elements = section_data.get("elements")

                if not isinstance(elements, dict):
                    continue

                current_section_font = None
                section_font_size_int = 0
                current_font_path = ""

                if section_font_family and section_font_size_raw:
                    try:
                        section_font_size_float = float(section_font_size_raw)
                        if section_font_size_float > 0:
                            section_font_size_int = int(section_font_size_float)
                            current_font_path = section_font_family
                            if os.path.exists(current_font_path):
                                current_section_font = ImageFont.truetype(current_font_path, section_font_size_int)
                    except Exception:
                        pass

                for element_name, element_data in elements.items():
                    item_counter += 1
                    coords_data = element_data.get("coords")

                    if coords_data is None:
                        continue
                    
                    x_coord = coords_data.get("x")
                    y_coord = coords_data.get("y")

                    if x_coord is None or y_coord is None:
                        continue
                    
                    try:
                        current_position = (int(x_coord), int(y_coord))
                    except ValueError:
                        continue

                    barcode_value = element_data.get("barcode")
                    if barcode_value is not None:
                        barcode_height_px = element_data.get("barcode_height")
                        barcode_module_width_px = element_data.get("barcode_module_width")

                        if barcode_height_px is None or barcode_module_width_px is None:
                            continue
                        
                        try:
                            barcode_height_px = int(barcode_height_px)
                            barcode_module_width_px = int(barcode_module_width_px)
                            if barcode_height_px <= 0 or barcode_module_width_px <= 0:
                                continue
                        except ValueError:
                            continue

                        barcode_buffer = generate_barcode_to_buffer(
                            str(barcode_value),
                            barcode_height_px,
                            barcode_module_width_px
                        )

                        if barcode_buffer:
                            try:
                                barcode_img = Image.open(barcode_buffer)
                                img.paste(barcode_img, current_position)
                            except Exception:
                                pass
                            finally:
                                barcode_buffer.close()
                        continue

                    text_to_write = element_data.get("text")
                    if text_to_write is None:
                        continue
                        
                    if not section_font_family or not section_font_size_raw or not current_section_font:
                        continue

                    element_font_size_raw = element_data.get("font-size")
                    font_to_use = current_section_font
                    font_size_to_log = section_font_size_int

                    if element_font_size_raw is not None:
                        try:
                            element_font_size_float = float(element_font_size_raw)
                            if element_font_size_float > 0:
                                element_font_size_int = int(element_font_size_float)
                                if element_font_size_int != section_font_size_int:
                                    try:
                                        font_to_use = ImageFont.truetype(current_font_path, element_font_size_int)
                                        font_size_to_log = element_font_size_int
                                    except Exception:
                                        pass
                                else:
                                    font_size_to_log = element_font_size_int
                        except ValueError:
                            pass
                    
                    if font_to_use:
                        draw.text(current_position, text_to_write, fill=text_font_color, font=font_to_use)

        img.save(output_path)
        return True

    except Exception as e:
        print(f"Erreur lors de la génération: {e}")
        return False


def write_text_on_image(image_path, text_to_write, font_path, font_size, text_color, output_path, position):
    try:
        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, font_size)
        draw.text(position, text_to_write, fill=text_color, font=font)
        img.save(output_path)
    except Exception:
        pass
