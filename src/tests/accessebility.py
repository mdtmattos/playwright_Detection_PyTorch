from playwright.sync_api import sync_playwright
import json
import torch
import numpy as np
from PIL import Image, ImageOps
import pytesseract
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Função para verificar acessibilidade
def check_accessibility(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        # Injetar axe-core para análise de acessibilidade
        axe_script = page.evaluate("""
            async () => {
                const response = await fetch('https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.4.2/axe.min.js');
                const scriptText = await response.text();
                eval(scriptText);
                return axe.run();
            }
        """)

        # Processar os resultados
        accessibility_issues = json.loads(json.dumps(axe_script))
        
        # Capturar screenshot da página
        screenshot = page.screenshot(full_page=True)
        browser.close()

        return accessibility_issues, screenshot

# Função para analisar o contraste
def analyze_contrast(image_bytes):
    # Abrir imagem com PIL
    image = Image.open(io.BytesIO(image_bytes))

    # Converter a imagem para escala de cinza
    grayscale_image = ImageOps.grayscale(image)
    image_array = np.array(grayscale_image)

    # Usar PyTorch para processar a imagem
    tensor_image = torch.tensor(image_array).float() / 255.0  # Normalizar a imagem

    # Calcular contraste (simples: diferença entre máximo e mínimo de intensidade)
    contrast = tensor_image.max() - tensor_image.min()
    print("📊 Analisando Contraste...")
    print(f"Contraste médio da imagem: {contrast:.2f}")

    # Sugestão: se o contraste é baixo
    if contrast < 0.5:
        print("⚠️ O contraste da imagem está baixo! Considere aumentar o contraste para melhorar a legibilidade.")
    else:
        print("✅ O contraste está adequado.")

# Função para analisar a legibilidade do texto
def analyze_text_legibility(image_bytes):
    # Usando PyTesseract para detectar texto na imagem
    image = Image.open(io.BytesIO(image_bytes))
    text = pytesseract.image_to_string(image)

    print("📊 Analisando Legibilidade do Texto...")

    # Verificar se o texto é suficientemente grande
    if len(text) > 0:
        print(f"Texto detectado: {text[:100]}...")  # Exibindo apenas os primeiros 100 caracteres
        print("✅ Texto legível detectado.")
    else:
        print("⚠️ Nenhum texto legível detectado na imagem!")

# Função para analisar cores (daltonismo)
def analyze_colors(image_bytes):
    print("📊 Analisando Cores Acessíveis...")

    # Carregar a imagem com PIL
    image = Image.open(io.BytesIO(image_bytes))
    image = image.convert("RGB")
    image_array = np.array(image)

    # Exemplo de verificação de cores (simples): detectar cores predominantes
    reds = np.sum(image_array[:, :, 0] > 200)
    greens = np.sum(image_array[:, :, 1] > 200)
    blues = np.sum(image_array[:, :, 2] > 200)

    if reds > 50000:
        print("⚠️ Possível problema com o uso excessivo de vermelho! Verifique para daltonismo.")
    if greens > 50000:
        print("⚠️ Possível problema com o uso excessivo de verde! Verifique para daltonismo.")
    if blues > 50000:
        print("⚠️ Possível problema com o uso excessivo de azul! Verifique para daltonismo.")

# URL para testar
url = "https://touchsource.com/"
issues, screenshot = check_accessibility(url)

# Exibir problemas de acessibilidade
for issue in issues['violations']:
    print(f"🔴 Problema: {issue['description']}")
    print(f"ℹ️ Impacto: {issue['impact']}")
    print(f"📌 Elementos afetados: {[el['html'] for el in issue['nodes']]}")
    print("-" * 50)

# Análise de contraste com PyTorch
analyze_contrast(screenshot)

# Análise de legibilidade
analyze_text_legibility(screenshot)

# Análise de cores (para daltonismo)
analyze_colors(screenshot)
