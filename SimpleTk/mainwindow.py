'''
Created on 27 feb 2017

@author: Luca
'''

import tkinter as tk



class MainWindow(tk.Frame):
    '''
    classdocs
    ''' 
    def __init__(self, master=None):
        tk.Frame.__init__(self, master) 
        self.grid() 
        self.createWidgets()
        self.master.title('Finestra principale')
     
    
    
    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',command=self.quit)
        self.quitButton.grid()
        #self.quitButton.grid_location(30, 30)   