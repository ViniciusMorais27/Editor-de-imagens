import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Função para carregar a imagem
def carregar_imagem():
    global img, img_original
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if caminho_arquivo:
        img = cv2.imread(caminho_arquivo)
        img_original = img.copy()  # Manter cópia da imagem original
        exibir_imagem(img)

# Função para exibir a imagem no rótulo
def exibir_imagem(imagem):
    imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    imagem_pil = Image.fromarray(imagem_rgb)
    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    lbl_imagem.config(image=imagem_tk)
    lbl_imagem.image = imagem_tk

# Função para aplicar conversão para escala de cinza
def converter_para_cinza():
    global img
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # Convertendo de volta para BGR para manter a compatibilidade
    exibir_imagem(img)

# Função para redimensionar a imagem
def redimensionar_imagem():
    global img
    img = cv2.resize(img, (300, 300))
    exibir_imagem(img)

# Função para aplicar filtro Gaussiano
def aplicar_filtro_gaussiano():
    global img
    img = cv2.GaussianBlur(img, (5, 5), 0)
    exibir_imagem(img)

# Função para detectar bordas
def detectar_bordas():
    global img
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img_gray, 100, 200)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # Convertendo de volta para BGR
    exibir_imagem(img)

# Função para aplicar rotação
def rotacionar_imagem():
    global img
    (h, w) = img.shape[:2]
    centro = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(centro, 45, 1.0)
    img = cv2.warpAffine(img, M, (w, h))
    exibir_imagem(img)

# Função para redefinir para a imagem original
def redefinir_imagem():
    global img
    img = img_original.copy()
    exibir_imagem(img)

# Função para salvar a imagem editada
def salvar_imagem():
    caminho_salvar = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("BMP files", "*.bmp")])
    if caminho_salvar:
        cv2.imwrite(caminho_salvar, img)
        messagebox.showinfo("Sucesso", "Imagem salva com sucesso!")

# Criando a interface gráfica (GUI) com Tkinter
janela = Tk()
janela.title("Editor de Imagens com OpenCV")
janela.geometry("600x500")

# Rótulo para exibir a imagem
lbl_imagem = Label(janela)
lbl_imagem.pack(pady=10)

# Botões para ações
btn_carregar = Button(janela, text="Carregar Imagem", command=carregar_imagem)
btn_carregar.pack(side=LEFT, padx=10, pady=10)

btn_cinza = Button(janela, text="Converter para Cinza", command=converter_para_cinza)
btn_cinza.pack(side=LEFT, padx=10, pady=10)

btn_redimensionar = Button(janela, text="Redimensionar", command=redimensionar_imagem)
btn_redimensionar.pack(side=LEFT, padx=10, pady=10)

btn_filtro = Button(janela, text="Filtro Gaussiano", command=aplicar_filtro_gaussiano)
btn_filtro.pack(side=LEFT, padx=10, pady=10)

btn_bordas = Button(janela, text="Detectar Bordas", command=detectar_bordas)
btn_bordas.pack(side=LEFT, padx=10, pady=10)

btn_rotacionar = Button(janela, text="Rotacionar", command=rotacionar_imagem)
btn_rotacionar.pack(side=LEFT, padx=10, pady=10)

btn_redefinir = Button(janela, text="Redefinir Imagem", command=redefinir_imagem)
btn_redefinir.pack(side=LEFT, padx=10, pady=10)

btn_salvar = Button(janela, text="Salvar Imagem", command=salvar_imagem)
btn_salvar.pack(side=LEFT, padx=10, pady=10)

# Inicializa a janela
janela.mainloop()