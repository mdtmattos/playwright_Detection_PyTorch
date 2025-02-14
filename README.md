## playwright_Detection_PyTorch

Este projeto utiliza Playwright e Python para realizar alguns testes usando IA com PyTorch.

## 📝 Descrição dos Arquivos
- **.gitignore**: Define arquivos e diretórios a serem ignorados pelo Git.
- **README.md**: Documentação do projeto.
- **requirements.txt**: Lista de dependências do projeto.
- **src/**: Código-fonte principal do projeto.
- **tests/**: Diretório contendo os testes.
- **accessebility.py**: Código para testes de acessibilidade.
- **faceDetect.py**: Código para detecção de rostos.
- **personDetect.py**: Código para detecção de pessoas.
- **screenshots/**: Diretório para armazenar capturas de tela.
- **takeWebpageScreenshots.py**: Script para capturar capturas de tela de páginas web.

## Ativar o Ambiente Virtual
```bash
python -m venv venv
.\venv\Scripts\activate
```

## Install dependencies
pip install -r requirements.txt

## Scripts Disponíveis
# Capturar Screenshot de uma Página Web
O script takeWebpageScreenshots.py captura uma screenshot de uma página web especificada.

python src/tests/takeWebpageScreenshots.py

# Verificar Acessibilidade
O script accessebility.py verifica a acessibilidade de uma página web e realiza análises de contraste, legibilidade do texto e cores.

python src/tests/accessebility.py

# Detectar Pessoas em uma Imagem
O script personDetect.py detecta pessoas em uma imagem usando um modelo pré-treinado do PyTorch.

python src/tests/personDetect.py

# Detectar Rostos em uma Imagem
O script faceDetect.py detecta rostos em uma imagem usando a biblioteca facenet_pytorch.

python src/tests/faceDetect.py

# Dependências
As dependências do projeto estão listadas no arquivo requirements.txt:

playwright
torch
numpy
pillow
pytesseract
torchvision
facenet_pytorch

