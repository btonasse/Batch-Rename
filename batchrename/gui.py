from tkinter import Tk, Frame, ttk, StringVar, messagebox, Menu

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

class MainWindow(Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # Widgets
        self.path_lbl = ttk.Label(self, text='Hello!')

        self.show_widgets()

    def show_widgets(self) -> None:
        self.path_lbl.pack()

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

if __name__ == '__main__':
    app = App()
    app.run()