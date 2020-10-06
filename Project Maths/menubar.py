from der import *

class Menubar(Derivative):
	def __init__(self,root):
		super().__init__(root)
		menu_bar=Menu(self.root)
		self.root.config(menu=menu_bar)

		File=Menu(menu_bar)
		menu_bar.add_cascade(label="File",menu=File)
		File.add_command(label="Exit",command=self.root.quit)
	

root=Tk()
"""------------- Class---------------- """
diffr=Derivative(root)
filemenu=Menubar(root)
"""--------------Class----------------- """

diffr.HeaderLabel()
diffr.DerivativeFrame()
diffr.eceptclass()
# diffr.InsideFrame()
diffr.EntryFrame()
diffr.ButtonFrame()

root.mainloop()