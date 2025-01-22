from playwright.sync_api import sync_playwright
import os

# Função para capturar a tela
def capture_screenshot(url, save_path):
    with sync_playwright() as p:
        # Iniciar o navegador
        browser = p.chromium.launch(headless=True)  # True para não exibir o navegador
        page = browser.new_page()

        # Ir até a URL
        page.goto(url)

        # Tirar a captura de tela
        page.screenshot(path=save_path)
        print(f"Captura de tela tirada e salva em {save_path}")

        # Fechar o navegador
        browser.close()

# URL da página que você quer capturar
url = "https://www.google.com/search?sca_esv=115fbc7a5c2d88aa&sxsrf=ADLYWIKKax1Sll7oN-MxjrxTC-ibaVjJVA:1737579986449&q=fotos+de+pessoas&udm=2&fbs=AEQNm0A_ElqRadfJ052eEZYKSIj__pYFaFHKdnGcO42W-poa4hqiqoSrkT7Gbj0jEa1XXHcpOVXJg6GWUM39QIGoNHiolJF6R_HI7vN-ARaK4Agzx2OFtr8rBZ4dWs9BMuz70G1qAVFA6xk5cCJgFuifVKBmANe5ifBDoDvn4NvufxhzBuNkKEx_JpVLaef-3ibJK_qC3VUhpQG8qyyk_VWfRQevcXn7CA&sa=X&ved=2ahUKEwjCvvHunYqLAxXsIbkGHRMsLkcQtKgLegQIExAB&biw=1536&bih=791&dpr=1.25"

# Definir o caminho para salvar a captura de tela
save_path = "screenshots/webpageImage.png"

# Garantir que a pasta screenshots exista
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Capturar e salvar a captura de tela
capture_screenshot(url, save_path)

# Verificar se o arquivo foi salvo
if os.path.exists(save_path):
    print(f"Arquivo salvo com sucesso em {save_path}")
else:
    print(f"Erro: Arquivo não encontrado em {save_path}")