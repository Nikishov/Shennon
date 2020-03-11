import math
import collections
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import *
import pickle
id_3 = {}
class Coder:
    text = ''
    coded_text=''
    id_2 = {}
    def Coding(self):
        sum = 0.0
        arr = [] 
        for i in range(0, 32):
            arr.append(0)
        id_1 = {
        'а':[arr[0],0,0.0,''],
        'б':[arr[1],0,0.0,''],
        'в':[arr[2],0,0.0,''],
        'г':[arr[3],0,0.0,''],
        'д':[arr[4],0,0.0,''],
        'е':[arr[5],0,0.0,''],
        'ж':[arr[6],0,0.0,''],
        'з':[arr[7],0,0.0,''],
        'и':[arr[8],0,0.0,''],
        'й':[arr[9],0,0.0,''],
        'к':[arr[10],0,0.0,''],
        'л':[arr[11],0,0.0,''],
        'м':[arr[12],0,0.0,''],
        'н':[arr[13],0,0.0,''],
        'о':[arr[14],0,0.0,''],
        'п':[arr[15],0,0.0,''],
        'р':[arr[16],0,0.0,''],
        'с':[arr[17],0,0.0,''],
        'т':[arr[18],0,0.0,''],
        'у':[arr[19],0,0.0,''],
        'ф':[arr[20],0,0.0,''],
        'х':[arr[21],0,0.0,''],
        'ц':[arr[22],0,0.0,''],
        'ч':[arr[23],0,0.0,''],
        'ш':[arr[24],0,0.0,''],
        'щ':[arr[25],0,0.0,''],
        'ъ':[arr[26],0,0.0,''],
        'ы':[arr[27],0,0.0,''],
        'ь':[arr[28],0,0.0,''],
        'э':[arr[29],0,0.0,''],
        'ю':[arr[30],0,0.0,''],
        'я':[arr[31],0,0.0,'']
        }

        t = text.get(1.0, 'end').lower()
        for t_mini in t:
            try:
                id_1[t_mini]
            except:
                pass
            else:
                self.text += t_mini

        for word_mini in self.text:
            try:
                id_1[word_mini][0] += 1
            except:
                pass

        def Translate(arg, l):
            num = ""
            for i in range(0,l):
                arg = arg * 2.0
                num += str(math.trunc(arg))
                if arg >= 1.0:
                    arg -= 1.0
            return num

        # for word_mini in self.text:
        #     id_1[word_mini][0] += 1

        for k in id_1.keys():
            if id_1[k][0] != 0.0:
                id_1[k][0] /= len(self.text)
                id_1[k][1] = math.ceil(math.log2(float(id_1[k][0]))*(-1))

        self.id_2.update(collections.OrderedDict(sorted(id_1.items(),key = lambda i:i[1][0],reverse=-1)))

        for k in self.id_2.keys():
            self.id_2[k][2] = sum
            sum += self.id_2[k][0]
            self.id_2[k][3] = Translate(self.id_2[k][2], self.id_2[k][1])
            

        for w in self.text:
            self.coded_text += self.id_2[w][3]
        text_code.insert(1.0, self.coded_text)
    

    def Decoding(self):
        string = ''
        for k,i in self.id_2.items():
            id_3[i[3]] = k
        temp = '00' + self.coded_text
        for i in temp:
            string += i
            try:
                id_3[string]
            except:
                pass
            else:
                text_code.insert('end', id_3[string])
                string = ''
        print(id_3)
def open_file():
    fl = fd.askopenfilename(filetypes=(('texts', '*.txt'), ('All files', '*.*')))
    with open(fl, 'r', encoding='utf-8') as f:
        text.delete(1.0, 'end')
        text.insert(1.0, f.read())
        
code = Coder()
def coding_file():
    code.Coding()
    
def save_file():
    new_file = fd.asksaveasfilename(filetypes=(('texts', '*.txt'), ('All files', '*.*')), defaultextension='.txt')
    temp_code = [int(code.coded_text[x:x+8],2) for x in range(0, len(code.coded_text), 8)]
    temp_bytes = bytes(temp_code)
    with open(new_file, 'wb') as f:
        f.write(temp_bytes)
    new_file = fd.asksaveasfilename(filetypes=(('texts', '*.txt'), ('All files', '*.*')), defaultextension='.txt')
    with open(new_file, 'wb') as f:
        pickle.dump(code.id_2, f)


def decode_file():
    text.delete(1.0, 'end')
    file_name = fd.askopenfilename(filetypes=(('texts', '*.txt'), ('All files', '*.*')))
    with open(file_name, 'rb') as f:
        temp_int = int.from_bytes(f.read(), byteorder='big')
        code.coded_text = "{0:b}".format(temp_int)
    file_name = fd.askopenfilename(filetypes=(('texts', '*.txt'), ('All files', '*.*')))
    with open(file_name, 'rb') as f:
        code.id_2 = pickle.load(f)
    text_code.delete(1.0, 'end')
    code.Decoding()

root = tk.Tk()
form = tk
root.wm_title("Алгорим Шеннона")
root.wm_resizable(width=True, height=True)
text = tk.Text(width=25, height=5, bg="darkgreen", fg='white', wrap=WORD)
text.grid(row = 0)
text_code = tk.Text(width=25, height=5, bg='lightblue', fg='black', wrap=WORD)
text_code.grid(column=2, row=0)
button_open = tk.Button(root,text='Открыть', height=3, width=20, command=open_file)
button_open.grid(row = 3)
button_code = tk.Button(root, text='Кодировать', height=3, width=20, command=coding_file)
button_code.grid(row = 3, column = 2)
button_save = tk.Button(root, text='Сохранить', height=3, width=20, command=save_file)
button_save.grid(row = 5, column = 1)
button_decode = tk.Button(root, text='Декодировать', height=3, width=20, command=decode_file)
button_decode.grid(row = 7, column = 1)
root.mainloop()
