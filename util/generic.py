from PIL import ImageTk, Image


def leerImagen(path,size):
    return ImageTk.PhotoImage(Image.open(path).resize(size,Image.ANTIALIAS))

def centrarVentana(ventana,ancho,largo):
    ancho=ventana.winfo_screenwidth()
    largo=ventana.winfo_screenheight()
    x=int((ancho/2)-(ancho/2))
    y=int((largo/2)-(largo/2))
    return ventana.geometry(f'{ancho}x{largo}+{x}+{y}')