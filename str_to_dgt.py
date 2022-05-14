def str_dgt(string):
    d = {'zero':0,
     'one':1,
     'two':2,
     'three':3,
     'four':4,
     'five':5,
     'six':6,
     'seven':7,
     'eight':8,
     'nine':9,
     'ten':10,
     'eleven':11,
     'twelve':12,
     'thirteen':13,
     'fourteen':14,
     'fifteen':15,
     'sixteen':16,
     'seventeen':17,
     'eighteen':18,
     'nineteen':19,
     'twenty':20,
     'thirty':30,
     'forty':40,
     'fifty':50,
     'sixty':60,
     'seventy':70,
     'eighty':80,
     'ninety':90,
     'hundred':100,
         'thousand': 1000,
         '1 million':1000000}
    if string == 'one million':
        return 1000000
    string = string.replace('-', ' ')
    string = string.split(' ')
    if 'and' in string:
        count = string.count('and')
        for j in range(0, count):
            del string[string.index('and')]
            j +=1
    arr = []
    rez = 0
    for i in string:
        if i in d.keys():
            arr.append(d[i])
    def one(arr, rez):
        for i in arr:
            rez += i
        return rez
    def hundred(arr, rez):
        if len(arr) == 1:
            return rez+arr[0]
        if arr[1] == 100 and 1000 not in arr:
            arr[0] = 100 * arr[0]
            del arr[1]
        else:
            return one(arr, rez)
        return one(arr, rez)
    def thouthand(arr, rez):
        index = arr.index(1000)
        if index == len(arr)-1:
            print(arr)
            return hundred(arr[0:index], rez) * 1000
        rez_100 = hundred(arr[0:index], rez)
        arr[index] = rez_100 * 1000
        del arr[0:index]
        rez = arr[0] + hundred(arr[1:], rez)
        return rez
    if 1000 in arr:
        return thouthand(arr,rez)
    elif 100 in arr and 1000 not in arr:
        return  hundred(arr,rez)
    else:
        return one(arr,rez)