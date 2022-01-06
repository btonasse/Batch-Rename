import tkinter as tk
from tkinter import Tk, ttk
import better_widgets
from better_widgets.widgets import FileDialogButton, myEntry

class App(better_widgets.App):
    '''Main GUI. Subclass of Tk'''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.minsize(300, 0)

        self.mainframe = MainWindow(self)
        self.mainframe.pack()
    
class MainWindow(tk.Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # Widgets
        self.path_lbl = ttk.Label(self, text='Folder')
        self.path_entry = myEntry(self)
        self.select_btn = FileDialogButton(self, self.path_entry, 'directory', text='...', command=lambda : self.master.test_callback('select_btn'))

        self.ext_lbl = ttk.Label(self, text='Extension')
        self.path_combo = ttk.Combobox(self)

        self.rename_btn = ttk.Button(self, text='Rename', command=lambda : self.master.test_callback('rename_btn'))
        self.close_btn = ttk.Button(self, text='Close', command=lambda : self.master.test_callback('close_btn'))
        
        self.show_widgets()       

    def show_widgets(self) -> None:
        self.path_lbl.pack()
        self.path_entry.pack()
        self.select_btn.pack()
        self.ext_lbl.pack()
        self.path_combo.pack()
        self.rename_btn.pack()
        self.close_btn.pack()
        self.master.update_screen_min_size()

if __name__ == '__main__':
    app = App("Batch Rename", None, True, None)
    app.run()