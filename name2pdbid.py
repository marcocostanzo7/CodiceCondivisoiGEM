f  = open("id.txt")

#user = input('Si inserisca il prorpio nome: ')



def get_id(user):
    user.upper()

    value = {
        ' ' : 0,
        'A' : 1,
        'à' : 1,
        'B' : 2,
        'C' : 3,
        'D' : 4,
        'E' : 5,
        'è' : 5,
        'F' : 6,
        'G' : 7,
        'H' : 8,
        'I' : 9,
        'ì' : 9,
        'J' : 10,
        'K' : 11,
        'L' : 12,
        'M' : 13,
        'N' : 14,
        'O' : 15,
        'ò' : 15,
        'P' : 16,
        'Q' : 17,
        'R' : 18,
        'S' : 19,
        'T' : 20,
        'U' : 21,
        'ù' : 21,
        'V' : 22,
        'W' : 23,
        'X' : 24,
        'Y' : 25,
        'Z' : 26
    }

    numb = 0

    for i in user:
        numb = numb  + value[i]
    print(numb)
    result = f.readlines()
    
    return result[numb]


