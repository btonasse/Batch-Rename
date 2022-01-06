import tkinter as tk
from tkinter import Tk, Frame, ttk, StringVar, messagebox, Menu, filedialog

class App(Tk):
    '''Main GUI. Subclass of Tk'''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.title('Batch Rename')
        #self.iconbitmap('todo')
        self.minsize(300, 0)
        self.resizable(False, False)

        self.mainframe = MainWindow(self)
        self.mainframe.pack()
    
    def run(self) -> None:
        self.mainloop()

    def test_callback(self, caller: tk.Widget, logger = None) -> None:
        """
        Debugging method to test widget action callbacks. Accepts a logger instance if you prefer to log the message instead of printing it.
        """
        if logger:
            try:
                logger.debug(f"Test callback called by {caller}")
            except AttributeError:
                print(f"Invalid logger passed to test callback method: {logger}")
        else:
            print(f"Test callback called by {caller}")

class MainWindow(Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # Widgets
        self.path_lbl = ttk.Label(self, text='Folder')
        self.path_entry = myEntry(self)
        self.select_btn = FileDialogButton(self, self.path_entry, 'directory', text='...', command=lambda : self.master.test_callback('select_btn'))

        self.ext_lbl = ttk.Label(self, text='Extension')
        self.path_combo = MyCombobox(self)

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

        self.master.update()

class MyCombobox(ttk.Combobox):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

class myEntry(ttk.Entry):
    '''
    Entry subclass that automatically creates a StringVar to track its contents if not specified.
    Set and get methods can be called directly on the class instance instead of the variable.
    '''
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__ (master=master, *args, **kwargs)
        self.master=master
        self.config(exportselection=0)
        self.value = None
        for kwarg, value in kwargs.items():
            if kwarg == 'textvariable':
                if not isinstance(value, StringVar):
                    raise ValueError(f'Textvariable must be StringVar')
                self.value = value
        if not self.value:
            self.value = StringVar()
            self.config(textvariable=self.value)
    def set(self, txt) -> None:
        self.value.set(txt)
    def get(self) -> None:
        return self.value.get()

class FileDialogButton(ttk.Button):
    """
    Button that opens a folder selection dialog.
    Has to be instantiated after an associated myEntry, where the path will be displayed. 
    Type is the type of file dialog to be opened. These are Tkinter's filedialog function names without the 'ask' prefix. Eg: directory or openfiles
    """
    def __init__(self, master, entry: myEntry, typ: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.master = master
        self.entry = entry
        self.config(command = self.callback)

        # Set appropriate filedialog function
        try:
            self.filedialog_function = getattr(filedialog, 'ask' + typ)
        except AttributeError as err:
            raise AttributeError("Valid values for 'typ' are the ask function names of Tkinter's filedialog module: openfilename, saveasfilename, directory etc.") from err

    def callback(self):
        """
        Opens the folder dialog
        """
        path = self.filedialog_function()
        self.entry.set(path)

if __name__ == '__main__':
    app = App()
    app.run()