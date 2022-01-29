import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

price_drink = {"아메리카노": 4000, "라떼": 4500, "카푸치노": 5000, "모카": 5500}
image_drink = {"아메리카노": "Americano.jpg", "라떼": "Latte.jpg", "카푸치노": "Cappuccino.jpg", "모카": "Mocha.jpg"}
order_drink = {}
total_price = 0


def add_order(m):
    global order_drink, total_price
    if m not in price_drink:
        print("입력한 메뉴가 존재하지 않습니다.")
    this_price = price_drink.get(m)
    total_price += this_price

    if m in order_drink:
        order_drink[m] = order_drink.get(m) + 1
    else:
        order_drink[m] = 1
    print_order()
    print_price()


def del_order(m):
    global order_drink, total_price
    if m not in price_drink:
        print("입력한 메뉴가 존재하지 않습니다.")
    this_price = price_drink.get(m)
    
    if m in order_drink:
        if order_drink.get(m) > 1:
            order_drink[m] = order_drink.get(m) - 1
            total_price -= this_price
        else:
            del(order_drink[m])
            total_price -= this_price
    
    print_order()
    print_price()


def print_order():
    global order_drink

    tmp = ""
    price_tmp = 0
    for i in order_drink:
        price_tmp = price_drink[i] * order_drink.get(i)
        tmp = tmp + i + " X " + str(order_drink.get(i)) +  " = " + "{:,}".format(price_tmp)+"\n"

    text_1.delete('1.0', tk.END)
    text_1.insert(1.0, tmp)


def order_cancel():
    global total_price, order_drink
    if total_price:
        messagebox.showerror(title="취소", message="음료주문이 취소되었습니다")

    total_price = 0
    order_drink = {}
    print_price()
    print_order()
    

def order_end():
    global total_price, order_drink
    if total_price:
        messagebox.showinfo(title="확인", message="음료주문을 완료하였습니다.\n결제화면은 직접 만들어보세요")
    
    total_price = 0
    order_drink = {}
    print_price()
    print_order()    
    

def print_price():
    global total_price
    label_price.configure(text="{:,}".format(total_price)+" 원")


window = tk.Tk()
window.title("음료주문 프로그램")
window.geometry("620x500+500+300")
window.resizable(False, False)

frame1 = tk.Frame(window, width="600", height="10")
frame1.pack(fill="both")

frame2 = tk.Frame(window, width="600")
frame2.pack(fill="both", expand=True)

frame3 = tk.Frame(window, width="600", height="10")
frame3.pack(fill="both", expand=True)

btn_cancel = tk.Button(frame1, text="주문취소", padx="10", pady="10", command=order_cancel)
btn_cancel.grid(row=0, column=1, padx=10, pady=10)

btn_end = tk.Button(frame1, text="주문완료", padx="10", pady="10", command=order_end)
btn_end.grid(row=0, column=2, padx=10, pady=10)

label_price = tk.Label(frame1, text="0 원", width="20", padx=10, pady="10", fg="blue", font='Arial 15')
label_price.grid(row=0, column="3", padx="10", pady="10")

# 사진
photo1 = ImageTk.PhotoImage(Image.open(image_drink["아메리카노"]))
photo2 = ImageTk.PhotoImage(Image.open(image_drink["라떼"]))
photo3 = ImageTk.PhotoImage(Image.open(image_drink["카푸치노"]))
photo4 = ImageTk.PhotoImage(Image.open(image_drink["모카"]))

img1 = tk.Label(frame2, image=photo1)
img2 = tk.Label(frame2, image=photo2)
img3 = tk.Label(frame2, image=photo3)
img4 = tk.Label(frame2, image=photo4)
img1.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
img2.grid(row=0, column=2, padx=10, pady=10, columnspan=2)
img3.grid(row=0, column=4, padx=10, pady=10, columnspan=2)
img4.grid(row=0, column=6, padx=10, pady=10, columnspan=2)

# 버튼
btn_drink_1 = tk.Button(frame2, text="추가", padx="1", pady="1", width="5", command=lambda: add_order('아메리카노'))
btn_drink_1.grid(row=1, column=0, padx=10, pady=2, sticky='ew')
btn_drink_2 = tk.Button(frame2, text="삭제", padx="1", pady="1", width="5", command=lambda: del_order('아메리카노'))
btn_drink_2.grid(row=1, column=1, padx=10, pady=2, sticky='ew')

btn_drink_3 = tk.Button(frame2, text="추가", padx="1", pady="1", width="5", command=lambda: add_order('라떼'))
btn_drink_3.grid(row=1, column=2, padx=10, pady=2, sticky='ew')
btn_drink_4 = tk.Button(frame2, text="삭제", padx="1", pady="1", width="5", command=lambda: del_order('라떼'))
btn_drink_4.grid(row=1, column=3, padx=10, pady=2, sticky='ew')

btn_drink_5 = tk.Button(frame2, text="추가", padx="1", pady="1", width="5", command=lambda: add_order('카푸치노'))
btn_drink_5.grid(row=1, column=4, padx=10, pady=2, sticky='ew')
btn_drink_6 = tk.Button(frame2, text="삭제", padx="1", pady="1", width="5", command=lambda: del_order('카푸치노'))
btn_drink_6.grid(row=1, column=5, padx=10, pady=2, sticky='ew')

btn_drink_7 = tk.Button(frame2, text="추가", padx="1", pady="1", width="5", command=lambda: add_order('모카'))
btn_drink_7.grid(row=1, column=6, padx=10, pady=2, sticky='ew')
btn_drink_8 = tk.Button(frame2, text="삭제", padx="1", pady="1", width="5", command=lambda: del_order('모카'))
btn_drink_8.grid(row=1, column=7, padx=10, pady=2, sticky='ew')

# 주문 리스트
text_1 = tk.Text(frame3, height="10")
text_1.pack()

window.mainloop()