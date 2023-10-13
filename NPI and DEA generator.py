import random, os, time
import colorama
from colorama import Fore
from colored import Fore, Back, Style
import pyperclip
from colorama import (Fore as d, Back as bg, Style as ds)

os.system('cls')

print(f"\n\t\t{Style.bold}"+f'{d.CYAN}.{d.RESET} '*42+f'{d.CYAN}.{d.RESET}' + Fore.YELLOW + f'\n\t\t||\t      =============== NPI/DEA Number Generator ===============  \t   ||\n\t\t||\t        ===== maintained at ©github.com/eternal-dvij  =======              ||'+ "\n\t\t"+f'{d.CYAN}.{d.RESET} '*42+f'{d.CYAN}.{d.RESET}')


def gen_dea():
    flag = True
    while flag:
        name = input(Fore.YELLOW + f"\n\nEnter the last name of prescriber: {d.CYAN}")
        firstletteroflName = name[0]
        if firstletteroflName.isdigit():
            print("Invalid Name! Try again")
            flag = True
            
        else:
            dea = input( f"\n{d.YELLOW}Choose dea type {d.RED}\n\t\t1. B (Hospital/Clinic) \n\t\t2. F (Distributor) \n\t\t3. P (Narcotic Treatment Program) \n\t\t4. C (Practitioner i.e. a physician, dentist, veterinarian) \n\t\t\t\t{d.YELLOW}")
            # \n\t\t5. Enter your ow}n dea type
            registrant_type = ['B', 'F', 'P', 'C']
            option_list = ['1','2','3','4']
            dea_input_flag = True
            while dea_input_flag:
                if dea in option_list:
                    ind = option_list.index(dea)
                    dea = registrant_type[ind]
                    dea_input_flag = False
                # elif dea == "5":
                #     dea = input("Please enter the type here: ")
                #     dea_input_flag = False
                else:
                    print(f"\n{d.CYAN}===== Please choose from given options only! =====")
                    dea = input( f"\n{d.YELLOW}Choose dea type {d.RED}\n\t\t1. B (Hospital/Clinic) \n\t\t2. F (Distributor) \n\t\t3. P (Narcotic Treatment Program) \n\t\t4. C (Practitioner i.e. a physician, dentist, veterinarian) \n\t\t\t\t{d.YELLOW}")
                    dea_input_flag = True
            dea = dea+firstletteroflName.upper()
            s = []
            for i in range(2,8):
                t = random.randint(0,9)
                s.append(t)
            for i in range(len(s)):
                x = str(s[i])
                dea = dea+x
            even = []
            odd = []
            for i in range(len(s)):
                if i%2==0:
                    even.append(s[i])
                else:
                    odd.append(s[i])
            finalsum = sum(even)+(sum(odd)*2)
            dea = dea+str(finalsum%10)
            pyperclip.copy(dea)
            print(Fore.YELLOW + f"DEA number for {name} is : \n\t\t     ||{d.BLUE} {dea} {d.YELLOW}|| \n \t\t !! DEA number copied !!")
            flag = False


def gen_npi():
    npi9 = random.randint(100000000,999999999)
    alt_digits = str(npi9) [0:10:2]
    rem_digits = str(npi9)[1:10:2]
    double_alt_digits = []
    for j in alt_digits[::-1]:
        d_alt = int(j)*2
        double_alt_digits.append(d_alt)

    make_unit_d = []

    for i in double_alt_digits:
        if len(str(i))>1:
            
            make_unit_d.append(int(str(i)[0]))
            make_unit_d.append(int(str(i)[1]))
        else:
            make_unit_d.append(i)

    for r in rem_digits:
        make_unit_d.append(int(r))
    sum_d = sum(make_unit_d)
    sum_d += 24

    if sum_d%10 != 0:
        check_digit = 10-(sum_d%10)
    else:
        check_digit = 0

    npi = int(str(npi9)+str(check_digit))
    # print(npi)
    pyperclip.copy(npi)
    print(Fore.YELLOW + f'\n\t        {d.WHITE} :::::{bg.MAGENTA}{d.WHITE }  NPI number  {bg.RESET}:::::{d.RESET} \n\n\t\t{d.YELLOW}     ||{d.BLUE} {npi} {d.YELLOW}|| \n \t\t  !! NPI number copied !!\n')


# gen_dea()  

def wrap_generators():
    s_input = input(f'\n{ds.BRIGHT}{d.YELLOW}Please Select one of the following options: \n\t\t\t 1. Generate DEA number \n\t\t\t 2. Generate NPI \n\t\t\t\t{d.RED}')
    s_input_flag = True
    while s_input_flag:
        if s_input == "1":
            gen_dea()
            s_input_flag = False
        elif s_input == "2":
            gen_npi()
            s_input_flag = False
        else:
            print(f'{d.RED}===== Invalid Input! Please select again =====')
            s_input = input(f'\n{ds.BRIGHT}{d.YELLOW}Please Select one of the following options: \n\t\t\t 1. Generate DEA number \n\t\t\t 2. Generate NPI \n\t\t\t\t{d.RED}')
            s_input_flag = True


wrap_generators()
x = input(Fore.GREEN + "\nWant to generate more NPI/DEA number? Y/N : ")
reuse = True
while reuse:
    if x.lower()=="y":
        wrap_generators()
        x = input(Fore.GREEN + "\nWant to generate more NPI/DEA number? Y/N : ")
    elif x.lower() == "n":
        print(f"{d.BLUE}{Style.bold}"+"\n"+"\t\t\t\t\t         "+"~"*30+"\n\t\t\t\t\t              "+"~"*20+f"\n\t\t\t{d.YELLOW}===== Thanks for using the DEA Number generator from \u00A9Amit ! please visit again! ====="+f"{d.BLUE}\n\t\t\t\t\t              "+"~"*20+"\n\t\t\t\t\t         "+"~"*30+"\n\n")
        time.sleep(3)
        reuse = False
    else:
        print(Fore.RED + "Ohho! Invalid input! Please select again!!!\n")
        x = input(Fore.GREEN + "\nWant to generate more NPI/DEA number? Y/N : ")
        reuse = True

