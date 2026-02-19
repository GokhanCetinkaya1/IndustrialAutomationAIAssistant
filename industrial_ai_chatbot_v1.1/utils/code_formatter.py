import re

def format_code_output(code, language):
    """Kod çıktısını formatla ve güzelleştir"""
    # Markdown code block kontrolü
    if not code.strip().startswith("```"):
        code = f"```{language.lower()}\n{code}\n```"
    return code

def extract_code_blocks(text):
    """Metinden kod bloklarını çıkar"""
    pattern = r"```[\w]*\n(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    return matches

def validate_plc_code(code, language):
    """PLC kodu için basit validasyon"""
    validations = {
        "ST": ["PROGRAM", "VAR", "END_VAR", "END_PROGRAM"],
        "SCL": ["FUNCTION_BLOCK", "VAR_INPUT", "END_VAR"],
        "STL": ["FUNCTION", "BEGIN", "END_FUNCTION"]
    }
    
    keywords = validations.get(language, [])
    for keyword in keywords:
        if keyword not in code:
            return False, f"Eksik anahtar kelime: {keyword}"
    
    return True, "OK"

def validate_robot_code(code, robot_brand):
    """Robot kodu için basit validasyon"""
    validations = {
        "Fanuc": ["/PROG", "/MN", "/POS", "/END"],
        "ABB": ["MODULE", "PROC", "ENDPROC", "ENDMODULE"],
        "KUKA": ["DEF", "END"]
    }
    
    keywords = validations.get(robot_brand, [])
    for keyword in keywords:
        if keyword not in code:
            return False, f"Eksik anahtar kelime: {keyword}"
    
    return True, "OK"

def add_line_numbers(code):
    """Koda satır numarası ekle"""
    lines = code.split('\n')
    numbered_lines = [f"{i+1:3d} | {line}" for i, line in enumerate(lines)]
    return '\n'.join(numbered_lines)

def get_syntax_hints(language):
    """Her dil için syntax ipuçları"""
    hints = {
        "ST": {
            "variables": "VAR ... END_VAR arasında tanımlayın",
            "conditions": "IF-THEN-ELSE veya CASE kullanın",
            "loops": "FOR, WHILE, REPEAT döngüleri kullanılabilir"
        },
        "SCL": {
            "variables": "VAR_INPUT, VAR_OUTPUT, VAR_TEMP kullanın",
            "blocks": "DB (Data Block) kullanımına dikkat edin",
            "references": "#temp, #static, DB.VAR formatında referans verin"
        },
        "STL": {
            "stack": "Stack mantığını (U, O, =) doğru uygulayın",
            "memory": "M, I, Q, DB adreslemesine dikkat edin",
            "timing": "S5T# formatında timer süreleri kullanın"
        },
        "Fanuc": {
            "positions": "P[n] formatında position register kullanın",
            "motion": "J (Joint), L (Linear), C (Circular) ayırımı yapın",
            "io": "DI[], DO[] formatında I/O kullanın"
        },
        "ABB": {
            "data": "robtarget, speeddata, zonedata tanımlayın",
            "motion": "MoveJ, MoveL, MoveC kullanın",
            "procedures": "PROC-ENDPROC yapısını kullanın"
        },
        "KUKA": {
            "positions": "E6POS, E6AXIS veri tiplerini kullanın",
            "motion": "PTP, LIN, CIRC komutlarını kullanın",
            "io": "$IN[], $OUT[] formatında I/O kullanın"
        }
    }
    return hints.get(language, {})
