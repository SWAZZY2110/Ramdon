#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 20:09:46 2022

@author: priyankadas
"""

from tkinter import *
import random

root = Tk()
root.title("Lists")
root.geometry("400x400")

random_list = Label(root)


def ramdon():
    items = ["Banana", "Muffin", "Apple", "Water", "Hat", "Hoodie", "Umbrella", "Oars", "Whale food", "Gun", "Cheese Toastie"]
    r = random.randint(1, 10)
    random_list["text"] = "Please take item " + str(items[r]) + " out of the bagging area"
btn = Button(root, text = "Give rise to the random numbers", command = ramdon)
btn.pack()
random_list.pack()
root.mainloop()

