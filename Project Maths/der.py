from Mathlibs import *

class Derivative():
	def __init__(self,root):
		self.root=root
		self.root.geometry("1920x1080")
		self.root.title("Project Math")
		self.root.config(bg="White")


	def HeaderLabel(self):
		
		Lab1=Label(self.root,text="Project Math",bg="BLACK",fg="White",font=("Arial",20,"bold"))
		Lab1.pack(fill=X)

		Lab2=Label(self.root,text="Math Engine",bg="BLACK",fg="White",
			font=("Arial",20,"bold"),border=5)
		Lab2.pack(pady=20)

		ft=IntVar()
		ft.set(30)

		lab3=Button(self.root,text="Font Size",bg="BLACK",fg="White",
		font=("Arial",10,"bold"),relief=GROOVE,border=5)
		lab3.place(x=1200,y=60)

		fntsize=Entry(self.root,text=ft,font=("Arial",10,"bold"),relief=SUNKEN,border=5)
		fntsize.place(x=1200,y=100)

		self.ft=ft

		


	def DerivativeFrame(self):
		x=emoji.emojize(":red_heart:")
		f1=LabelFrame(self.root,text=f"I Love Maths {x}",bg="WHITE",fg="black",
			font=("Arial",15,"bold"),relief=SUNKEN,border=5)
		f1.pack(fill=BOTH)

		f2=LabelFrame(self.root,bg="WHITE",fg="black",
			font=("Arial",15,"bold"),relief=SUNKEN,border=5)
		f2.pack(fill=BOTH,expand=True)

		f3=LabelFrame(f2,text="Function",width=300,height=480,bg="WHITE",fg="black",
			font=("Arial",15,"bold"),relief=GROOVE,border=7)
		f4=LabelFrame(f2,text="Derivative of Function",width=300,height=480,bg="WHITE",fg="black",
			font=("Arial",15,"bold"),relief=GROOVE,border=7)
		

		self.f1=f1
		self.f2=f2
		self.f3=f3
		self.f4=f4
		
		
	def EntryFrame(self):
		"""Label """
		lab3=Label(self.f1,text="Enter Your Function",fg="Black",
			font=("Arial",20,"bold"),bg="White")
		lab3.grid(row=0,column=0,pady=40)
		"""Label """

		inp=StringVar()
		res=StringVar()
		res.set("x")
		"""Entry Widget"""
		Myinput=Entry(self.f1,text=inp,font=("Arial",30,"bold"),relief=SUNKEN,border=5)
		Myinput.grid(row=0,column=1,padx=20)
		Myinput.focus()

		respectlab=Label(self.f1,text="With Respect",bg="White",font=("Arial",10,"bold"))
		respectlab.grid(row=0,column=4)

		respect=Entry(self.f1,text=res,font=("Arial",10,"bold"),relief=SUNKEN,border=5)
		respect.grid(row=0,column=5)

		
		self.inp=inp
		self.res=res
	def eceptclass(self):
		newlab=Label(self.f2,text="Please Check Your Function",bg="BLACK",fg="White",font=("Arial",60,"bold"))
		# newlab.pack(anchor="center",pady=150)
		self.newlab=newlab

	def ButtonFrame(self):

		def getdiff():
			self.newlab.pack_forget()
			self.f2.pack_forget()
			self.f3.pack_forget()
			self.f4.pack_forget()
			try:
				
				self.f2.pack(fill=BOTH,expand=True)
				lx=self.inp.get()
				fig0= plt.gca()
				plt.clf()

				# print(diff(self.inp.get()))
				a,b,c,p,q,r,d,e,f,g,h,i,j,k,l,m,n,o,s,t,u,v,w,y,z=symbols("a b c p q r d e f g h i j k l m n o s t u v w  y z")
				x=Symbol("X")
				y=Symbol("Y")
				z=Symbol("Z")

				func=latex(eval(self.inp.get()))

				plt.text(-0.1,0.6,fr"${func}$",fontsize=self.ft.get())

				""" Input Function"""   

				fig = plt.gca()                                                                 
				fig.axes.get_xaxis().set_visible(False)                                         
				fig.axes.get_yaxis().set_visible(False)  
				fig.axes.spines["left"].set_color("none")
				fig.axes.spines["right"].set_color("none")
				fig.axes.spines["top"].set_color("none")
				fig.axes.spines["bottom"].set_color("none")                                       
				plt.draw() #or savefig  
				plt.savefig("1.png")
				img = Image.open("1.png")
				img.mode = 'RGBA' 
				# img = img.resize((750, 590), Image.ANTIALIAS)
				print(img.size)
				pimg = ImageTk.PhotoImage(img)
				lbl = Label(self.f3,image=pimg)
				lbl.image=pimg
				lbl.grid(row=0,column=1)
				self.f3.pack(side=LEFT,fill=Y,expand=True)
				self.plt=plt
				plt.clf()

				"""Output Function"""

				symdiff=diff(eval(self.inp.get()),eval(self.res.get()))
				newfunc=latex(symdiff)

				plt.text(-0.1,0.6,fr"${newfunc}$",fontsize=self.ft.get())
	                                                                      
				fig1 = plt.gca()                                                                 
				fig1.axes.get_xaxis().set_visible(False)                                         
				fig1.axes.get_yaxis().set_visible(False)  
				fig1.axes.spines["left"].set_color("none")
				fig1.axes.spines["right"].set_color("none")
				fig1.axes.spines["top"].set_color("none")
				fig1.axes.spines["bottom"].set_color("none")                                       
		 
				plt.savefig("2.png")


				img1 = Image.open("2.png")
				img1.mode = 'RGBA' 
				# img = img.resize((1360, 500), Image.ANTIALIAS)
		

				pimgpic = ImageTk.PhotoImage(img1)
				lbl1 = Label(self.f4,image=pimgpic)
				lbl1.image=pimgpic
				lbl1.grid(row=0,column=1)
				self.f4.pack(side=RIGHT,fill=Y,expand=True)
			except:
				self.newlab.pack(anchor="center",pady=150)
				
		def clear():
			self.f2.pack_forget()
			self.f3.pack_forget()
			self.f4.pack_forget()
			self.newlab.pack_forget()
			self.plt.clf()
			self.plt.clf()
		mybutton=Button(self.f1,text="Derivative",font=("Arial",10,"bold"),relief=GROOVE,border=5,command=getdiff)
		mybutton.grid(row=0,column=2,padx=20)
		clearbutton=Button(self.f1,text="Clear",font=("Arial",10,"bold"),relief=GROOVE,border=5,command=clear)
		clearbutton.grid(row=0,column=3,padx=20)





# root=Tk()

# diffr=Derivative(root)
# diffr.HeaderLabel()
# diffr.DerivativeFrame()
# diffr.eceptclass()
# # diffr.InsideFrame()
# diffr.EntryFrame()
# diffr.ButtonFrame()

# root.mainloop()
