import math
import sys

print('Вы являетесь, ПЕРВЫМ пользователем, пожалуйста, представьтесь : ')
userOne = str(input())
print('Вы являетесь, ВТОРЫМ пользователем, пожалуйста, представьтесь : ')
userTwo = str(input())
# Протокол Диффи-Хеллмана
# шаг 1
print(userOne, ' , пожалуйста, введите модуль :')
aliceModule = int(input())
print(userTwo, ' , пожалуйста, введите основание : ')
bobFooting = int(input())

# шаг2
print(userOne, ' , пожалуйста, введите приватный ключ : ')
alicePrivateKey = int(input())
print(userTwo, ' , пожалуйста, введите приватный ключ : ')
bobPrivateKey = int(input())

# шаг3
alicePublicKey = math.pow(bobFooting, alicePrivateKey) % aliceModule
bobPublicKey = math.pow(bobFooting, bobPrivateKey) % aliceModule

# шаг4
print(userOne, ' , Ваш публичный ключ : ', int(bobPublicKey), '|',
      userTwo, ' , Ваш публичный ключ : ', int(alicePublicKey), '\n')
# шаг5
aliceSecretKey = math.pow(bobPublicKey, alicePrivateKey) % aliceModule
bobSecretKey = math.pow(alicePublicKey, bobPrivateKey) % aliceModule
print(userOne, ' , Ваш секретный ключ : ', int(aliceSecretKey), '|',
      userTwo, ' , Ваш секретный ключ : ', int(bobSecretKey), '\n')
if aliceSecretKey == bobSecretKey:
    sharedSecretKey = aliceSecretKey
    print('Общий секретный ключ : ', int(sharedSecretKey), '\n')
else:
    print('Ошибка, общий ключ НЕ совпал')
    sys.exit()

# Алфавит в нижнем регистре
llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
        'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

# Алфавит в высоком регистре
ulst = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х',
        'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']


# Зашифровать сообщение
def encryptCaesar(msg, shift):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x) % len(llst)
            ret += llst[(ind + shift) % len(llst)]
        elif x in ulst:
            ind = ulst.index(x) % len(llst)
            ret += ulst[(ind + shift) % len(llst)]
        else:
            ret += x
    return ret


# Расшифровать сообщение
def decryptCaesar(msg, shift):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x)
            ret += llst[ind - shift]
        elif x in ulst:
            ind = ulst.index(x)
            ret += ulst[ind - shift]
        else:
            ret += x
    return ret


print('Пожалуйста, введите ваше сообщение : ')
message = str(input())
print('Ваше сообщение в зашифрованном виде выглядит следующим образом : ', encryptCaesar(message, int(sharedSecretKey)))
print('Ваше сообщение в расшифрованном виде выглядит следующим образом : ',
      decryptCaesar(message, int(sharedSecretKey)))

sys.exit()