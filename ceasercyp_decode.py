def ceasercyp_decode (str, int):
    """The goal of this function is to print out the rotated version of the string
    By the mean of the rotating string, we mean to increase the index of a letter as 'int'
    Since the ord value for the uppercase and lowercase of the same letter is different """
    yenistring = ''
    for i in range(len(str)):
        magara = chr(ord(str[i]) + int)
        yenistring += magara
    print(yenistring)