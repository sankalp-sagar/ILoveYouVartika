import tkinter as tk
import time

root = tk.Tk()
root.title('Tinker Geometry Managers')

colors = ['black', 'red', 'orange', 'blue', 'green',
          'yellow', 'brown', 'gold']
          
def empty_textbox():
    textbox.delete("1.0", END)


label_one = tk.Label(text='Vartika I love you and help you to get past it\nif any darkness arises').pack()
label_one_black = tk.Label(root, bg=colors[0]).pack(fill=tk.X)


label_two = tk.Label(text='Vartika I love you just like this red colour of love').pack()
label_two_red = tk.Label(root, bg=colors[1]).pack(fill=tk.X)


label_three = tk.Label(text='Vartika I love you with all my energy').pack()
label_three_orange = tk.Label(root, bg=colors[2]).pack(fill=tk.X)


label_four = tk.Label(text='Vartika my love for you is clean just like the Oceans').pack()
label_four_blue = tk.Label(root, bg=colors[3]).pack(fill=tk.X)


label_five = tk.Label(text='Vartika I love you and want to see us in peace').pack()
label_five_blue = tk.Label(root, bg=colors[4]).pack(fill=tk.X)


label_six = tk.Label(text='Vartika I love you and want to live with you happily').pack()
label_six_yellow = tk.Label(root, bg=colors[5]).pack(fill=tk.X)


label_seven = tk.Label(text='Vartika I love you and want to make you feel safe').pack()
label_six_brown = tk.Label(root, bg=colors[6]).pack(fill=tk.X)

label_eight = tk.Label(text='Vartika I love you and you are pure GOLD to me').pack()
label_six_gold = tk.Label(root, bg=colors[7]).pack(fill=tk.X)


root.mainloop()