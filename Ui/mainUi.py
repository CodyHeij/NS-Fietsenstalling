from tkinter import *

from Ui.Elements import userUi
from Ui.Elements import bikeUI


def main():
    master = Tk()
    userUi.registerUser(master)
    bikeUI.addBike(master)
    mainloop()

main()