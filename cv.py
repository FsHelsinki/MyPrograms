import cv2
import numpy as np
# vid = cv2.VideoCapture('Photos/vid2.mp4')
# while True:
#     success, img = vid.read()
#     cv2.imshow('School', img)
#     if cv2.waitKey(2) & 0xFF == ord('q'):
#         break
sand = cv2.imread('Photos/send.jpg')
durov = cv2.imread('Photos/durov.jpg')
cv2.imshow('man', durov)
cv2.waitKey(1000)

durov = cv2.resize(durov, (durov.shape[1]//2, durov.shape[0]//2))
sand = cv2.resize(sand, (sand.shape[1]//4, sand.shape[0]//4))
cv2.imshow('man', durov)
cv2.waitKey(1000)
sand = cv2.GaussianBlur(sand,(15,15), 0)    #Размытие
durov = cv2.cvtColor(durov, cv2.COLOR_BGR2GRAY)
cv2.imshow('man', durov)
cv2.waitKey(1000)
durov = cv2.Canny(durov, 105, 105)
cv2.imshow('man', durov)
cv2.waitKey(1000)
b = np.ones((500, 500, 3), np.uint8)
print('Что хотите видеть?')
text = input('крест/круг/текст ')
while True:
    if text == 'крест':
        cv2.cv2.line(b, (0, 0), (500, 500), (0, 0, 255), thickness=10)
        cv2.cv2.line(b, (500, 0), (0, 500), (0, 0, 255), thickness=10)
        cv2.imshow('0', b)
        cv2.waitKey(0)

    elif text == 'круг':
        cv2.cv2.circle(b, (250, 250), 250, (255, 255, 255), thickness=6)
        cv2.imshow('0', b)
        cv2.waitKey(0)

    elif text == 'решетка':
        cv2.cv2.rectangle(b, (100, 100), (b.shape[0] // 2, b.shape[1] // 2), (240, 7, 157), thickness=cv2.cv2.FILLED)
        cv2.cv2.rectangle(b, (400, 400), (b.shape[0] // 2, b.shape[1] // 2), (240, 7, 157), thickness=cv2.cv2.FILLED)
        cv2.cv2.rectangle(b, (400, 100), (b.shape[0] // 2, b.shape[1] // 2), (240, 7, 157), thickness=3)
        cv2.cv2.rectangle(b, (100, 400), (b.shape[0] // 2, b.shape[1] // 2), (240, 7, 157), thickness=3)
        cv2.imshow('0', b)
        cv2.waitKey(0)

    elif text == 'текст':
        frase = input('Введите текст: ')

        cv2.cv2.putText(b, frase, (50, 50), cv2.cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 3)

        cv2.imshow('0', b)
        cv2.waitKey(0)
#b[100:400, 100:400] = 240, 7, 157
# cv2.cv2.rectangle(b, (100,100), (b.shape[0]//2,b.shape[1]//2), (240, 7, 157), thickness=cv2.cv2.FILLED)
# cv2.cv2.rectangle(b, (400,400), (b.shape[0]//2,b.shape[1]//2), (240, 7, 157), thickness=cv2.cv2.FILLED)
# cv2.cv2.rectangle(b, (400,100), (b.shape[0]//2,b.shape[1]//2), (240, 7, 157), thickness=3)
# cv2.cv2.rectangle(b, (100,400), (b.shape[0]//2,b.shape[1]//2), (240, 7, 157), thickness=3)
# cv2.cv2.line(b, (0,0), (500,500), (0,0,255), thickness=10)
# cv2.cv2.line(b, (500,0), (0,500), (0,0,255), thickness=10)
# cv2.cv2.circle(b, (250,250), 250, (255,255,255),thickness=6)
#
# cv2.cv2.putText(b, 'I WILL SHOOT', (50,50), cv2.cv2.FONT_ITALIC, 1,(255,255,0), 3)
#cv2.imshow('0', b)
cv2.waitKey(000)
kernel = np.ones((5,5), np.uint8)   # uint8 - это формат важная штука менять нельзя
durov = cv2.dilate(durov, kernel, iterations=1)
#cv2.imshow('man', durov)
#cv2.waitKey(1000)






















# import cv2
# pic1 = input('Введите название картинки ')
#
# imgbmw = cv2.imread('image/bmw.jpg')
# imgford = cv2.imread('image/ford.jpg')
# pic = {'форд':1, 'лада':2, 'шевроле':3, 'тесла':4, 'порш':5, 'ламборгини':6, 'рено':7, 'хёндай':8}
# if pic[pic1] == 1:
#     imgford = cv2.imread('image/ford.jpg')
#     cv2.imshow('ford', imgford)
#     cv2.waitKey(0)
# elif pic[pic1] == 2:
#     imglada = cv2.imread('image/lada.jpeg')
#     cv2.imshow('lada', imgbmw)
#     cv2.waitKey(0)
#
# elif pic[pic1] == 2:
#     imglada = cv2.imread('image/lada.jpeg')
#     cv2.imshow('lada', imglada)
#     cv2.waitKey(0)