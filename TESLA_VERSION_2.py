from builtins import len
from tkinter import filedialog
from tkinter import *
import pandas as pd
from tkinter import messagebox

def format_rpl_file(file_ss_frame):
    row_counter = 0
    h = open(r"Tesla Supersessions.txt", "w+")
    # with open("Tesla Supersessions.txt", 'w', newline='', encoding='utf-8') as h:
    for row in file_ss_frame:
        row_counter += 1
        row = list(row)
        #set variables
        part_number = str(row[0])
        replacement = str(row[2])
        model = str(row[4]).replace("Roadster", "Roadste")
        reason_code = str(row[5])
        while len(part_number) < 12:
            part_number = part_number + ' '
        while len(replacement) < 12:
            replacement = replacement + ' '
        final_row = ''.join(part_number + ',' + replacement + ',' + model + ',' + reason_code + '\n')
        # print(final_row)
        h.write(final_row)
    print("Supersession File")
    print('Output Count', row_counter)
    msg = 'Output Count: ' + str(row_counter)
    messagebox.showinfo("Supersession File", msg)

def format_priceFile(file_frame):
    #Tesla USA
    f = open(r"Tesla USA.txt", "w+")
    # with open("Tesla USA.txt", 'w', newline='') as f:

    # #Tesla Canada
    g = open(r"Tesla Canada.txt", "w+")
    # with open("Tesla Canada.txt", 'w', newline='') as g:

    counter_us = 0
    counter_can = 0
    NA_field = "NA                  Z1    "
    for row in file_frame:
        row = list(row)
        part_number = str(row[0].replace('-', ''))
        try:
            retail_price = str(round(float(row[1]), 2))
        except:
            pass
        country = str(row[3])

        if "US" in country:
            counter_us += 1
            int_prc = retail_price[:retail_price.index('.')]

            while len(part_number) < 18:
                part_number = part_number + ' '
            # print(int_prc)
            while len(retail_price) < 11:
                retail_price = retail_price + ' '

            final_row = ''.join('002>' + part_number + NA_field + retail_price + '0.00' + '\n')
            if len(int_prc) < 6:
                f.write(final_row)

        elif "CA" in country:
            counter_can += 1
            int_prc = retail_price[:retail_price.index('.')]

            while len(part_number) < 18:
                part_number = part_number + ' '
            # print(int_prc)
            while len(retail_price) < 11:
                retail_price = retail_price + ' '

            final_row = ''.join('002>' + part_number + NA_field + retail_price + '0.00' + '\n')
            if len(int_prc) < 6:
                g.write(final_row)
    print("price lists")
    print('Output count for USA', counter_us)
    print('Output count for CAN', counter_can)

    msg1 = 'Output count for USA: ' + str(counter_us)
    msg2 = 'Output count for CAN: ' + str(counter_can)

    messagebox.showinfo("USA Price Files Results", msg1)
    messagebox.showinfo("CAN Price Files Results", msg2)

def price_list():
    try:
        filename = filedialog.askopenfilename(title='Select the PRICE file for Tesla')
        df = pd.read_csv(filename)
        file_frame = df.values
        format_priceFile(file_frame)
    except Exception as e:
        messagebox.showinfo("Error: ", "Wrong file")
        print("Error: ", e)

def supersessions():
    try:
        filename_ss = filedialog.askopenfilename(title='Select SUPERSESSION file for Tesla')
        ss = pd.read_csv(filename_ss)
        file_ss_frame = ss.values
        format_rpl_file(file_ss_frame)
    except Exception as e:
        messagebox.showinfo("Error: ", "Wrong file")
        print("Error: ", e)

def main():
    root = Tk()
    root.title("Select the file to format")
    root.geometry('300x200')
    # Create a Buttons
    Button_price_list = Button(root, text="Price List", command=price_list, pady=20)
    Button_supersession = Button(root, text="Supersessions File", command=supersessions, pady=20)
    # Set the position of buttons
    Button_price_list.pack(side=TOP)
    Button_supersession.pack(side=BOTTOM)
    root.mainloop()

if __name__ == "__main__":
    main()
