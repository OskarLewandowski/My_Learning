# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 110"""


def word_to_length(infile, outfile):
    """Zwraca teskt zapisany za pomocą liczb
    liczba reprezentuje ilość liter w słowie
    Przykład `pies, czyli kot`
    powinno wyjść `5 5 3`"""

    newNumbereWords = ""
    count = 0
    readFile = open(infile.name, "r")
    writeFile = open(outfile.name, "w")

    if(readFile.readable()):
        text = readFile.readlines()
        for x in text:
            #print("CAŁA LINIA " + x)
            count = 0
            for y in x:
                #print(y)
                if(y != " " and y != "\n"):
                    count = count + 1
                    #print(count)
                elif(count == 0):
                    writeFile.write("\n")
                    newNumbereWords = newNumbereWords + "\n"
                elif(y == "\n"):
                    #print("Koniec lini")
                    writeFile.write(str(count) + "\n")
                    newNumbereWords = newNumbereWords + str(count) + "\n"
                    count = 0
                else:
                    #print("jeden wyraz")
                    writeFile.write(str(count) + " ")
                    newNumbereWords = newNumbereWords + str(count) + " "
                    count = 0
    readFile.close()
    writeFile.close()
    #print(newNumbereWords)
    return newNumbereWords



if __name__ == '__main__':
    print(word_to_length("Task110Test.dat.in.txt", "Task110Test.out.txt"))
