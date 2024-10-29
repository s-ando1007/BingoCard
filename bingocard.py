import tkinter as tk
import random

class bingocard:
    def __init__(self, x):
        self.x = x
        self.x.title("ビンゴカード")

        self.y = set()
        self.z = self.a()
        self.o = 0
        self.g = set()

        self.b()

    def a(self):
        c = {
            0: range(1, 16),
            1: range(16,31),
            2: range(31, 46),
            3: range(46, 61),
            4: range(61, 76)
        }

        z = []
        for i in range(5):
            col_values = random.sample(c[i], 5)
            z.append(col_values)
        
        z[2][2] = "FREE"

        return z
    
    def b(self):
        self.u = []
        for r in range(5):
            row_buttons = []
            for c in range(5):
                v = self.z[c][r]
                btn = tk.Button(self.x, text = v, width = 5, height = 2, command = lambda x = r, y = c:self.e(x, y))
                btn.grid(row = r, column = c)
                row_buttons.append(btn)
            self.u.append(row_buttons)
    
    def e(self, r, c):
        if (r, c) in self.y:
            return
        
        self.y.add((r, c))
        self.u[r][c].config(bg = "lightgreen", text = "◯")
        self.d()

    def d(self):
        p = 0
        for r in range(5):
            if all((r, col) in self.y for col in range(5)) and ('row', r) not in self.g:
                p += 1
                self.g.add(('row', r))
        
        for c in range(5):
            if all((row, c) in self.y for row in range(5)) and ('col', c) not in self.g:
                p += 1
                self.g.add(('col', c))

        if all((i, i) in self.y for i in range(5)) and 'diag1' not in self.g:
            p += 1
            self.g.add('diag1')

        if all((i, 4 - i) in self.y for i in range(5)) and 'diag2' not in self.g:
            p += 1
            self.g.add('diag2')

        self.o += p

        if p > 0:
            if self.o == 1:
                print("ビンゴ!")
            elif self.o == 2:
                print("ダブルビンゴ!")
            elif self.o == 3:
                print("トリプルビンゴ!")
            elif self.o == 4:
                print("クアドラプルビンゴ!")
            else:
                print(f"{self.o}ビンゴ!")

if __name__ == "__main__":
    r = tk.Tk()
    app = bingocard(r)
    r.mainloop()        