import tkinter as tk
from tkinter import ttk
import better_widgets
from better_widgets.widgets import FileDialogButton, myEntry, myCombobox

class App(better_widgets.App):
    '''Main GUI. Subclass of Tk'''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.mainframe = MainWindow(self)
        self.mainframe.grid(row=0, column=0)

        self.update_screen_min_size()

class ExtSelection(myCombobox):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self['values'] = ('jpg', 'jpeg', 'png')
        self.bind('<<ComboboxSelected>>', self.callback)
        self.current(0)

        self.validation_command = self.register(self.validate)
        self.config(validate='all', validatecommand=(self.validation_command, '%P'))
    
    def callback(self, event) -> None:
        self.selection_clear()
        self.master.focus() # Remove ugly highlighting

    def validate(self, ext: str) -> bool:
        if ext.isalnum():
            return True
        return False
class MainWindow(tk.Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        #self.columnconfigure(0, weight=1)
        # Widgets
        self.path_lbl = ttk.Label(self, text='Folder')
        self.path_entry = myEntry(self, width=30)
        self.select_btn = FileDialogButton(self, entry=self.path_entry, typ='directory', text='...', command=lambda : self.master.test_callback('select_btn'), width=5)

        self.ext_lbl = ttk.Label(self, text='Extension')
        self.path_combo = ExtSelection(self, width=6)

        self.name_lbl = ttk.Label(self, text='New name')
        self.name_entry = myEntry(self, width=30)

        self.rename_btn = ttk.Button(self, text='Rename', command=lambda : self.master.test_callback('rename_btn'))
        self.close_btn = ttk.Button(self, text='Close', command=lambda : self.master.test_callback('close_btn'))
        
        self.show_widgets()       

    def show_widgets(self) -> None:
        self.path_lbl.grid(row=0, column=0, columnspan=3)
        self.path_entry.grid(row=1, column=0, columnspan=2)
        self.select_btn.grid(row=1, column=2, sticky='w')
        self.ext_lbl.grid(row=2, column=0, columnspan=3)
        self.path_combo.grid(row=3, column=0, columnspan=3)
        self.name_lbl.grid(row=4, column=0, columnspan=3)
        self.name_entry.grid(row=5, column=0, columnspan=3)
        self.rename_btn.grid(row=6, column=0, sticky='ew')
        self.close_btn.grid(row=6, column=1, columnspan=2, sticky='ew')

if __name__ == '__main__':
    app = App("Batch Rename", None, True, None)
    app.run()