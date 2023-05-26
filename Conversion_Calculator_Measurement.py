from tkinter import *
from tkinter import ttk


def reset1():
    global entry
    entry.destroy()
    entry = Entry(tab1)
    entry.place(x=124, y=20)


def mmcm():
    global entry
    mm = float(entry.get())
    cm = mm/10
    print(cm)
    reset1()
    entry.insert(0, f"{cm}CM")


def mmdm():
    global entry
    mm = float(entry.get())
    dm = mm/100
    print(dm)
    reset1()
    entry.insert(0, f"{dm}DM")


def mmm():
    global entry
    mm = float(entry.get())
    m = mm/1000
    print(m)
    reset1()
    entry.insert(0, f"{m}M")


def mmdkm():
    global entry
    mm = float(entry.get())
    dkm = mm/10000
    print(dkm)
    reset1()
    entry.insert(0, f"{dkm}DKM")


def mmhm():
    global entry
    mm = float(entry.get())
    hm = mm/100000
    print(hm)
    reset1()
    entry.insert(0, f"{hm}HM")


def mmkm():
    global entry
    mm = float(entry.get())
    km = mm/1000000
    print(km)
    reset1()
    entry.insert(0, f"{km}KM")


def reset2():
    global entry
    entry.destroy()
    entry = Entry(tab2)
    entry.place(x=124, y=20)


def cmmm():
    global entry
    cm = float(entry.get())
    millim = cm * 10
    print(millim)
    reset2()
    entry.insert(0, f"{millim}MM")


def cmdm():
    global entry
    cm = float(entry.get())
    dm = cm/10
    print(dm)
    reset2()
    entry.insert(0, f"{dm}DM")


def cmm():
    global entry
    cm = float(entry.get())
    m = cm/100
    print(m)
    reset2()
    entry.insert(0, f"{m}M")


def cmdkm():
    global entry
    cm = float(entry.get())
    dkm = cm/1000
    print(dkm)
    reset2()
    entry.insert(0, f"{dkm}DKM")


def cmhm():
    global entry
    cm = float(entry.get())
    hm = cm/10000
    print(hm)
    reset2()
    entry.insert(0, f"{hm}HM")


def cmkm():
    global entry
    cm = float(entry.get())
    km = cm/100000
    print(km)
    reset2()
    entry.insert(0, f"{km}KM")


def reset3():
    global entry
    entry.destroy()
    entry = Entry(tab3)
    entry.place(x=124, y=20)


def dmmm():
    global entry
    dm = float(entry.get())
    millim = dm * 100
    print(millim)
    reset1()
    entry.insert(0, f"{millim}MM")


def dmcm():
    global entry
    dm = float(entry.get())
    cm = dm*10
    print(cm)
    reset3()
    entry.insert(0, f"{cm}CM")


def dmm():
    global entry
    dm = float(entry.get())
    m = dm/10
    print(m)
    reset3()
    entry.insert(0, f"{m}M")


def dmdkm():
    global entry
    dm = float(entry.get())
    dkm = dm/100
    print(dkm)
    reset3()
    entry.insert(0, f"{dkm}DKM")


def dmhm():
    global entry
    dm = float(entry.get())
    hm = dm/1000
    print(hm)
    reset3()
    entry.insert(0, f"{hm}HM")


def dmkm():
    global entry
    dm = float(entry.get())
    km = dm/10000
    print(km)
    reset3()
    entry.insert(0, f"{km}KM")


def reset4():
    global entry
    entry.destroy()
    entry = Entry(tab4)
    entry.place(x=124, y=20)


def mm():
    global entry
    m = float(entry.get())
    mm = m*1000
    print(mm)
    reset4()
    entry.insert(0, f"{mm}MM")


def mcm():
    global entry
    m = float(entry.get())
    cm = m*100
    print(cm)
    reset4()
    entry.insert(0, f"{cm}CM")


def mdm():
    global entry
    m = float(entry.get())
    dm = m/10
    print(m)
    reset4()
    entry.insert(0, f"{dm}DM")


def mdkm():
    global entry
    m = float(entry.get())
    dkm = m/10
    print(dkm)
    reset4()
    entry.insert(0, f"{dkm}DKM")


def mhm():
    global entry
    m = float(entry.get())
    hm = m/100
    print(hm)
    reset4()
    entry.insert(0, f"{hm}HM")


def mkm():
    global entry
    m = float(entry.get())
    km = m/1000
    print(km)
    reset4()
    entry.insert(0, f"{km}KM")


def reset5():
    global entry
    entry.destroy()
    entry = Entry(tab5)
    entry.place(x=124, y=20)


def dkmmm():
    global entry
    dkm = float(entry.get())
    mm = dkm*10000
    print(mm)
    reset5()
    entry.insert(0, f"{mm}MM")


def dkmdm():
    global entry
    dkm = float(entry.get())
    cm = dkm*1000
    print(cm)
    reset5()
    entry.insert(0, f"{cm}CM")


def dkmm():
    global entry
    dkm = float(entry.get())
    dm = dkm*100
    print(dm)
    reset5()
    entry.insert(0, f"{dm}DM")


def dkmdkm():
    global entry
    dkm = float(entry.get())
    m = dkm*10
    print(m)
    reset5()
    entry.insert(0, f"{m}M")


def dkmhm():
    global entry
    dkm = float(entry.get())
    hm = dkm/10
    print(hm)
    reset5()
    entry.insert(0, f"{hm}HM")


def dkmkm():
    global entry
    dkm = float(entry.get())
    km = dkm/100
    print(km)
    reset5()
    entry.insert(0, f"{km}KM")


def reset6():
    global entry
    entry.destroy()
    entry = Entry(tab6)
    entry.place(x=124, y=20)


def hmmm():
    global entry
    hm = float(entry.get())
    mm = hm*100000
    print(mm)
    reset6()
    entry.insert(0, f"{mm}MM")


def hmdm():
    global entry
    hm = float(entry.get())
    cm = hm*10000
    print(cm)
    reset6()
    entry.insert(0, f"{cm}CM")


def hmm():
    global entry
    hm = float(entry.get())
    dm = hm*1000
    print(dm)
    reset6()
    entry.insert(0, f"{dm}DM")


def hmdkm():
    global entry
    hm = float(entry.get())
    m = hm*100
    print(m)
    reset6()
    entry.insert(0, f"{m}M")


def hmhm():
    global entry
    hm = float(entry.get())
    dkm = hm/10
    print(dkm)
    reset6()
    entry.insert(0, f"{dkm}DKM")


def hmkm():
    global entry
    hm = float(entry.get())
    km = hm*10
    print(km)
    reset6()
    entry.insert(0, f"{km}KM")


def reset7():
    global entry
    entry.destroy()
    entry = Entry(tab7)
    entry.place(x=124, y=20)


def kmmm():
    global entry
    km = float(entry.get())
    mm = km*1000000
    print(mm)
    reset7()
    entry.insert(0, f"{mm}MM")


def kmdm():
    global entry
    mm = float(entry.get())
    dm = mm*100000
    print(dm)
    reset7()
    entry.insert(0, f"{dm}CM")


def kmm():
    global entry
    mm = float(entry.get())
    m = mm*10000
    print(m)
    reset7()
    entry.insert(0, f"{m}DM")


def kmdkm():
    global entry
    mm = float(entry.get())
    dkm = mm*1000
    print(dkm)
    reset7()
    entry.insert(0, f"{dkm}M")


def kmhm():
    global entry
    mm = float(entry.get())
    hm = mm*100
    print(hm)
    reset7()
    entry.insert(0, f"{hm}DKM")


def kmkm():
    global entry
    mm = float(entry.get())
    km = mm/10
    print(km)
    reset7()
    entry.insert(0, f"{km}HM")


window = Tk()
window.title("Conversion Calculator")
notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
notebook.add(tab1, text="MM")
notebook.pack(expand=True)
lbl = Label(tab1, text="", width=50, height=25)
lbl.pack(expand=True)
entry = Entry(tab1)
entry.place(x=124, y=20)
mmb = Button(tab1, text="Millimeters To Centimeters", command=mmcm, bg="black", fg="white")
mmb.place(x=107, y=60)
mmbd = Button(tab1, text="Millimeters To Decimeters", command=mmdm, bg="black", fg="white")
mmbd.place(x=109, y=100)
mmbm = Button(tab1, text="Millimeters To Meters", command=mmm, bg="black", fg="white")
mmbm.place(x=120, y=140)
mmbdk = Button(tab1, text="Millimeters To Dekameters", command=mmdkm, bg="black", fg="white")
mmbdk.place(x=109, y=180)
mmbh = Button(tab1, text="Millimeters To Hectometers", command=mmhm, bg="black", fg="white")
mmbh.place(x=107, y=220)
mmbd = Button(tab1, text="Millimeters To Kilometers", command=mmkm, bg="black", fg="white")
mmbd.place(x=112, y=260)


tab2 = Frame(notebook)
notebook.add(tab2, text="CM")
notebook.pack(expand=True)
lbl = Label(tab2, text="", width=50, height=25)
lbl.pack(expand=True)
entry = Entry(tab2)
entry.place(x=124, y=20)
cmb = Button(tab2, text="Centimeters To Millimeters", command=cmmm, bg="black", fg="white")
cmb.place(x=107, y=60)
cmbd = Button(tab2, text="Centimeters To Decimeters", command=cmdm, bg="black", fg="white")
cmbd.place(x=109, y=100)
cmbm = Button(tab2, text="Centimeters To Meters", command=cmm, bg="black", fg="white")
cmbm.place(x=120, y=140)
cmbdk = Button(tab2, text="Centimeters To Dekameters", command=cmdkm, bg="black", fg="white")
cmbdk.place(x=109, y=180)
cmbh = Button(tab2, text="Centimeters To Hectometers", command=cmhm, bg="black", fg="white")
cmbh.place(x=107, y=220)
cmbd = Button(tab2, text="Centimeters To Kilometers", command=cmkm, bg="black", fg="white")
cmbd.place(x=112, y=260)


tab3 = Frame(notebook)
notebook.add(tab3, text="DM")
notebook.pack(expand=True)
lbl = Label(tab3, text="", width=50, height=25)
lbl.pack(expand=True)
entry = Entry(tab3)
entry.place(x=124, y=20)
dmb = Button(tab3, text="Decimeters To Millimeters", command=dmmm, bg="black", fg="white")
dmb.place(x=109, y=60)
dmbd = Button(tab3, text="Decimeters To Centimeters", command=dmcm, bg="black", fg="white")
dmbd.place(x=109, y=100)
dmbm = Button(tab3, text="Decimeters To Meters", command=dmm, bg="black", fg="white")
dmbm.place(x=122, y=140)
dmbdk = Button(tab3, text="Decimeters To Dekameters", command=dmdkm, bg="black", fg="white")
dmbdk.place(x=111, y=180)
dmbh = Button(tab3, text="Decimeters To Hectometers", command=dmhm, bg="black", fg="white")
dmbh.place(x=109, y=220)
dmbd = Button(tab3, text="Decimeters To Kilometers", command=dmkm, bg="black", fg="white")
dmbd.place(x=115, y=260)


tab4 = Frame(notebook)
notebook.add(tab4, text="M")
notebook.pack(expand=True)
entry = Entry(tab4)
entry.place(x=124, y=20)
mb = Button(tab4, text="Meters To Millimeters", command=mm, bg="black", fg="white")
mb.place(x=120, y=60)
mbd = Button(tab4, text="Meters To Centimeters", command=mcm, bg="black", fg="white")
mbd.place(x=119, y=100)
mbm = Button(tab4, text="Meters To Decimeters", command=mdm, bg="black", fg="white")
mbm.place(x=123, y=140)
mbdk = Button(tab4, text="Meters To Dekameters", command=mdkm, bg="black", fg="white")
mbdk.place(x=119, y=180)
mbh = Button(tab4, text="Meters To Hectometers", command=mhm, bg="black", fg="white")
mbh.place(x=117, y=220)
mbd = Button(tab4, text="Meters To Kilometers", command=mkm, bg="black", fg="white")
mbd.place(x=122, y=260)


tab5 = Frame(notebook)
notebook.add(tab5, text="DKM")
notebook.pack(expand=True)
entry = Entry(tab5)
entry.place(x=124, y=20)
dkmb = Button(tab5, text="Dekameters To Millimeters", command=dkmmm, bg="black", fg="white")
dkmb.place(x=109, y=60)
dkmbd = Button(tab5, text="Dekameters To Centimeters", command=dkmdm, bg="black", fg="white")
dkmbd.place(x=111, y=100)
dkmbm = Button(tab5, text="Dekameters To Decimeters", command=dkmm, bg="black", fg="white")
dkmbm.place(x=113, y=140)
dkmbdk = Button(tab5, text="Dekameters To Meters", command=dkmdkm, bg="black", fg="white")
dkmbdk.place(x=120, y=180)
dkmbh = Button(tab5, text="Dekameters To Hectometers", command=dkmhm, bg="black", fg="white")
dkmbh.place(x=109, y=220)
dkmbd = Button(tab5, text="Dekameters To Kilometers", command=dkmkm, bg="black", fg="white")
dkmbd.place(x=114, y=260)


tab6 = Frame(notebook)
notebook.add(tab6, text="HM")
notebook.pack(expand=True)
entry = Entry(tab6)
entry.place(x=124, y=20)
hmb = Button(tab6, text="Hectometers To Millimeters", command=hmmm, bg="black", fg="white")
hmb.place(x=107, y=60)
hmbd = Button(tab6, text="Hectometers To Centimeters", command=hmdm, bg="black", fg="white")
hmbd.place(x=106, y=100)
hmbm = Button(tab6, text="Hectometers To Decimeters", command=hmm, bg="black", fg="white")
hmbm.place(x=112, y=140)
hmbdk = Button(tab6, text="Hectometers To Meters", command=hmdkm, bg="black", fg="white")
hmbdk.place(x=122, y=180)
hmbh = Button(tab6, text="Hectometers To Dekameters", command=hmhm, bg="black", fg="white")
hmbh.place(x=107, y=220)
hmbd = Button(tab6, text="Hectometers To Kilometers", command=hmkm, bg="black", fg="white")
hmbd.place(x=112, y=260)


tab7 = Frame(notebook)
notebook.add(tab7, text="KM")
notebook.pack(expand=True)
entry = Entry(tab7)
entry.place(x=124, y=20)
kmb = Button(tab7, text="Kilometers To Millimeters", command=kmmm, bg="black", fg="white")
kmb.place(x=107, y=60)
kmbd = Button(tab7, text="Kilometers To Centimeters", command=kmdm, bg="black", fg="white")
kmbd.place(x=106, y=100)
kmbm = Button(tab7, text="Kilometers To Decimeters", command=kmm, bg="black", fg="white")
kmbm.place(x=112, y=140)
kmbdk = Button(tab7, text="Kilometers To Meters", command=kmdkm, bg="black", fg="white")
kmbdk.place(x=122, y=180)
kmbh = Button(tab7, text="Kilometers To Dekameters", command=kmhm, bg="black", fg="white")
kmbh.place(x=115, y=220)
kmbd = Button(tab7, text="Kilometers To Hectometers", command=kmkm, bg="black", fg="white")
kmbd.place(x=112, y=260)
window.mainloop()
