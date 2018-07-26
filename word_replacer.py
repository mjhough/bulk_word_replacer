import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class WordReplacer(tk.Tk):
    def request_filename(self):
        return filedialog.askopenfilename(title='Choose a file')

    def read_file(self, filename):
        try:
            with open(filename, 'r') as f:
                return f.read()
        except IOError:
            messagebox.showerror('Error', 'There was an error loading the file')

    def replace_words(self, filedata, word_to_replace, word_replacement):
        return filedata.replace(word_to_replace, word_replacement)

    def write_output(self, filedata, new_filename):
        try:
            with open(new_filename, 'w') as f:
                f.write(filedata)
        except IOError:
            messagebox.showerror('Error', 'There was an error saving to the file')

    def request_savename(self):
        return filedialog.asksaveasfilename(title='Save new file')

    def load_file(self):
        self.filedata = self.read_file(self.request_filename())

    def save_file(self):
        replaced_filedata = self.replace_words(self.filedata, self.word_to_replace.get(), self.word_replacement.get())
        self.write_output(replaced_filedata, self.request_savename())
        messagebox.showinfo('Success!', 'Successfully replaced word(s)')

    def __init__(self):
        tk.Tk.__init__(self)

        self.winfo_toplevel().title("Word Replacer")

        tk.Label(self, text="Word to replace").grid(row=0)
        self.word_to_replace = tk.Entry(self)
        self.word_to_replace.grid(row=0, column=1)

        tk.Label(self, text="Replacement word").grid(row=1)
        self.word_replacement = tk.Entry(self)
        self.word_replacement.grid(row=1, column=1)

        tk.Button(self, text='Step 1: Load File', command=self.load_file).grid(row=3, column=1, pady=4)
        tk.Button(self, text='Step 2: Save New File', command=self.save_file).grid(row=4, column=1, pady=4)

wr = WordReplacer()
wr.mainloop()
