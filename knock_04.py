
if __name__ == "__main__":
    MSG = "Hi He Lied Because Boron Could Not Oxidize Fluorine.\
           New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    word_list = MSG.split()

    genso = {}
    signal = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    for index in range(len(word_list)):
        cin = 1 if index+1 in signal else 2
        genso[index+1] = word_list[index][:cin]
    print(genso)




