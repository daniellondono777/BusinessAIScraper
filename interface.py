import betterInterface
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import curtis
import tkinter.font as font

root = Tk()
root.title(" OG Analytica Hussle Program")
root.geometry('400x200')
root.configure(bg='black')

def hussle_i():
    symbol = str(entry1.get().split(" ")[0])
    depth = int(entry1.get().split(" ")[1])

    app = betterInterface.TestApp(symbol, depth)
    app.mainloop()


    

entry1 = Entry(root, width = 20, borderwidth=5, relief="solid", highlightcolor="red")
entry1.pack()

def company_quarter_report_i():
    symbol = str(entry1.get().split(" ")[0])
    depth = int(entry1.get().split(" ")[1])
    curtis.Curtis(symbol).getCompanyQuarterReport(depth)
    entry1.delete('0','end')
    entry1.insert(0, 'Check Terminal')
    
    mainloop()

def company_anual_report_i():
    symbol = str(entry1.get().split(" ")[0])
    depth = int(entry1.get().split(" ")[1])
    curtis.Curtis(symbol).getCompanyAnualReport(depth)
    entry1.delete('0','end')
    entry1.insert(0, 'Check Terminal')
    
    mainloop()

def most_active_i():
    symbol = str(entry1.get().split(" ")[0])
    depth = int(entry1.get().split(" ")[1])
    curtis.Curtis(symbol).getMostActive()
    entry1.delete('0','end')
    entry1.insert(0, 'Check Terminal')
    
    mainloop()

def most_gainerz_i():
    symbol = str(entry1.get().split(" ")[0])
    depth = int(entry1.get().split(" ")[1])
    curtis.Curtis(symbol).getMostGainerz()
    entry1.delete('0','end')
    entry1.insert(0, 'Check Terminal')
    
    mainloop()


def most_losers_i():
    symbol = str(entry1.get().split(" ")[0])
    depth = int(entry1.get().split(" ")[1])
    curtis.Curtis(symbol).getMostLosers()
    entry1.delete('0','end')
    entry1.insert(0, 'Check Terminal')
    
    mainloop()

def market_performance_i():
    symbol = str(entry1.get().split(" ")[0])
    depth = int(entry1.get().split(" ")[1])
    curtis.Curtis(symbol).getHourlyMarketPerformance()
    entry1.delete('0','end')
    entry1.insert(0, 'Check Terminal')
    
    mainloop()





Button(root, text = "Perform Marshall-Hussle", command = hussle_i, width = 50, font = font.Font(family='Helvetica', weight='bold'),borderwidth=5, relief="solid", highlightcolor="red").pack()
Button(root, text = "Company Quarter Report", command = company_quarter_report_i, width = 50, font = font.Font(family='Helvetica', weight='bold'),borderwidth=5, relief="solid", highlightcolor="red").pack()
Button(root, text = "Company Anual Report", command = company_anual_report_i, width = 50, font = font.Font(family='Helvetica', weight='bold'),borderwidth=5, relief="solid", highlightcolor="red").pack()
Button(root, text = "Most Active Stocks", command = most_active_i, width = 50, font = font.Font(family='Helvetica', weight='bold'),borderwidth=5, relief="solid", highlightcolor="red").pack()
Button(root, text = "Most Gainer Stocks", command = most_gainerz_i, width = 50, font = font.Font(family='Helvetica', weight='bold'),borderwidth=5, relief="solid", highlightcolor="red").pack()
Button(root, text = "Most Loser Stocks", command = most_losers_i, width = 50, font = font.Font(family='Helvetica', weight='bold'),borderwidth=5, relief="solid", highlightcolor="red").pack()
Button(root, text = "Hourly Market Performance", command = most_losers_i, width = 50, font = font.Font(family='Helvetica', weight='bold'),borderwidth=5, relief="solid", highlightcolor="red").pack()






root.mainloop()
