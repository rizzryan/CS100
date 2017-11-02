# Ryan Welch
# CS100 2017F Section 105
# HW 07, November 2nd, 2017

import random

def combineLists(k, v):
    d = {}
    for elems in range(len(k)):
        if k[elems] in d.keys():
            d[k[elems]].append(v[elems])
        else:
            d[k[elems]] = [v[elems]]
    print(d)

def who(ledger, item):
    numItems = len(ledger)
    name = []

    for items in ledger:
        if item in ledger[items]:
            name.append(items)
    print(name)


if __name__ == '__main__':
    peeps = ['Trevor', 'Joey', 'Joey', 'Trevor', 'Joey']
    stuff = ['Pencil', 'Notebook', 'Laptop', 'Speakers', 'Calculator']
    d = {'Joe' : ['Soda' , 'Candy'], 'Alex' : ['Soda', 'Pretzels']}

    # combineLists(peeps, stuff)
    who(d, 'Candy')
