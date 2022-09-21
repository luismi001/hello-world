from builtins import len
from tkinter import filedialog
from tkinter import *
import pandas as pd
from tkinter import messagebox
import re


def format_priceFile(file_frame):
    #Harley CAN
    f = open(r"Harley-Canada.txt", "w+")
    counter_us = 0
    pattern = '\w'
    # print(file_frame)
    for row in file_frame:
        row = list(row)
        part_number = str(row[2])     #18
        description = str(row[3])     #30
        retail_price = str(row[4])    #11
        # print("part number ", part_number)
        # print("retail price ", retail_price)
        # print("description ", description)

        counter_us += 1
        int_prc = retail_price[:retail_price.index('.')]
        part_number = re.findall(pattern, part_number)
        part_number = ''.join(part_number)

        while len(part_number) < 101:
            part_number = part_number + ' '
        # while len(description) < 30:
        #     description = description + ' '
        while len(retail_price) < 8:
            retail_price = retail_price + ' '

        #filtering out invalid rows.
        if len(int_prc) > 6:
            part_number = retail_price = 'N/A'
        if '-' in retail_price:
            part_number = retail_price = 'N/A'
        # print(part_number)
        # print(retail_price)

        if (part_number != 'N/A') and (retail_price != 'N/A'):
            final_row = part_number + retail_price + '\n'
            f.write(final_row)
    print("price list")
    print('Output count', counter_us)
    msg1 = 'Output count for CAN: ' + str(counter_us)
    messagebox.showinfo("Price Files Results", msg1)

def price_list():

    try:
        print("")
        filename = filedialog.askopenfilename(title='Harley Canada PRICE FILE')
        df = pd.read_csv(filename)
        file_frame = df.values
        format_priceFile(file_frame)
    except Exception as e:
        s = str(e)
        print("Error:", s)

        if 'invalid continuation byte' in s:
            print("Reading the file............")
            try:
                # filename = filedialog.askopenfilename(title='Harley Canada PRICE FILE')
                df = pd.read_excel(filename)
                file_frame = df.values
                format_priceFile(file_frame)
            except Exception as e:
                print("Error:", e)
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
