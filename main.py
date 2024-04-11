from tkinter import* 
from tkinter import messagebox
import requests
import urllib.parse
import json

# Función para obtener la URL
def validar_url(url):
  

  parsed_url = urllib.parse.urlparse(url)
  if parsed_url.scheme != "https":
    return True
  if "@" in parsed_url.hostname:
    return True
  
  # Listas negras y herramientas de análisis
  try:
    response = requests.get(url, timeout=5)
  except requests.exceptions.RequestException:
    return True
  if response.status_code != 200:
    return True
  if "text/html" not in response.headers["Content-Type"]:
    return True
  
  # Análisis del comportamiento
  if "location.href" in response.text:
    return True
  if "form action" in response.text:
    return True
  
  return False
  
def mostrar():
  url=entrada_url.get()
  if(validar_url(url)):
    messagebox.showinfo("Analisis", "La URL es: " + entrada_url.get() + " es malisiosa" )
  else:
    messagebox.showinfo("Analisis", "La URL es: " + entrada_url.get() + " no es malisiosa" )

# Función principal
def main():
  # Crea la ventana principal
  ventana = Tk()
  ventana.title("Verificar URL")
  ventana.geometry("300x150")
  ventana.config(bg="#6FCFEB")
  etiqueta_url = Label(ventana, text="Introduzca la URL:")
  etiqueta_url.pack()
  # Entrada para la URL
  global entrada_url
  entrada_url = Entry(ventana, width=200)
  entrada_url.pack() 
  
  etiqueta_url.pack()
  # Etiqueta informativa
  #etiqueta_info = Label(text=entrada_url, fg="black", font=("Arial", 12))
  #etiqueta_info.pack()

  # Botón para obtener la URL
  boton_url = Button(text="Validar URL", command=lambda: mostrar())
  boton_url.pack()

  # Bucle principal
  ventana.mainloop()

# Iniciar la aplicación
main()