import random
import time
from tkinter import messagebox
from tkinter import *
import string

root = Tk()
root.geometry("1600x900+0+0")
root.title("  Cafe Management Systems  ")
root.configure(background='powder blue')

Tops = Frame(root, width=1350, height=100, bd=14,bg="powder blue", relief="flat")
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=650, bg="powder blue",bd=8, relief="flat")
f1.pack(side=LEFT)
f2 = Frame(root, width=440, height=650, bd=8, bg="powder blue",relief="flat")
f2.pack(side=RIGHT)

ft2 = Frame(f2, width=440, height=450, bd=14,bg="powder blue", relief="flat")
ft2.pack(side=TOP)
fb2 = Frame(f2, width=440, height=250, bd=14, bg="powder blue",relief="flat")
fb2.pack(side=BOTTOM)

f1a = Frame(f1, width=900, height=330, bd=14, bg="powder blue",relief="flat")
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=320, bd=14, bg="powder blue",relief="flat")
f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=330, bd=14,bg="powder blue", relief="flat")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=330, bd=16,bg="powder blue", relief="flat")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=450, height=330, bd=14,bg="powder blue", relief="flat")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330, bd=14,bg="powder blue", relief="flat") 
f2ab.pack(side=RIGHT)

Tops.configure(background='powder blue')
f1.configure(background='powder blue')
f2.configure(background='powder blue')
# ======================================CostofItem============================================
def CostofItem():
    Item1=float(E_Latta.get())
    Item2=float(E_Espresso.get())
    Item3=float(E_Iced_Latta.get())
    Item4=float(E_Vale_coffee.get())
    Item5=float(E_Cappuccino.get())
    Item6=float(E_African_Coffee.get())
    Item7=float(E_American_Coffee.get())
    Item8=float(E_Iced_Cappuccino.get())
    Item9=float(E_Coffee_Cake.get())
    Item10=float(E_Red_Velvet_cake.get())
    Item11=float(E_Black_Forest_Cake.get())
    Item12=float(E_Boston_Cream_Cake.get())
    Item13=float(E_Lagos_Chocolate_Cake.get())
    Item14=float(E_Kilburn_Chocolate_cake.get())
    Item15=float(E_Carlton_Hill_Chocolate_Cake.get())
    Item16=float(E_Queen_Park_Cake_Chocolate_Cake.get())


    PriceofDrinks=(Item1 * 1.2)+(Item2*1.99)+(Item3*2.05)+(Item4*1.99) +(Item5*1.99) +(Item6*2.99)+(Item7*2.39) +(Item8*1.29)

    PriceofCakes = (Item9 * 1.35 ) + (Item10 *2.2) + (Item11 * 1.99) + (Item12 * 1.49) +(Item13 * 1.8)
    + (Item14 * 1.67) + (Item15 * 1.6) + (Item16 + 1.99)

    DrinksPrice = "$", str('%.2f' % PriceofDrinks)
    CakesPrice = "$", str('%.2f' % PriceofCakes)
    CostofCakes.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)
    SC="$"+ str('%.2f'%1.59)
    ServiceCharge.set(SC)
    SubTotalofITEMS="$"+ str('%.2f'%(PriceofDrinks + PriceofCakes +1.59))
    SubTotal.set(SubTotalofITEMS)

    Tax="$"+ str('%.2f'%((PriceofDrinks + PriceofCakes + 1.59)*0.15))
    PaidTax.set(Tax)
    TT=((PriceofDrinks + PriceofCakes + 1.59)*0.15)
    TC="$"+ str('%.2f'%(PriceofDrinks + PriceofCakes + 1.59 + TT))
    TotalCost.set(TC)

#=======================================Functions=========================================
def qExit():
    qExit = messagebox.askyesno("Quit System","Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return

def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCakes.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0", END)

    E_Latta.set("0")
    E_Espresso.set("0")
    E_Iced_Latta.set("0")
    E_Vale_coffee.set("0")
    E_Cappuccino.set("0")
    E_African_Coffee.set("0")
    E_American_Coffee.set("0")
    E_Iced_Cappuccino.set("0")

    E_Coffee_Cake.set("0")
    E_Red_Velvet_cake.set("0")
    E_Black_Forest_Cake.set("0")
    E_Boston_Cream_Cake.set("0")
    E_Lagos_Chocolate_Cake.set("0")
    E_Kilburn_Chocolate_cake.set("0")
    E_Carlton_Hill_Chocolate_Cake.set("0")
    E_Queen_Park_Cake_Chocolate_Cake.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtLatta.configure(state=DISABLED)
    txtEspresso.configure(state=DISABLED)
    txtIced_Latte.configure(state=DISABLED)
    txtVale_Coffee.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)
    txtAfrican_Coffee.configure(state=DISABLED)
    txtAmerican_Coffee.configure(state=DISABLED)
    txtIced_Cappuccino.configure(state=DISABLED)
    txtCoffee_Cake.configure(state=DISABLED)
    txtRed_Velvet_cake.configure(state=DISABLED)
    txtBlack_Forest_Cake.configure(state=DISABLED)
    txtBoston_Cream_Cake.configure(state=DISABLED)
    txtLagos_Chocolate_Cake.configure(state=DISABLED)
    txtKilburn_Chocolate.configure(state=DISABLED)
    txtCarlton_Hill_Cake.configure(state=DISABLED)
    txtQueen_Park_Cake.configure(state=DISABLED)
def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randRef = str(x)
    txtReceipt.insert(END, '\t\t\t\t\t\t\tReceipt Ref:\t' + Receipt_Ref.get() + '\t\t\t' + Dateoforder.get() + "\n")
    txtReceipt.insert(END, '\nItems\t\t' + "#Items " + "Price\t\n\n")
    #PriceofDrinks = (Item1 * 1.2) + (Item2 + 1.99) + (Item3 * 2.05) + (Item4 * 1.99) + (Item5 * 1.99) + (
    #            Item6 * 2.99) + (Item7 * 2.39) + (Item8 * 1.29)

    #PriceofCakes = (Item9 * 1.35) + (Item10 * 2.2) + (Item11 * 1.99) + (Item12 * 1.49) + (Item13 * 1.8)
   # + (Item14 * 1.67) + (Item15 * 1.6) + (Item16 + 1.99)
    with open('wk1.txt', 'a') as fo:
        if var1.get() == 1:
            x=' '
            v1 = (1.2 * float(E_Latta.get()))
            txtReceipt.insert(END,f'Latte\t\t{E_Latta.get()}' +f'\t{(1.2*float(E_Latta.get()))}$'+ "\n")
            fo.write('Latte\t\t'+str(E_Latta.get())+'\t'+str(v1)+'$'+ "\n")
        else:
            txtReceipt.delete("17.0")
        if var2.get() == 1:
            v2 = (1.99 * float(E_Espresso.get()))
            txtReceipt.insert(END, f'Espresso\t\t{E_Espresso.get()}' +f'\t{(1.99*float(E_Espresso.get()))}$'+ "\n")
            fo.write('Espresso\t' + str(E_Espresso.get()) + '\t' + str(v2) + '$' + "\n")
        else:
            txtReceipt.delete("17.0")
        if var3.get()==1:
            v3 = (2.05 * float(E_Iced_Latta.get()))
            txtReceipt.insert(END, f'Iced_Latte\t\t{E_Iced_Latta.get()}' +f'\t{(2.05*float(E_Iced_Latta.get()))}$'+ "\n")
            fo.write('Iced_Latte\t' + str(E_Iced_Latta.get()) + '\t' + str(v3) + '$' + "\n")
        else:
            txtReceipt.delete("17.0")
        if var4.get()==1:
            txtReceipt.insert(END, 'Vale_Coffee:  \t\t\t\t\t' + E_Vale_coffee.get() + "\n")
        else:
            txtReceipt.delete("17.0")
        if var5.get()==1:
            txtReceipt.insert(END, 'Cappuccino:  \t\t\t\t\t'+E_Cappuccino.get()+"\n")
        else:
            txtReceipt.delete("17.0")
        if var6.get()==1:
            txtReceipt.insert(END,  'African_Coffee:  \t\t\t\t\t'+E_African_Coffee.get()+"\n")
        else:
            txtReceipt.delete("17.0")
        if var7.get()==1:
            txtReceipt.insert(END,  'American_Coffee:  \t\t\t\t\t'+E_American_Coffee.get()+"\n")
        else:
            txtReceipt.delete("17.0")
    if var8.get()==1:
        txtReceipt.insert(END,  'Iced_Cappuccino:  \t\t\t\t\t'+E_Iced_Cappuccino.get()+"\n")
    else:
        txtReceipt.delete("17.0")
    if var9.get()==1:
        txtReceipt.insert(END,  'Coffee_Cake:  \t\t\t\t\t'+E_Coffee_Cake.get()+"\n")
    else:
        txtReceipt.delete("17.0")
    if var10.get()==1:
        txtReceipt.insert(END,  'Red_Velvet_cake:  \t\t\t\t\t'+E_Red_Velvet_cake.get()+"\n")
    else:
        txtReceipt.delete("1.0")
    if var11.get()==1:
        txtReceipt.insert(END,  'Black_Forest_Cake:  \t\t\t\t\t'+E_Black_Forest_Cake.get()+"\n")
    else:
        txtReceipt.delete("1.0")
    if var12.get()==1:
        txtReceipt.insert(END,  'Boston_Cream_Cake:  \t\t\t\t\t'+E_Boston_Cream_Cake.get()+"\n")
    else:
        txtReceipt.delete("1.0")
    if var13.get()==1:
        txtReceipt.insert(END,  'Lagos_Chocolate_Cake:  \t\t\t\t\t'+E_Lagos_Chocolate_Cake.get()+"\n")
    else:
        txtReceipt.delete("1.0")

    if var14.get()==1:
        txtReceipt.insert(END,  'Kilburn_Chocolate_cake:  \t\t\t\t\t'+E_Kilburn_Chocolate_cake.get()+"\n")
    else:
        txtReceipt.delete("1.0")
    if var15.get()==1:
        txtReceipt.insert(END,  'Carlton Hill Chocolate: \t\t\t\t\t'+E_Carlton_Hill_Chocolate_Cake.get()+"\n")
    else:
        txtReceipt.delete("1.0")

    if var16.get()==1:
        txtReceipt.insert(END, 'E_Queen_Park_Cake_Chocolate_Cake  \t\t\t\t\t' + E_Queen_Park_Cake_Chocolate_Cake.get()+"\n")
    else:
        txtReceipt.delete("1.0")

    txtReceipt.insert(END,"\n" 'Service Charge:\t' + ServiceCharge.get() + "\n")
    txtReceipt.insert(END,'Tax Paid:\t' + PaidTax.get() + "\n")
    txtReceipt.insert(END,'Total Cost:\t' + TotalCost.get() + "\n")
    #1.04.38 https://www.youtube.com/watch?v=wTg7rOq8-2Y&t=3510s
# =======================================================Heading===================================================================================
lblInfo = Label(Tops,font=('arial', 70, 'bold'),text="  Cafe Management Systems  ",bg="powder blue",bd=10,anchor='w')
lblInfo.grid(row=0, column=0)
# ======================================================Calculator===========================================================================
def chkbutton_value():
        if (var1.get()==1):
            txtLatta.configure(state=NORMAL)
        elif var1.get() == 0:
            txtLatta.configure(state=DISABLED)
            E_Latta.set("0")
        if (var2.get() == 1):
            txtEspresso.configure(state=NORMAL)
        elif var2.get() == 0:
            txtEspresso.configure(state=DISABLED)
            E_Espresso.set("0")
        if (var3.get() == 1):
            txtIced_Latte.configure(state=NORMAL)
        elif var3.get() == 0:
            txtIced_Latte.configure(state=DISABLED)
            E_Iced_Latta.set("0")
        if (var4.get() == 1):
            txtVale_Coffee.configure(state=NORMAL)
        elif var4.get() == 0:
            txtVale_Coffee.configure(state=DISABLED)
            E_Vale_coffee.set("0")
        if (var5.get() == 1):
            txtCappuccino.configure(state=NORMAL)
        elif var5.get() == 0:
            txtCappuccino.configure(state=DISABLED)
            E_Cappuccino.set("0")
        if (var6.get() == 1):
            txtAfrican_Coffee.configure(state=NORMAL)
        elif var6.get() == 0:
            txtAfrican_Coffee.configure(state=DISABLED)
            E_African_Coffee.set("0")
        if (var7.get() == 1):
            txtAmerican_Coffee.configure(state=NORMAL)
        elif var7.get() == 0:
            txtAmerican_Coffee.configure(state=DISABLED)
            E_American_Coffee.set("0")
        if (var8.get() == 1):
            txtIced_Cappuccino.configure(state=NORMAL)
        elif var8.get() == 0:
            txtIced_Cappuccino.configure(state=DISABLED)
            E_Iced_Cappuccino.set("0")
        if (var9.get() == 1):
            txtCoffee_Cake.configure(state=NORMAL)
        elif var9.get() == 0:
            txtCoffee_Cake.configure(state=DISABLED)
            E_Coffee_Cake.set("0")
        if (var10.get() == 1):
            txtRed_Velvet_cake.configure(state=NORMAL)
        elif var10.get() == 0:
            txtRed_Velvet_cake.configure(state=DISABLED)
            E_Red_Velvet_cake.set("0")
        if (var11.get() == 1):
            txtBlack_Forest_Cake.configure(state=NORMAL)
        elif var11.get() == 0:
            txtBlack_Forest_Cake.configure(state=DISABLED)
            E_Black_Forest_Cake.set("0")
        if (var12.get() == 1):
            txtBoston_Cream_Cake.configure(state=NORMAL)
        elif var12.get() == 0:
            txtBoston_Cream_Cake.configure(state=DISABLED)
            E_Boston_Cream_Cake.set("0")
        if (var13.get() == 1):
            txtLagos_Chocolate_Cake.configure(state=NORMAL)
        elif var13.get() == 0:
            txtLagos_Chocolate_Cake.configure(state=DISABLED)
            E_Lagos_Chocolate_Cake.set("0")
        if (var14.get() == 1):
            txtKilburn_Chocolate.configure(state=NORMAL)
        elif var14.get() == 0:
            txtKilburn_Chocolate.configure(state=DISABLED)
            E_Kilburn_Chocolate_cake.set("0")
        if (var15.get() == 1):
            txtCarlton_Hill_Cake.configure(state=NORMAL)
        elif var15.get() == 0:
            txtCarlton_Hill_Cake.configure(state=DISABLED)
            E_Carlton_Hill_Chocolate_Cake.set("0")
        if (var16.get() == 1):
            txtQueen_Park_Cake.configure(state=NORMAL)
        elif var16.get() == 0:
            txtQueen_Park_Cake.configure(state=DISABLED)
            E_Queen_Park_Cake_Chocolate_Cake.set("0")



# ===========================================================Variables=============================================

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
Dateoforder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()
E_Latta = StringVar()
E_Espresso = StringVar()
E_Iced_Latta = StringVar()
E_Vale_coffee = StringVar()
E_Cappuccino = StringVar()
E_African_Coffee = StringVar()
E_American_Coffee = StringVar()
E_Iced_Cappuccino = StringVar()
E_Coffee_Cake = StringVar()
E_Red_Velvet_cake = StringVar()
E_Black_Forest_Cake = StringVar()
E_Boston_Cream_Cake = StringVar()
E_Lagos_Chocolate_Cake = StringVar()
E_Kilburn_Chocolate_cake = StringVar()
E_Carlton_Hill_Chocolate_Cake = StringVar()
E_Queen_Park_Cake_Chocolate_Cake = StringVar()
E_Latta.set("0")
E_Espresso.set("0")
E_Iced_Latta.set("0")
E_Vale_coffee.set("0")
E_Cappuccino.set("0")
E_African_Coffee.set("0")
E_American_Coffee.set("0")
E_Iced_Cappuccino.set("0")
E_Coffee_Cake.set("0")
E_Red_Velvet_cake.set("0")
E_Black_Forest_Cake.set("0")
E_Boston_Cream_Cake.set("0")
E_Lagos_Chocolate_Cake.set("0")
E_Kilburn_Chocolate_cake.set("0")
E_Carlton_Hill_Chocolate_Cake.set("0")
E_Queen_Park_Cake_Chocolate_Cake.set("0")
Dateoforder.set(time.strftime("%d/%m/%Y"))
# =================================Drinks=========================================
Latta = Checkbutton(f1aa, text="Latte \t", variable=var1, onvalue=1, offvalue=0,
                    font=('arial', 18, 'bold'),bg="powder blue", command=chkbutton_value).grid(row=0, sticky=W)
Espresso = Checkbutton(f1aa, text="Espresso \t", variable=var2, bg="powder blue",onvalue=1, offvalue=0,
                    font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=1, sticky=W)
Iced_Latte = Checkbutton(f1aa, text="Iced_Latte \t", variable=var3, onvalue=1,bg="powder blue", offvalue=0,
                    font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=2, sticky=W)
Vale_coffee = Checkbutton(f1aa, text="Vale_coffee \t", variable=var4, onvalue=1,bg="powder blue", offvalue=0,
                    font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=3, sticky=W)
Cappuccino = Checkbutton(f1aa, text="Cappuccino \t", variable=var5, onvalue=1, bg="powder blue",offvalue=0,
                    font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=4, sticky=W)
African_Coffee = Checkbutton(f1aa, text="African_Coffee \t", variable=var6, onvalue=1,bg="powder blue", offvalue=0,
                    font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=5, sticky=W)
American_Coffee = Checkbutton(f1aa, text="American_Coffee \t", variable=var7, onvalue=1,bg="powder blue", offvalue=0,
                    font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=6, sticky=W)

Iced_Cappuccino = Checkbutton(f1aa, text="Iced_Cappuccino \t", variable=var8, onvalue=1, bg="powder blue",offvalue=0,
                    font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=7, sticky=W)
#=================================Cakes=========================================

CoffeeCake = Checkbutton(f1ab, text="CoffeeCake \t", variable=var9, onvalue=1, offvalue=0,bg="powder blue",
                    font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=0, sticky=W)
Red_Velvet_cake = Checkbutton(f1ab, text="Red Velvet cake \t", variable=var10, onvalue=1, offvalue=0,bg="powder blue",
                    font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=1, sticky=W)
Black_Forest_Cake = Checkbutton(f1ab, text="Black Forest Cake \t", variable=var11, onvalue=1, offvalue=0,bg="powder blue",
                    font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=2, sticky=W)
Boston_Cream_Cake = Checkbutton(f1ab, text="Boston Cream Cake \t", variable=var12, onvalue=1, offvalue=0,bg="powder blue",
                    font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=3, sticky=W)
Lagos_Chocolate_Cake = Checkbutton(f1ab, text="Lagos Chocolate Cake \t", variable=var13, onvalue=1, offvalue=0,bg="powder blue",
                    font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=4, sticky=W)
Kilburn_Chocolate = Checkbutton(f1ab, text="Kilburn Chocolate \t", variable=var14, onvalue=1, offvalue=0,bg="powder blue",
                    font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=5, sticky=W)
Carlton_Hill_Cake = Checkbutton(f1ab, text="Carlton Hill Cake \t", variable=var15, onvalue=1, offvalue=0,bg="powder blue",
                    font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=6, sticky=W)

Queen_Park_Cake = Checkbutton(f1ab, text="Queen Park Cake \t", variable=var16, onvalue=1, offvalue=0,bg="powder blue",
                    font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=7, sticky=W)

#=================================Enter Widget for Drinks==========================================================================

txtLatta = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=8, justify='left', textvariable=E_Latta, state=DISABLED)
txtLatta.grid(row=0, column=1)
txtEspresso = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=8, justify='left', textvariable=E_Espresso, state=DISABLED)
txtEspresso.grid(row=1, column=1)
txtIced_Latte = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=8, justify='left', textvariable=E_Iced_Latta ,state=DISABLED)
txtIced_Latte.grid(row=2, column=1)
txtVale_Coffee = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=8, justify='left', textvariable=E_Vale_coffee, state=DISABLED)
txtVale_Coffee.grid(row=3, column=1)

txtCappuccino = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=8, justify='left', textvariable=E_Cappuccino, state=DISABLED)
txtCappuccino.grid(row=4, column=1)
txtAfrican_Coffee = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=8, justify='left', textvariable=E_African_Coffee, state=DISABLED)
txtAfrican_Coffee.grid(row=5, column=1)
txtAmerican_Coffee = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=8, justify='left', textvariable=E_American_Coffee, state=DISABLED)
txtAmerican_Coffee.grid(row=6, column=1)
txtIced_Cappuccino = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=8, justify='left',textvariable=E_Iced_Cappuccino, state=DISABLED)
txtIced_Cappuccino.grid(row=7, column=1)

#=================================Enter Widget for forCakes===========================================================================
txtCoffee_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=8, justify='left',textvariable=E_Coffee_Cake, state=DISABLED)
txtCoffee_Cake.grid(row=0, column=1)
txtRed_Velvet_cake = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=8, justify='left',textvariable=E_Red_Velvet_cake, state=DISABLED)
txtRed_Velvet_cake.grid(row=1, column=1)
txtBlack_Forest_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=8, justify='left',textvariable=E_Black_Forest_Cake, state=DISABLED)
txtBlack_Forest_Cake.grid(row=2, column=1)
txtBoston_Cream_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=8, justify='left', textvariable=E_Boston_Cream_Cake, state=DISABLED)
txtBoston_Cream_Cake.grid(row=3, column=1)
txtLagos_Chocolate_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=8, justify='left',textvariable=E_Lagos_Chocolate_Cake, state=DISABLED)
txtLagos_Chocolate_Cake.grid(row=4, column=1)
txtKilburn_Chocolate = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=8, justify='left', textvariable=E_Kilburn_Chocolate_cake,state=DISABLED)
txtKilburn_Chocolate.grid(row=5, column=1)
txtCarlton_Hill_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=8, justify='left',textvariable=E_Carlton_Hill_Chocolate_Cake, state=DISABLED)
txtCarlton_Hill_Cake.grid(row=6, column=1)
txtQueen_Park_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=8, justify='left',textvariable=E_Queen_Park_Cake_Chocolate_Cake, state=DISABLED)
txtQueen_Park_Cake.grid(row=7, column=1)

#=================================Cost Items Information=========================================
lblCostofDrinks = Label(f2aa, font=('arial', 16, 'bold'), text="Cost of Drinks",bg="powder blue", bd=8)
lblCostofDrinks.grid(row=2, column=0, sticky=W)
txtCostofDrinks=Entry(f2aa, font=('arial', 16, 'bold'), bd=8, justify='left',bg="powder blue",textvariable=CostofDrinks)
txtCostofDrinks.grid(row=2, column=1)

lblCostofCakes = Label(f2aa, font=('arial', 16, 'bold'),bg="powder blue", text="Cost of Cakes", bd=8)
lblCostofCakes.grid(row=3, column=0, sticky=W)
txtCostofCakes = Entry(f2aa, font=('arial', 16, 'bold'), bd=8, justify='left',bg="powder blue",textvariable=CostofCakes)
txtCostofCakes.grid(row=3, column=1)

lblServiceCharge = Label(f2aa, font=('arial', 16, 'bold'), text="Service Charge",bg="powder blue", bd=8)
lblServiceCharge.grid(row=4, column=0)
txtServiceCharge = Entry(f2aa, font=('arial', 16, 'bold'), bd=8, justify='left',bg="powder blue", textvariable=ServiceCharge)
txtServiceCharge.grid(row=4, column=1)

#===============================Payment Information==============================
lblPaidTax = Label(f2ab, font=('arial', 16, 'bold'), text=" Paid Tax ",bg="powder blue", bd=8)
lblPaidTax.grid(row=2, column=0, sticky=W)
txtPaidTax=Entry(f2ab, font=('arial', 16, 'bold'), bd=8,insertwidth=2, justify='left', bg="powder blue",textvariable=PaidTax)
txtPaidTax.grid(row=2, column=1)

lblSubTotal = Label(f2ab, font=('arial', 16, 'bold'), text="Sub total",bg="powder blue", bd=8)
lblSubTotal.grid(row=3, column=0, sticky=W)
txtSubTotal=Entry(f2ab, font=('arial', 16, 'bold'), bd=8, insertwidth=2, justify='left',bg="powder blue", textvariable=SubTotal)
txtSubTotal.grid(row=3, column=1)

lblTotalCost= Label(f2ab, font=('arial', 16, 'bold'), text="Total Cost",bg="powder blue", bd=8)
lblTotalCost.grid(row=4, column=0, sticky=W)
txtTotalCost = Entry(f2ab,font=('arial', 16, 'bold'), bd=8, insertwidth=2, justify='left',bg="powder blue", textvariable=TotalCost)
txtTotalCost.grid(row=4, column=1)
#=================================================Information===========================================================
lblReceipt = Label(ft2, font=('arial', 12, 'bold'), text=" Receipt: ", bd=2, bg="powder blue",anchor='w')
lblReceipt.grid(row=0, column=0, sticky=W)
txtReceipt = Text(ft2,width=80, height=22,bg="powder blue",  bd=8, font=('arial', 11, 'bold'))
txtReceipt.grid(row=1, column=0)
#=================================Button=========================================

btnTotal = Button(fb2, padx=16, pady=1, bd=2, fg="black", font=('arial', 16, 'bold'), width=4, text="Total",bg="powder blue",command=CostofItem)
btnTotal.grid(row=0, column=0)


btnReceipt = Button(fb2, padx=16, pady=1, bd=2, fg="black", font=('arial', 16, 'bold'), width=4, bg="powder blue",text="Receipt",command=Receipt)
btnReceipt.grid(row=0, column=1)

btnReset = Button(fb2, padx=16, pady=1, bd=2, fg="black", font=('arial', 16, 'bold'),bg="powder blue", width=4, text="Reset", command=Reset)
btnReset.grid(row=0, column=2)

btnExit = Button(fb2, padx=16, pady=1, bd=2, fg="black",bg="powder blue", font=('arial', 16, 'bold'), width=4, text="Exit",command=qExit)
btnExit.grid(row=0, column=3)




root.mainloop()

