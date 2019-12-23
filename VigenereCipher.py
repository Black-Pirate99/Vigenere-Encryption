#!/usr/bin/python
letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']


def findIndex(string):
    index = []
    for i in range(len(string)):
        for j in range(len(letter)):
            if (string[i].upper() == letter[j]):
                index.append(j)
    return index


def checkLength(textIndex=[], keyIndex=[]):
    counter = 0
    while True:
        if len(textIndex) <= len(keyIndex):
            return True
        # if len(textIndex) == len(keyIndex):
        #     return True
        if counter >= len(keyIndex):
            counter = 0
        keyIndex.append(keyIndex[counter])
        counter += 1


def sort(text, reslut=[]):
    for i in range(len(text)):
        if text[i] == ' ':
            reslut.insert(i, ' ')


def encryption(text , kek):
    tIndex = findIndex(text)
    kIndex = findIndex(key)

    if len(tIndex) > len(kIndex):
        base = checkLength(tIndex, kIndex)
        if base == True:
            print("The Message Index: %s" % tIndex)
            print("The Key Index    : %s" % kIndex)

            cipherText = []
            for i in range(len(tIndex)):
                Ci = (tIndex[i] + kIndex[i]) % 26
                cipherText.append(letter[Ci])
            sort(text, cipherText)
            cipherText = ''.join(cipherText)
            print("\n[*] The Cipher Message is: %s\n" % cipherText.lower())
            return cipherText

    else:
        print("The Message Index: %s" % tIndex)
        print("The Key Index    : %s" % kIndex)

        cipherText = []
        for i in range(len(tIndex)):
            Ci = (tIndex[i] + kIndex[i]) % 26
            cipherText.append(letter[Ci])
        sort(text, cipherText)
        cipherText = ''.join(cipherText)
        print("\n[*] The Cipher Message is: %s\n" % cipherText.lower())
        return cipherText.lower()


def decryption(cipherText="", key=""):
    tIndex = findIndex(cipherText)
    kIndex = findIndex(key)
    if len(tIndex) > len(kIndex):
        base = checkLength(tIndex, kIndex)
        if base == True:
            print("The Cipher Message Index: %s" % tIndex)
            print("The Key Index           : %s" % kIndex)

            messageText = []
            for i in range(len(tIndex)):
                Mi = (tIndex[i] - kIndex[i])
                messageText.append(letter[Mi])

            sort(cipherText, messageText)
            messageText = ''.join(messageText)

            print("\n[*] The Message is: %s\n" % messageText.lower())
    else:
        print("The Cipher Message Index: %s" % tIndex)
        print("The Key Index           : %s" % kIndex)

        messageText = []
        for i in range(len(tIndex)):
            Mi = (tIndex[i] - kIndex[i])
            messageText.append(letter[Mi])

        sort(cipherText, messageText)
        messageText = ''.join(messageText)
        print("\n[*] The Message is: %s\n" % messageText.lower())

    return messageText.lower()


if __name__ == '__main__':
    while True:
        try:
            letter2 = ['A=0', 'B=1', 'C=2', 'D=3', 'E=4', 'F=5', 'G=6', 'H=7', 'I=8', 'J=9', 'K=10', 'L=11', 'M=12',
                       'N=13',
                       'O=14', 'P=15', 'Q=16', 'R=17', 'S=18', 'T=19', 'U=20', 'V=21', 'W=22', 'X=23', 'Y=24', 'Z=25']
            choice = input(
                "1) Encryption: \n2) Decryption: \n3) Encrypt a File \n4) Decrypt a File \n5) Exit \nEnter The Number: ")
            if choice == 1:
                print "%s" % letter2[0:14]
                print "%s\n" % letter2[14:26]
                text = raw_input("Enter The Message: ")
                key = raw_input("Enter The Key    : ")
                encryption(text, key)

            if choice == 2:
                print "%s" % letter2[0:14]
                print "%s\n" % letter2[14:26]

                text = raw_input("Enter The Cipher Message: ")
                key = raw_input("Enter The Key           : ")

                decryption(text, key)

            if (choice == 3):
		print "%s" % letter2[0:14]
                print "%s\n" % letter2[14:26]
                key = raw_input("Enter The Key: ")
                filename = raw_input("Enter File Name To Encrypt: ")
                f = open(filename, 'r')
                filename2 = raw_input("Enter File Name To Save: ")
                fw = open(filename2, 'w+')

                for text in f.readlines():
                    fw.write(encryption(text, key).lower())
                    fw.write('\n')
                fw.close()
                f.close()

            if choice == 4:
		print "%s" % letter2[0:14]
                print "%s\n" % letter2[14:26]
	        key = raw_input("Enter The Key: ")
                filename = raw_input("Enter File Name To Decrypt: ")
                f = open(filename, 'r')
                filename2 = raw_input("Enter File Name To Save: ")
                fw = open(filename2, 'w+')
                for text in f.readlines():
                    fw.write(decryption(text, key))
                    fw.write('\n')
                fw.close()
                f.close()

            if choice == 5:
                break

        except:
            print"\n[!] Enter Number Only\n"
