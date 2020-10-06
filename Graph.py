from tkinter import *
from sympy import *
import numpy as np 
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from io import BytesIO
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
# plt.style.use("dark_background")

class Derivative():
	def __init__(self,root):
		self.root=root
		self.root.geometry("1920x1080")
		self.root.title("Derivative")
		self.root.config(bg="White")
		Label(self.root,text="Derivative",bg="BLACK",fg="White",font=("Arial",20,"bold")).pack(fill=X)
		f1=LabelFrame(self.root)
		f1.place(x=0,y=50,relwidth=1)
		self.f1=f1

		def getfromhere():
			Label1=Label(f1,text="$"+myinput.get()+"$")
			Label1.place(x=10,y=100)
		def plot():
			fig0=Figure()
			fig0.clf()
			x=Symbol("X")

			nums=np.linspace(-2,2)
			exp=eval(myinput.get())
			diffo=diff(exp)
			f=lambdify(x,exp,"numpy")
			f1=lambdify(x,diffo,"numpy")
		
			fig=Figure(figsize=(5,5),dpi=130)

			axe=fig.add_subplot(1,1,1)
			axe.spines["left"].set_position("center")
			axe.spines["bottom"].set_position("zero")
			axe.spines["top"].set_color("none")
			axe.spines["right"].set_color("none")
			axe.plot(1, 0, ">k", transform=axe.get_yaxis_transform(), clip_on=False)
			axe.plot(0, 1, "^k", transform=axe.get_xaxis_transform(), clip_on=False)

			axe.stem(nums,f(nums),"RED",label=f"${myinput.get()}$")
			# axe.plot(nums,f1(nums),"Blue")
			# plt.title("Rate Of Change")
			# plt.legend()
			# plt.show()
			canvas = FigureCanvasTkAgg(fig,master=self.root)   
			canvas.draw()
			canvas.get_tk_widget().pack(side=TOP,fill=BOTH,pady=200,expand=True)
			self.fig=fig

		def clear():
			self.fig.clf()
			self.f1.pack_forget()

		 

		Label(f1,text="Enter Your Function Here",font=("Arial",15,"bold")).grid(row=0,column=0)
		myinput=Entry(f1,font=("Arial",25),width=30)
		myinput.grid(row=1,column=0,padx=500)
		Button(f1,text="Derivative",font=("Arial",15),relief=GROOVE,command=plot).grid(row=2,column=0,padx=500,pady=10)
		clearb=Button(f1,text="Clear",font=("Arial",15),relief=GROOVE,command=clear)
		clearb.grid(row=3,column=0,padx=500,pady=10)
		f = BytesIO()
		preview(myinput.get(), viewer='BytesIO', outputbuffer=f)
		f.seek(0)
		img = Image.open(f)
		pimg = ImageTk.PhotoImage(img)
		lbl = Label(f1,image=pimg)
		lbl.grid(row=4,column=0)

		
	

root=Tk()
myapp=Derivative(root)
root.mainloop()