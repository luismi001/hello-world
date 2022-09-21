from builtins import len
from tkinter import filedialog
from tkinter import *
import pandas as pd
from tkinter import messagebox
import os
# i have found a wey to inv
def price_list():

    ######### Parts Pice File
    check_digit = 20  # position 20
    ######### SUPERSESSION CHECK DIGIT
    replaced_check_digit = 20  # position 20 replaced part
    replacing_check_digit = 41  # position 41 replacing part

    # filename = filedialog.askopenfilename(title='PRICE FILE VOLVO USA RTLPRICE')
    # print(filename)
    dir_path = filedialog.askdirectory(title="SELECT VOLVO FOLDER")
    # print(dir_path)
    file_list = os.listdir(dir_path)
    dir_path = dir_path + "\\"
    # print(dir_list)
    for filename in file_list:
        ############PARTS LIST
        parts_list = []
        #########SUPERSESSION LIST
        rpl_list = []
        if 'RTLPRICE' in filename:
            print("price file:         ", filename)
            with open(dir_path + filename, "r") as f:
                data_list = f.readlines()
            for row in data_list:
                new_row = row[0:check_digit] + ' ' + row[check_digit + 1:]
                # print(new_row)
                parts_list.append(new_row)
            if '_CA_' in filename:
                with open("Volvo_CA_RTLPRICE_UPD.txt", "w") as new_file:
                    new_file.writelines(parts_list)
                messagebox.showinfo("FILE STAUS FOR CAN", "PARTS PRICE FILE EXTRACTION SUCCESSFULL")
            else:
                with open("Volvo_US_RTLPRICE_UPD.txt", "w") as new_file:
                    new_file.writelines(parts_list)
                messagebox.showinfo("FILE STAUS FOR USA", "PARTS PRICE FILE EXTRACTION SUCCESSFULL")

        if 'RTLREPLPRICE' in filename:
            print("supersession: ", filename)
            with open(dir_path + filename, "r") as f:
                data_list = f.readlines()
            for row in data_list:
                new_row = row[0:replaced_check_digit] + ' ' + \
                          row[replaced_check_digit + 1:replacing_check_digit] + ' ' + \
                          row[replacing_check_digit + 1:]
                rpl_list.append(new_row)
            if '_CA_' in filename:
                with open("Volvo_CA_RTLREPLPRICE_UPD.txt", "w") as new_file:
                    new_file.writelines(rpl_list)
                messagebox.showinfo("FILE STAUS FOR CAN", "SUPERSESSION EXTRACTION SUCCESSFULL")
            else:
                with open("Volvo_US_RTLREPLPRICE_UPD.txt", "w") as new_file:
                    new_file.writelines(rpl_list)
                messagebox.showinfo("FILE STAUS FOR USA", "SUPERSESSION EXTRACTION SUCCESSFULL")
# def supersessions():
#     try:
#         filename_ss = filedialog.askopenfilename(title='SUPERSESSION FILE RTLREPLPRICE')
#         replaced_check_digit = 20  #position 20 replaced part
#         replacing_check_digit = 41 #position 41 replacing part
#         rpl_list = []
#         with open(filename_ss, "r") as f:
#             data_list = f.readlines()
#         for row in data_list:
#             new_row = row[0:replaced_check_digit] + ' ' +\
#                       row[replaced_check_digit + 1:replacing_check_digit] + ' ' +\
#                       row[replacing_check_digit + 1:]
#             rpl_list.append(new_row)
#         if '_CA_' in filename_ss:
#             with open("Volvo_CA_RTLREPLPRICE_UPD.txt", "w") as new_file:
#                 new_file.writelines(rpl_list)
#             messagebox.showinfo("FILE STAUS FOR CAN", "SUPERSESSION EXTRACTION SUCCESSFULL")
#         else:
#             with open("Volvo_US_RTLREPLPRICE_UPD.txt", "w") as new_file:
#                 new_file.writelines(rpl_list)
#             messagebox.showinfo("FILE STAUS FOR USA", "SUPERSESSION EXTRACTION SUCCESSFULL")
#
#     except Exception as e:
#         messagebox.showinfo("Error: ", "Wrong file")
#         print("Error: ", e)

def main():
    root = Tk()
    root.title("VOLVO")
    root.geometry('300x200')
    # Create a Buttons
    Button_price_list = Button(root, text="SELECT VOLVO FOLDER", command=price_list, pady=20)
    #Button_supersession = Button(root, text="Supersessions File", command=supersessions, pady=20)
    # Set the position of buttons
    Button_price_list.pack(side=TOP)
    # Button_supersession.pack(side=BOTTOM)
    root.mainloop()

if __name__ == "__main__":
    main()
