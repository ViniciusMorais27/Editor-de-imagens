
# Editor de Imagens com OpenCV e Tkinter

Este projeto é uma aplicação simples de edição de imagens desenvolvida em Python, utilizando as bibliotecas **OpenCV**, **Tkinter** e **Pillow**. A interface gráfica permite ao usuário carregar, manipular e salvar imagens com diversas funcionalidades, como conversão para escala de cinza, redimensionamento, aplicação de filtro gaussiano, detecção de bordas e rotação da imagem.

## Funcionalidades

- **Carregar Imagem**: Permite carregar uma imagem a partir de um diretório do sistema.
- **Converter para Cinza**: Converte a imagem carregada para escala de cinza.
- **Redimensionar Imagem**: Redimensiona a imagem para 300x300 pixels.
- **Filtro Gaussiano**: Aplica um filtro gaussiano para suavizar a imagem.
- **Detectar Bordas**: Aplica o detector de bordas Canny para realçar as bordas da imagem.
- **Rotacionar Imagem**: Rotaciona a imagem em 45 graus.
- **Redefinir Imagem**: Restaura a imagem original carregada.
- **Salvar Imagem**: Salva a imagem editada no formato JPEG, PNG ou BMP.

## Pré-requisitos

Certifique-se de ter instalado as seguintes bibliotecas antes de executar o código:

- [OpenCV](https://opencv.org/) (cv2)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (incluído na biblioteca padrão do Python)
- [Pillow](https://pillow.readthedocs.io/en/stable/)

Você pode instalar as bibliotecas necessárias com os seguintes comandos:

```bash
pip install opencv-python
pip install pillow
```

## Como usar

1. **Clonar o repositório ou baixar o código**:
   ```bash
   git clone https://github.com/ViniciusMorais27/Editor-de-imagens.git
   ```

2. **Executar o arquivo Python**:
   Navegue até o diretório do projeto e execute o script:

   ```bash
   python main.py
   ```

3. **Interagir com a interface gráfica**:
   - Clique em "Carregar Imagem" para selecionar uma imagem do seu sistema.
   - Utilize os botões disponíveis para editar a imagem conforme desejar.
   - Após realizar as alterações, clique em "Salvar Imagem" para salvar a imagem editada.

## Exemplo de Interface

A interface gráfica tem o seguinte layout:

- Exibe a imagem no centro da janela.
- Botões alinhados à esquerda permitem realizar as edições disponíveis.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE] para mais detalhes.

---

Desenvolvido por Vinicius Morais.
