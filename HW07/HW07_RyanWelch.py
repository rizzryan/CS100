def combineLists(k, v):
    stuffList = []
    itemList = []
    possesionList = []
    d1 = dict()

    for elems in range(len(v)):
        stuffList.append(k[elems] + ',' + v[elems])

    for items in stuffList:
        possesionList.append(items.split(',')[0] + ' : ' + items.split(',')[1])
        # if items.count(items.split(',')[0]) > 0 and

    # print(sorted(possesionList))
    for items in sorted(possesionList):
        d = dict()
        d.update({items.split(' : ')[0]:items.split(' : ')[1]})

        d1.update(d)

        print(d1)






if __name__ == '__main__':
    peeps = ['Trevor', 'Joey', 'Joey', 'Trevor', 'Joey']
    stuff = ['Pencil', 'Notebook', 'Laptop', 'Speakers', 'Calculator']

    combineLists(peeps, stuff)
