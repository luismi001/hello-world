from builtins import len
from tkinter import filedialog
from tkinter import *
import pandas as pd
import time
import csv
from tkinter import messagebox
import re
import chardet
######Global variables
csv_date = time.strftime('%m%d%y')

def format_priceFile(file_frame):
    #ASTON MARTIN
    supplier_us = 'ASTON_MARTIN_US_'
    supplier_ca = 'ASTON_MARTIN_CA_'
    row_list_us = []
    row_list_ca = []
    ##write headers in the csv file
    csv_file_headers_us(supplier_us)
    csv_file_headers_ca(supplier_ca)

    for row in file_frame:
        row = list(row)
        country = row[6]
        del row[6:]
        # print(row)
        if country == 'US':
            row_list_us.append(row)
        if country == 'CA':
            row_list_ca.append(row)
    csv_file_writer_us(supplier_us, row_list_us)
    csv_file_writer_ca(supplier_ca, row_list_ca)

    messagebox.showinfo("FILE EXTRACTION STATUS", "SUCCESFULLY FORMATTED" + '\n' +
                        "" + '\n' +
                        "USA:" + str(len(row_list_us)) + '\n' +
                        "" + '\n' +
                        'CAN:' + str(len(row_list_ca)))

def price_list():
    global headers_list
    try:
        print("1ST TRY READING.............")
        filename = filedialog.askopenfilename(title='ASTON MARTIN')
        df = pd.read_csv(filename)
        headers_list = df.columns.values.tolist()

        headers_list.remove('Country of Origin')
        headers_list.remove('EU export commodity code')

        file_frame = df.values
        format_priceFile(file_frame)
    except Exception as e:
        print("Error:", e)
        s = str(e)

        if 'invalid continuation byte' in s:
            print("2ND TRY Reading the file............")
            try:
                # filename = filedialog.askopenfilename(title='Harley Canada PRICE FILE')
                df = pd.read_excel(filename)
                file_frame = df.values
                format_priceFile(file_frame)
            except Exception as e:
                print("Error:", e)
        if 'Permission denied' in s:
            messagebox.showinfo("WARNING!! PLEASE CLOSE YOUR EXCEL FILE", s)

def csv_file_headers_us(supplier_us):
    filename = supplier_us + time.strftime(csv_date) + '.csv'
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        #WRITE IN THE EXCEL SHEET
        writer.writerow(headers_list)

def csv_file_headers_ca(supplier_ca):
    filename = supplier_ca + time.strftime(csv_date) + '.csv'
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        #WRITE IN THE EXCEL SHEET
        writer.writerow(headers_list)

def csv_file_writer_us(supplier_us ,row):
    filename = supplier_us + time.strftime(csv_date) + '.csv'
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(row)

def csv_file_writer_ca(supplier_ca ,row):
    filename = supplier_ca + time.strftime(csv_date) + '.csv'
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(row)

def main():
    root = Tk()
    root.title("Select the file to format")
    root.geometry('300x200')
    # Create a Buttons
    Button_price_list = Button(root, text="Price List", command=price_list, pady=20, padx=40)
    # Set the position of buttons
    Button_price_list.pack(side=TOP)
    root.mainloop()

if __name__ == "__main__":
    main()
