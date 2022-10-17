# Các công cụ hỗ trợ trong toàn dự án
import os 
from datetime import datetime


def clearScreen():
    os.system('cls||clear')


def printMenu(funcs: list):
    print('\n'.join(funcs))


def printHeader(title: str):
    header = f'*** {title} ***'
    print(header)
    print('-'*len(header))

def checkDate(date: str):
    date_object = None
    try:
        date_object = datetime.strptime(date, "%d/%m/%Y")
    except ValueError as err:
        date_object = None
    return date_object

def checkFloat(point: str):
    float_object = False
    try:
        float(point) # 1 phép tính bất kỳ để kiểm tra xem point nhập vào có phải số thực không
        float_object = True
    except ValueError as err:
        float_object = False
    return float_object

import re
def checkEmail(email: str):
    isValid = False
    try:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex,email)):
            isValid = True
    except Exception as err:
            print(err)
    return isValid