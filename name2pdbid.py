def get_id(user):
    f  = open("id.txt")

    user.upper()

    value = {
        ' ' : 0,
        'A' : 10,
        'à' : 10,
        'B' : 20,
        'C' : 30,
        'D' : 40,
        'E' : 50,
        'è' : 50,
        'F' : 60,
        'G' : 70,
        'H' : 80,
        'I' : 90,
        'ì' : 90,
        'J' : 100,
        'K' : 110,
        'L' : 120,
        'M' : 130,
        'N' : 140,
        'O' : 150,
        'ò' : 150,
        'P' : 160,
        'Q' : 170,
        'R' : 180,
        'S' : 190,
        'T' : 200,
        'U' : 210,
        'ù' : 210,
        'V' : 220,
        'W' : 230,
        'X' : 240,
        'Y' : 250,
        'Z' : 260
    }

    numb = 0

    for i in user:
        numb = numb  + value[i]
    result = f.readlines()

    f.close()

    return result[numb]

