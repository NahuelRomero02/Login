import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from fromularios.master import masterPanel
##import util.generic as utl90

class app:
    def verificar(self):
        usu=self.usuario.get()
        psw=self.contraseña.get()
        if(usu=="root" and psw=="12345678"):
            self.ventana.destroy()
            masterPanel()
        else:
            messagebox.showerror(message="La contraseña no es correcta", title="Mensaje")
    
                

    def __init__(self) -> None:
        self.ventana=tk.Tk()
        self.ventana.title('Inicio sesion')
        self.ventana.geometry('')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=600,height=440)
        utl.centrarVentana(self.ventana,600,400)
        
        

        logo=utl.leerImagen("./Imagen/proyecto.jpg",(200,200))

        frameLogo=tk.Frame(self.ventana,bd=0,width=300,relief=tk.SOLID,padx=10,pady=10,bg='#3a7ff6')
        frameLogo.pack(side="left",expand=tk.NO,fill=tk.BOTH)
        label=tk.Label(frameLogo,image=logo,bg='#3a7ff6')
        label.place(x=0,y=0,relwidth=1,relheight=1)
        
        frameForm=tk.Frame(self.ventana,bd=0,relief=tk.SOLID,bg='#fcfcfc')
        frameForm.pack(side="right",expand=tk.YES,fill=tk.BOTH)

        frameFormTop=tk.Frame(frameForm,height=50,bd=0,relief=tk.SOLID,bg='black')
        frameFormTop.pack(side='top',fill=tk.X)
        title=tk.Label(frameFormTop,text="Inicio de sesion",font=('Times',30),fg="#666a88",bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)

        frameFromFill=tk.Frame(frameForm,height=50,bd=0,relief=tk.SOLID,bg='#fcfcfc')
        frameFromFill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        etiquetaUsuario=tk.Label(frameFromFill,text='Usuario',font=('Times',14),fg='#666a88',bg='#fcfcfc',anchor='w')
        etiquetaUsuario.pack(fill=tk.X,padx=20,pady=5)
        self.usuario=ttk.Entry(frameFromFill,font=('Times',14))
        self.usuario.pack(fill=tk.X,padx=20,pady=5)

        etiquetaPsw= tk.Label(frameFromFill,text='Contraseña',font=('Times',14),fg='#666a88',bg='#fcfcfc',anchor='w')
        etiquetaPsw.pack(fill=tk.X,padx=20,pady=5)
        self.contraseña=ttk.Entry(frameFromFill,font=('Times',14))
        self.contraseña.pack(fill=tk.X,padx=20,pady=5)
        self.contraseña.config(show="*")

        inicio=tk.Button(frameFromFill,text="Iniciar sesion",font=("Times",15,BOLD),bg="#3a7ff6",bd=0,fg="#fff",command=self.verificar)
        inicio.pack(fill=tk.X,padx=20,pady=20)
        inicio.bind("<Return>",(lambda event:self.verificar()))

#        registrarse=tk.Button(frameFromFill,text='Registrarse',font=("Times",15,BOLD),bg="#3a7ff6",bd=0,fg="#fff")
#        registrarse.pack(fill=tk.X,padx=20,pady=20)
#        registrarse.bind("<Return>",(lambda event:self.registrarse()))
    

        self.ventana.mainloop()