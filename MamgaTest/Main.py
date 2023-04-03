import Magma
import sys
import fileinput



def Encrypt():
    fileKey, fileOutput, fileText = GetArgs()
    CheckEmtyFields(fileKey)
    plainText = GetPlainText(fileText)
    key = GetKey(fileKey)
    textEncrypt = Magma.encrypt(plainText, key)
    WriteAnswer(fileOutput, textEncrypt)

def Decrypt():
    fileKey, fileOutput, fileText = GetArgs()
    CheckEmtyFields(fileKey)
    plainText = GetPlainText(fileText)
    key = GetKey(fileKey)
    textDecrypt = Magma.decrypt(plainText, key)
    WriteAnswer(fileOutput, Magma.hexToUtf8(textDecrypt))


def GetArgs():
    params = sys.argv
    i = 2
    while(i < len(params)):
        if params[i] == '-k':
            i += 1
            fileKey = params[i]
        elif params[i] == '-o':
            i += 1
            fileOutput = params[i]
        elif params[i] == '-i':
            i += 1
            fileText = params[i]
        i += 1
    return (fileKey, fileOutput, fileText)

def GetPlainText(fileText):
    result = ''
    if fileText == '':
        print("Введите входное сообщение")
        for line in fileinput.input():
            result += line
    else:
        with open(fileText) as file:
            result = file.read()
            file.close()
    return result


def CheckEmtyFields(fileKey):
    if fileKey == None:
        raise Exception("Введите ключ!")


def GetKey(fileKey):
    with open(fileKey) as file:
        result = "".join([line for line in file])
        file.close()
    return result


def WriteAnswer(fileOutput, text):
    if fileOutput == None:
        print(text)
    else:
        f = open(fileOutput, 'w')
        f.write(text)
        f.close()


def main():
    params = sys.argv
    if params[1] == 'encrypt':
        Encrypt()
    elif params[1] == 'decrypt':
        Decrypt()
    else:
        raise Exception("Некорректный ввод");

if __name__=='__main__':
    main()