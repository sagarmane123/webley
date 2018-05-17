import csv
import itertools
import re
import sys

'''
 readCSV

 Read CSV file and store output in list format

'''
def readCSV(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        dishes_list = list(reader)
    return dishes_list

'''
getPrice

function return price in float format by removing prefix currency

'''
def getPrice(price):
    try:
        return float(re.compile(r'[^-\d.,]+').sub('', price))
    except:
        return 0.0

'''
getDishes

Function return different combination of menu matches with target value

'''
def getDishes(dishes):
    # if (dishes[0][1] == ''):
    #     print('Target value not properly defined')
    #     exit()
    target = getPrice(dishes[0][1])
    if target==0.0:
        print('Target value not properly defined')
    dishes_price = []
    dishes_name = []
    dishes_comb = []

    for i in dishes[1:]:
        dish_price = getPrice(i[1])
        if (dish_price>0):
            dishes_price.append(dish_price)
            dishes_name.append(i[0])
    for L in range(1, len(dishes_price) + 1):
        for i, subset in enumerate(itertools.combinations(dishes_price, L)):
            if sum(subset) == target:
                index = [dishes_price.index(a) for a in list(subset)]
                dish_comb = [(dishes_name[a], dishes_price[a]) for a in index]
                dishes_comb.append(dish_comb)
    return dishes_comb

'''
printResult

Function to print different combination of menu

'''
def printResult(b):
    for i, j in enumerate(b):
        print('\nDish Combination ', (i + 1))
        for k in j:
            print(k)

def getDicision():
    user_decision = input('\nDo you want to continue ? [y/n]\n')
    flag = True if user_decision == 'y' else  False
    return flag

def main():
    try:
        flag = True
        while(flag):
            filename = input('\nEnter file name eg. Dishes.csv\n')
            dishes = readCSV(filename)
            dish_comb = getDishes(dishes)
            if (len(dish_comb) == 0):
                print('There is no combination of dishes that is equal to the target price')
            else:
                printResult(dish_comb)

            flag = getDicision()

    except ValueError:
        print("Price is blank or not in proper format")

    except FileNotFoundError:
        print("Wrong file or file path")
        pass

    except:
        print('Something goes wrong :)')
        # print(sys.exc_info()[1])
        pass

    if flag==False:
        exit()
    if getDicision():
        main()

if __name__ == "__main__":
    main();
