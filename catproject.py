import tkinter
import tkinter.messagebox
import pygame
import random
from pygame import mixer
from tkinter import*
from time import sleep
import time
from tkinter import messagebox

from tkinter import PhotoImage
from PIL import Image, ImageTk
window = Tk()
window.geometry('1400x800')
window.configure(background='#DDA0DD')
window.title('Tamagotchi')






image1 = tkinter.PhotoImage(file='cat41.png')
image2 = tkinter.PhotoImage(file='set (1).png')
image6 = tkinter.PhotoImage(file='tamagotchi (1).png')
image7 = tkinter.PhotoImage(file='playbtn1.png')
image8 = tkinter.PhotoImage(file='exitbtn1.png')
image9 = tkinter.PhotoImage(file='aboutbtn1.png')
catgif = tkinter.PhotoImage(file='catg.gif')
catl = tkinter.PhotoImage(file='catl (1).png')
lin = tkinter.PhotoImage(file='liniya.png')
coin = tkinter.PhotoImage(file='coin_94963 (1).png')
image10 = tkinter.PhotoImage(file='btnexitround.png')

imgsleep100 = tkinter.PhotoImage(file='btnsleep100.png')
imgsleep80 = tkinter.PhotoImage(file='btnsleep80.png')
imgsleep50 = tkinter.PhotoImage(file='btnsleep50.png')
imgsleep20 = tkinter.PhotoImage(file='btnsleep20.png')

imgfood100 = tkinter.PhotoImage(file='btnfood100.png')
imgfood80 = tkinter.PhotoImage(file='btnfood80.png')
imgfood50 = tkinter.PhotoImage(file='btnfood50.png')
imgfood20 = tkinter.PhotoImage(file='btnfood20.png')

imgbath100 = tkinter.PhotoImage(file='btnbath100.png')
imgbath80 = tkinter.PhotoImage(file='btnbath80.png')
imgbath50 = tkinter.PhotoImage(file='btnbath50.png')
imgbath20 = tkinter.PhotoImage(file='btnbath20.png')

imggame100 = tkinter.PhotoImage(file='btngame100.png')
imggame80 = tkinter.PhotoImage(file='btngame80.png')
imggame50 = tkinter.PhotoImage(file='btngame50.png')
imggame20 = tkinter.PhotoImage(file='btngame20.png')

imgd = tkinter.PhotoImage(file='catssd.png')
imgs = tkinter.PhotoImage(file='catss.png')

city = tkinter.PhotoImage(file='city.png')
windowoffice = tkinter.PhotoImage(file='pixelwindow.png')
comp = tkinter.PhotoImage(file='pixelcomp (2).png')
book = tkinter.PhotoImage(file='book.png')
clockoffice = tkinter.PhotoImage(file='clock.png')
water = tkinter.PhotoImage(file='water.png')
tv = tkinter.PhotoImage(file='tv (1).png')
sofa = tkinter.PhotoImage(file='sofa (1).png')
nightcity = tkinter.PhotoImage(file='nightcity.png')

bathimg = tkinter.PhotoImage(file='newbath.png')
bathcat = tkinter.PhotoImage(file='newbath1.png')
towell = tkinter.PhotoImage(file='towel.png')
mirrors = tkinter.PhotoImage(file='mirrorsink.png')

bedimg = tkinter.PhotoImage(file='bedd (1).png')
bedcatimg = tkinter.PhotoImage(file='bedcat (1).png')
closet1 = tkinter.PhotoImage(file='closetclosed (1).png')
closet2 = tkinter.PhotoImage(file='closetopened.png')

brownbear = tkinter.PhotoImage(file='bear.png')
tvv = tkinter.PhotoImage(file='tvhouse.png')

imgwithtv1 = tkinter.PhotoImage(file='tvwithprg1.png')
imgwithtv2 = tkinter.PhotoImage(file='tvwithprg2.png')
imgwithtv3 = tkinter.PhotoImage(file='tvwithprg3.png')
imgwithtv4 = tkinter.PhotoImage(file='tvwithprg4.png')
imgwithtv5 = tkinter.PhotoImage(file='tvwithprg5.png')
imgwithtv6 = tkinter.PhotoImage(file='tvwithprg6.png')
imgwithtv7 = tkinter.PhotoImage(file='tvwithprg7.png')
imgwithtv8 = tkinter.PhotoImage(file='tvwithprg8.png')
imgwithtv9 = tkinter.PhotoImage(file='tvwithprg9.png')

shopimg = tkinter.PhotoImage(file='shop.png')
clothshopimg = tkinter.PhotoImage(file='clothshop (1).png')
thing1img = tkinter.PhotoImage(file='hat1.png')
thing2img = tkinter.PhotoImage(file='hat2.png')
thing3img = tkinter.PhotoImage(file='hat3.png')
thing4img = tkinter.PhotoImage(file='glasses.png')
thing5img = tkinter.PhotoImage(file='t1.png')
thing6img = tkinter.PhotoImage(file='t2.png')
thing7img = tkinter.PhotoImage(file='t3.png')

catt1 = tkinter.PhotoImage(file='catwithhat1.png')
catt2 = tkinter.PhotoImage(file='catwithhat2.png')
catt3 = tkinter.PhotoImage(file='catwithhat3.png')
catt4 = tkinter.PhotoImage(file='catwithglasses.png')
catt5 = tkinter.PhotoImage(file='catwithtshirt.png')
catt6 = tkinter.PhotoImage(file='catwithtshirt1.png')
catt7 = tkinter.PhotoImage(file='catwithshirt3.png')

fridge = tkinter.PhotoImage(file='fridge (1).png')
table = tkinter.PhotoImage(file='table (1).png')
tablefood1 = tkinter.PhotoImage(file='food1table.png')
tablefood2 = tkinter.PhotoImage(file='food2table.png')
tablefood3 = tkinter.PhotoImage(file='food3table.png')
tablefood4 = tkinter.PhotoImage(file='food4table.png')
tablefood5 = tkinter.PhotoImage(file='food5table.png')
tablefood6 = tkinter.PhotoImage(file='food6table.png')
tablefood7 = tkinter.PhotoImage(file='food7table.png')
tablefood8 = tkinter.PhotoImage(file='food8table.png')
tablefood9 = tkinter.PhotoImage(file='food9table.png')
tablefood10 = tkinter.PhotoImage(file='food10table.png')
tablefood11 = tkinter.PhotoImage(file='food11table.png')
tablefood12 = tkinter.PhotoImage(file='food12table.png')
tablefood13 = tkinter.PhotoImage(file='food13table.png')
food1 = tkinter.PhotoImage(file='food1.png')
food2 = tkinter.PhotoImage(file='sushi.png')
food3 = tkinter.PhotoImage(file='soup.png')
food4 = tkinter.PhotoImage(file='soup1.png')
food5 = tkinter.PhotoImage(file='apple.png')
food6 = tkinter.PhotoImage(file='bananas.png')
food7 = tkinter.PhotoImage(file='pizza.png')
food8 = tkinter.PhotoImage(file='taco.png')
food9 = tkinter.PhotoImage(file='chickenmac.png')
food10 = tkinter.PhotoImage(file='fish.png')
food11 = tkinter.PhotoImage(file='doshik.png')
food12 = tkinter.PhotoImage(file='cake1.png')
food13 = tkinter.PhotoImage(file='milk.png')
shopfood = tkinter.PhotoImage(file='foodshop.png')

nofood1 = tkinter.PhotoImage(file='food1no.png')
nofood2 = tkinter.PhotoImage(file='food2no.png')
nofood3 = tkinter.PhotoImage(file='food3no.png')
nofood4 = tkinter.PhotoImage(file='food4no.png')
nofood5 = tkinter.PhotoImage(file='food5no.png')
nofood6 = tkinter.PhotoImage(file='food6no.png')
nofood7 = tkinter.PhotoImage(file='food7no.png')
nofood8 = tkinter.PhotoImage(file='food8no.png')
nofood9 = tkinter.PhotoImage(file='food9no.png')
nofood10 = tkinter.PhotoImage(file='food10no.png')
nofood11 = tkinter.PhotoImage(file='food11no.png')
nofood12 = tkinter.PhotoImage(file='food12no.png')
nofood13 = tkinter.PhotoImage(file='food13no.png')

not1 = tkinter.PhotoImage(file='t1no.png')
not2 = tkinter.PhotoImage(file='t2no.png')
not3 = tkinter.PhotoImage(file='t3no.png')
nohat1 = tkinter.PhotoImage(file='hat1no.png')
nohat2 = tkinter.PhotoImage(file='hat2no.png')
nohat3 = tkinter.PhotoImage(file='hat3no.png')
noglasses = tkinter.PhotoImage(file='glassesno.png')

mixer.init()


def clickedcat():
    L = ['myaukane-domashney-koshki-37030 (mp3cut.net).wav', 'myaukane-domashney-koshki-37030 (mp3cut.net) (1).wav',
         'aivaaroo-purr-tims (mp3cut.net).wav']
    ran = random.choice(L)
    r = pygame.mixer.Sound(ran)
    r.play()

def clickedbtn():
    image3 = tkinter.PhotoImage(file='m1.png')
    image4 = tkinter.PhotoImage(file='m2.png')
    image5 = tkinter.PhotoImage(file='m12.png')
    p = pygame.mixer.Sound('zvuk11.wav')
    p.play()
    window2 = Toplevel(window)
    window2.geometry('450x200')
    window2.configure(background='#DDA0DD')
    window2.title('Tamagotchi')

    def ml():
        songs = ['Christmas Songs - Jingle Bell Rock.mp3',
                 'Sufjan Stevens - Mystery of Love_Visions of Gideon (minus).mp3',
                 '90sFlav_-_Call_me_(musmore.com).mp3']
        songsran = random.choice(songs)
        pygame.mixer.music.load(songsran)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)


    button2 = Button(window2, image=image3, height='75', width='75', bg='#DDA0DD', relief='flat')


    def clickedbtn2():
        button2.config(image=image5)
        pygame.mixer.music.stop()
    button2.config(command=clickedbtn2)
    button2.place(x = 50, y = 50)

    label = Button(window2, image=image4, bg='#DDA0DD', relief = 'flat', command = ml)
    label.place(x = 310, y = 50)





    window2.mainloop()

label1 = Label(window, bg = '#DDA0DD', image=image6)
label1.place(x = 400, y = 1)
button = Button(window, image=image1, height='163', width='100', bg='#DDA0DD', relief='flat', command=clickedcat,
                cursor ='heart')
button.pack(pady=225)



button1 = Button(window, image=image2, height='75', width='75', bg='#DDA0DD', relief='flat', command=clickedbtn)
button1.place(x=1270, y=25)

buttonplay = Button(window, image=image7, height=150, width=300, bg='#DDA0DD', relief='flat')
buttonplay.place(x = 40, y = 150)

buttonexit = Button(window, image=image8, height=150, width=300, bg='#DDA0DD', relief='flat')
buttonexit.place(x = 40, y = 490)

buttonabout = Button(window, image=image9, height=150, width=300, bg='#DDA0DD', relief='flat')
buttonabout.place(x = 40, y = 320)

coins = 200
time = 0
sleepp = 100
eatp = 100
bathp = 100
gamep = 100
thing1 = 0
thing2 = 0
thing3 = 0
thing4 = 0
thing5 = 0
thing6 = 0
thing7 = 0
eat1 = 0
eat2 = 0
eat3 = 0
eat4 = 0
eat5 = 0
eat6 = 0
eat7 = 0
eat8 = 0
eat9 = 0
eat10 = 0
eat11 = 0
eat12 = 0
eat13 = 0
price1 = 50
price25 = 25
price100 = 100
price10 = 10
price2 = 2
price80 = 80
price5 = 5
a = 0
b = 0
c = 0
d = 0


def btnplay():
    global coins
    global time
    global sleepp
    global eatp
    global bathp
    global gamep

    p = pygame.mixer.Sound('zvuk11.wav')
    p.play()
    window4 = Toplevel(window)
    window4.geometry('1400x800')
    window4.configure(background='#DDA0DD')

    def dwn():
        global coins
        global time
        global sleepp
        global eatp
        global bathp
        global gamep
        def btnexit():
            global coins
            global time

            p = pygame.mixer.Sound('zvuk11.wav')
            p.play()
            messagebox = tkinter.messagebox.askquestion('Выход', 'Вы точно хотите выйти?', icon='error')
            if messagebox == 'yes':
                window.destroy()
        def coinsound():
            c = pygame.mixer.Sound('monetyi-vyisyipayut-2-30613.wav')
            c.play()
            messagebox2 = tkinter.messagebox.askquestion('Выход', 'Вы точно хотите пойти на работу?')
            if messagebox2 == 'yes':
                window5 = Toplevel(window)
                window5.geometry('1000x600')
                window5.configure(background='#DDA0DD')
                window5.resizable(height=False, width=False)

                labelcity = Label(window5, bg='#DDA0DD', image = city)
                labelcity.place(x = 0, y = 40)

                labeldwn1 = Label(window5, bg='#DDA0DD', text='Загрузка...', font=('Times New Roman', 20))
                labeldwn1.place(x=450, y = 0)

                citysound = pygame.mixer.Sound('peshehodnaya-alleya (mp3cut.net).wav')
                citysound.play()
                def job():
                    global coins
                    global sleepp
                    global eatp
                    global bathp
                    global gamep

                    sleep(6)
                    window5.destroy()
                    window6 = Toplevel(window)
                    window6.geometry('1000x600')
                    window6.configure(background='#DEB887')
                    window6.resizable(height=False, width=False)

                    labelbook = Label(window6, bg='#DEB887', image=book)
                    labelbook.place(x = 750, y = 150)

                    btnwindow = Button(window6, bg='#DEB887', image=windowoffice, relief='flat')
                    btnwindow.place(x = 600, y = 150)

                    btncomp = Button(window6, bg='#DEB887', image=comp, relief='flat')
                    btncomp.place(x = 330, y = 285)

                    labelclock = Label(window6, bg='#DEB887', image=clockoffice)
                    labelclock.place(x = 860, y = 80)

                    labelwater = Label(window6, bg='#DEB887', image=water)
                    labelwater.place(x = 270, y = 333)

                    labeltv = Label(window6, bg='#DEB887', image=tv)
                    labeltv.place(x = 330, y = 120)

                    labelsofa = Label(window6, bg='#DEB887', image=sofa)
                    labelsofa.place(x = 35, y = 340)

                    labelcoin1 = Label(window6, bg='#DEB887', image=coin)
                    labelcoin1.place(x=1, y=1)

                    labelcointext = Label(window6, bg='#DEB887', font=('Times New Roman', 20), text=coins)
                    labelcointext.place(x=80, y = 10)

                    def birds():
                        bird = pygame.mixer.Sound('effekt-peniya-ptits-26159 (mp3cut.net).wav')
                        bird.play()



                    def compkl():
                        global time
                        global coins
                        global sleepp
                        global eatp
                        global bathp
                        global gamep
                        time += 1
                        coins += 5
                        sleepp -= 2
                        eatp -= 2
                        bathp -= 2
                        gamep -= 1

                        kb = pygame.mixer.Sound('klaviatura-kompyutera-30453 (mp3cut.net).wav')
                        kb.play()
                        labelcoin.config(text=coins)
                        labelcointext.config(text=coins)
                        if sleepp < 100 and sleepp >= 80:
                            buttonsleep.config(image=imgsleep80)
                        elif sleepp < 80 and sleepp >= 50:
                            buttonsleep.config(image=imgsleep50)
                        elif sleepp < 50 and sleepp >= 20:
                            button.config(image=imgs)
                            buttonsleep.config(image=imgsleep20)

                        elif sleepp < 20:
                            button.destroy()
                            messagebox1 = tkinter.messagebox.showinfo('Котик ушел',
                                                                      'К сожалению, вы не заботились о котенке, '
                                                                      'и он ушел. Видимо вам еще слишком рано заводить питомцев.')
                            buttongame.config(command='')
                            buttonsleep.config(command='')
                            buttongame.config(command='')
                            buttoneat.config(command='')
                            coinbtn.config(command='')

                        if eatp < 100 and eatp >= 80:
                            buttoneat.config(image=imgfood80)
                        elif eatp < 80 and eatp >= 50:
                            buttoneat.config(image=imgfood50)
                        elif eatp < 50 and eatp >= 20:
                            button.config(image=imgs)
                            buttoneat.config(image=imgfood20)

                        elif eatp < 20:
                            button.destroy()
                            messagebox5 = tkinter.messagebox.showinfo('Котик ушел',
                                                                      'К сожалению, вы не заботились о котенке, '
                                                                      'и он ушел. Видимо вам еще слишком рано заводить питомцев.')
                            buttongame.config(command='')
                            buttonsleep.config(command='')
                            buttongame.config(command='')
                            buttoneat.config(command='')
                            coinbtn.config(command='')
                        if bathp < 100 and bathp >= 80:
                            buttonbath.config(image=imgbath80)
                        elif bathp < 80 and bathp >= 50:
                            buttonbath.config(image=imgbath50)
                        elif bathp < 50 and bathp >= 20:
                            button.config(image=imgd)
                            buttonbath.config(image=imgbath20)

                        elif bathp < 20:
                            button.destroy()
                            messagebox7 = tkinter.messagebox.showinfo('Котик ушел',
                                                                      'К сожалению, вы не заботились о котенке, '
                                                                      'и он ушел. Видимо вам еще слишком рано заводить питомцев.')
                            buttongame.config(command='')
                            buttonsleep.config(command='')
                            buttongame.config(command='')
                            buttoneat.config(command='')
                            coinbtn.config(command='')

                        if gamep < 100 and gamep >= 80:
                            buttongame.config(image=imggame80)
                        elif gamep < 80 and gamep >= 50:
                            buttongame.config(image=imggame50)
                        elif gamep < 50 and gamep >= 20:
                            button.config(image=imgs)
                            buttongame.config(image=imggame20)

                        elif gamep < 20:
                            button.destroy()
                            messagebox8 = tkinter.messagebox.showinfo('Котик ушел',
                                                                      'К сожалению, вы не заботились о котенке, '
                                                                      'и он ушел. Видимо вам еще слишком рано'
                                                                      ' заводить питомцев.')
                            buttongame.config(command='')
                            buttonsleep.config(command='')
                            buttongame.config(command='')
                            buttoneat.config(command='')
                            coinbtn.config(command='')

                        if time >= 25:
                            time = 0
                            m = tkinter.messagebox.showinfo('Домой!', 'Вы уже задерживаетесь!'
                                                                      ' Идите домой, ваш котик скучает...')
                            window6.destroy()
                            window7 = Toplevel(window)
                            window7.geometry('1000x600')
                            window7.configure(background='#DDA0DD')
                            window7.resizable(height=False, width=False)

                            nightcitylabel = Label(window7, bg='#DDA0DD', image=nightcity)
                            nightcitylabel.place(x = 0, y = 40)

                            nightcitydwn = Label(window7, bg='#DDA0DD', text='Загрузка...',
                                                 font=('Times New Roman', 20))
                            nightcitydwn.place(x = 450, y = 0)

                            nightcitysound = pygame.mixer.Sound('zapisan-nochnoy-gorodskoy-sredyi-dvijeniya'
                                                                '-shumnyiy-zvuk-42731 (mp3cut.net).wav')
                            nightcitysound.play()
                            def dwn3():
                                sleep(6)
                                window7.destroy()

                            window7.after(100, dwn3)
                            window7.mainloop()



                    btnwindow.config(command=birds)
                    btncomp.config(command=compkl)


                    window6.mainloop()

                window.after(200, job)
                window5.mainloop()

        sleep(3)
        buttonplay.destroy()
        buttonabout.destroy()
        buttonexit.destroy()



        labelliniya = Label(window, image=lin, bg='#DDA0DD')
        labelliniya.place(x = 150, y=0)

        labelliniya2 = Label(window, image=lin, bg='#DDA0DD')
        labelliniya2.place(x = 1200, y =0)

        buttonexit1 = Button(window, image=image10, bg='#DDA0DD', relief='flat', command=btnexit)
        buttonexit1.place(x=1220, y=550)

        coinbtn = Button(window, image = coin, bg='#DDA0DD', relief = 'flat', command=coinsound)
        coinbtn.place(x = 1, y = 0)

        buttoneat = Button(window, image=imgfood100, bg='#DDA0DD', relief='flat')
        buttoneat.place(x = 315, y = 550)

        buttonbath = Button(window, image=imgbath100, bg='#DDA0DD', relief='flat')
        buttonbath.place(x=515, y=550)

        buttongame = Button(window, image=imggame100, bg='#DDA0DD', relief='flat')
        buttongame.place(x=715, y=550)

        buttonsleep = Button(window, image=imgsleep100, bg='#DDA0DD', relief='flat')
        buttonsleep.place(x=915, y=550)



        def gameroom():
            p = pygame.mixer.Sound('zvuk11.wav')
            p.play()

            smallbear = Button(window, bg='#DDA0DD', relief='flat', image=brownbear)
            smallbear.place(x=800, y=250)

            tvh = Button(window, bg='#DDA0DD', relief='flat', image=tvv)
            tvh.place(x = 300, y = 200)

            def tvon():
                global sleepp
                global eatp
                global bathp
                global gamep

                p = pygame.mixer.Sound('zvuk11.wav')
                p.play()
                T = [tvv, imgwithtv1, imgwithtv2, imgwithtv3, imgwithtv4, imgwithtv5, imgwithtv6,
                     imgwithtv7, imgwithtv8, imgwithtv9]
                to = random.choice(T)
                tvh.config(image=to)
                if gamep == 100:
                    sleepp += 0
                elif gamep < 100:
                    sleepp -= 1
                    gamep += 3
                if sleepp < 100 and sleepp >= 80:
                    buttonsleep.config(image=imgsleep80)
                elif sleepp < 80 and sleepp >= 50:
                    buttonsleep.config(image=imgsleep50)
                elif sleepp < 50 and sleepp >= 20:
                    button.config(image=imgs)
                    buttonsleep.config(image=imgsleep20)

                elif sleepp < 20:
                    button.destroy()
                    messagebox1 = tkinter.messagebox.showinfo('Котик ушел',
                                                              'К сожалению, вы не заботились о котенке, '
                                                              'и он ушел. Видимо, вам еще слишком рано заводить питомцев.')
                    buttongame.config(command='')
                    buttonsleep.config(command='')
                    buttongame.config(command='')
                    buttoneat.config(command='')
                    coinbtn.config(command='')

                if gamep < 100 and gamep >= 80:
                    buttongame.config(image=imggame80)
                elif gamep < 80 and gamep >= 50:
                    buttongame.config(image=imggame50)
                elif gamep < 50 and gamep >= 20:
                    button.config(image=imgs)
                    buttongame.config(image=imggame20)

                elif gamep < 20:
                    button.destroy()
                    messagebox8 = tkinter.messagebox.showinfo('Котик ушел',
                                                              'К сожалению, вы не заботились о котенке, '
                                                              'и он ушел. Видимо, вам еще слишком рано'
                                                              ' заводить питомцев.')
                    buttongame.config(command='')
                    buttonsleep.config(command='')
                    buttongame.config(command='')
                    buttoneat.config(command='')
                    coinbtn.config(command='')
            def bearz():
                global sleepp
                global eatp
                global bathp
                global gamep
                if gamep == 100:
                    gamep += 0
                elif gamep < 100:
                    gamep += 1
                    sleepp -= 1
                Bz = ['zvuk-rezinovoy-igrushki-pischalki-16885 (mp3cut.net) (1).wav',
                      'zvuk-rezinovoy-igrushki-pischalki-16885 (mp3cut.net) (2).wav',
                      'zvuk-rezinovoy-igrushki-pischalki-16885 (mp3cut.net) (3).wav',
                      'zvuk-rezinovoy-igrushki-pischalki-16885 (mp3cut.net).wav']
                z = random.choice(Bz)
                lz = pygame.mixer.Sound(z)
                lz.play()

                if sleepp < 100 and sleepp >= 80:
                    buttonsleep.config(image=imgsleep80)
                elif sleepp < 80 and sleepp >= 50:
                    buttonsleep.config(image=imgsleep50)
                elif sleepp < 50 and sleepp >= 20:
                    button.config(image=imgs)
                    buttonsleep.config(image=imgsleep20)

                elif sleepp < 20:
                    button.destroy()
                    messagebox1 = tkinter.messagebox.showinfo('Котик ушел',
                                                              'К сожалению, вы не заботились о котенке, '
                                                              'и он ушел. Видимо, вам еще слишком рано заводить питомцев.')
                    buttongame.config(command='')
                    buttonsleep.config(command='')
                    buttongame.config(command='')
                    buttoneat.config(command='')
                    coinbtn.config(command='')

                if gamep < 100 and gamep >= 80:
                    buttongame.config(image=imggame80)
                elif gamep < 80 and gamep >= 50:
                    buttongame.config(image=imggame50)
                elif gamep < 50 and gamep >= 20:
                    button.config(image=imgs)
                    buttongame.config(image=imggame20)

                elif gamep < 20:
                    button.destroy()
                    messagebox8 = tkinter.messagebox.showinfo('Котик ушел',
                                                              'К сожалению, вы не заботились о котенке, '
                                                              'и он ушел. Видимо, вам еще слишком рано'
                                                              ' заводить питомцев.')
                    buttongame.config(command='')
                    buttonsleep.config(command='')
                    buttongame.config(command='')
                    buttoneat.config(command='')
                    coinbtn.config(command='')

            tvh.config(command=tvon)
            smallbear.config(command=bearz)

        buttongame.config(command=gameroom)


        def sleeppp():
            p = pygame.mixer.Sound('zvuk11.wav')
            p.play()

            def sleeping():
                p = pygame.mixer.Sound('zvuk11.wav')
                p.play()
                global sleepp
                global eatp
                global bathp
                global gamep
                sleepb.config(image=bedcatimg)
                button.config(image='')
                buttonsleep.config(command='')
                buttoneat.config(command='')
                buttongame.config(command='')
                buttonbath.config(command='')
                shopbutton.config(command='')
                coinbtn.config(command='')
                closetc.config(command='')
                sleepb.config(command='')
                bs = 100 - sleepp
                bsm = bs*60000
                if sleepp == 100:
                    sleepp += 0
                elif sleepp < 100:
                    sleepp += bs
                    gamep -= 15
                    eatp -= 15
                    bathp -= 5
                if sleepp < 100 and sleepp >= 80:
                    buttonsleep.config(image=imgsleep80)
                elif sleepp < 80 and sleepp >= 50:
                    buttonsleep.config(image=imgsleep50)
                elif sleepp < 50 and sleepp >= 20:
                    buttonsleep.config(image=imgsleep20)

                elif sleepp < 20:
                    button.destroy()
                    messagebox1 = tkinter.messagebox.showinfo('Котик ушел',
                                                              'К сожалению, вы не заботились о котенке, '
                                                              'и он ушел. Видимо, вам еще слишком рано заводить питомцев.')
                    buttongame.config(command='')
                    buttonsleep.config(command='')
                    buttongame.config(command='')
                    buttoneat.config(command='')
                    coinbtn.config(command='')


                if eatp < 100 and eatp >= 80:
                    buttoneat.config(image=imgfood80)
                elif eatp < 80 and eatp >= 50:
                    buttoneat.config(image=imgfood50)
                elif eatp < 50 and eatp >= 20:
                    buttoneat.config(image=imgfood20)

                elif eatp < 20:
                    button.destroy()
                    messagebox5 = tkinter.messagebox.showinfo('Котик ушел',
                                                              'К сожалению, вы не заботились о котенке, '
                                                              'и он ушел. Видимо, вам еще слишком рано заводить питомцев.')
                    buttongame.config(command='')
                    buttonsleep.config(command='')
                    buttongame.config(command='')
                    buttoneat.config(command='')
                    coinbtn.config(command='')

                if bathp < 100 and bathp >= 80:
                    buttonbath.config(image=imgbath80)
                elif bathp < 80 and bathp >= 50:
                    buttonbath.config(image=imgbath50)
                elif bathp < 50 and bathp >= 20:
                    buttonbath.config(image=imgbath20)
                elif bathp < 20:
                    button.destroy()
                    messagebox7 = tkinter.messagebox.showinfo('Котик ушел',
                                                              'К сожалению, вы не заботились о котенке, '
                                                              'и он ушел. Видимо,'
                                                              ' вам еще слишком рано заводить питомцев.')
                    buttongame.config(command='')
                    buttonsleep.config(command='')
                    buttongame.config(command='')
                    buttoneat.config(command='')
                    coinbtn.config(command='')

                if gamep < 100 and gamep >= 80:
                    buttongame.config(image=imggame80)
                elif gamep < 80 and gamep >= 50:
                    buttongame.config(image=imggame50)
                elif gamep < 50 and gamep >= 20:
                    buttongame.config(image=imggame20)

                elif gamep < 20:
                    button.destroy()
                    messagebox8 = tkinter.messagebox.showinfo('Котик ушел',
                                                              'К сожалению, вы не заботились о котенке, '
                                                              'и он ушел. Видимо, вам еще слишком рано'
                                                              ' заводить питомцев.')
                    buttongame.config(command='')
                    buttonsleep.config(command='')
                    buttongame.config(command='')
                    buttoneat.config(command='')
                    coinbtn.config(command='')
                    coinbtn.config(command='')
                def slept():
                    global sleepp
                    global eatp
                    global bathp
                    global gamep
                    button.config(image=image1)
                    sleepb.config(image=bedimg)
                    buttonsleep.config(image=imgsleep100)
                    buttonsleep.config(command=sleeppp)
                    buttoneat.config(command=kitchen)
                    buttongame.config(command=gameroom)
                    buttonbath.config(command=bath1)
                    coinbtn.config(command=coinsound)
                    shopbutton.config(command=shopcommand)
                    closetc.config(command=closetopening)
                    sleepb.config(command=sleeping)
                window.after(bsm, slept)
            sleepb = Button(window, bg='#DDA0DD', relief='flat', image=bedimg, command=sleeping)
            sleepb.place(x=800, y=250)
            closetc = Button(window, bg='#DDA0DD', relief='flat', image=closet1)
            closetc.place(x=300, y=200)

            def closetopening():
                closetc.config(image = closet2)
                p = pygame.mixer.Sound('zvuk11.wav')
                p.play()
                def opened():
                    global button
                    sleep(2)
                    window9 = Toplevel(window)
                    window9.geometry('500x500')
                    window9.configure(bg='#DEB887')
                    window9.resizable(width = False, height = False)
                    closetc.config(image = closet1)

                    labelcl = Label(window9, bg='#DEB887', font=('Times New Roman', 20), text='Шкаф')
                    labelcl.pack()
                    def catthing1():
                        button.config(image = catt1)
                    def catthing2():
                        button.config(image = catt2)
                    def catthing3():
                        button.config(image = catt3)
                    def catthing4():
                        button.config(image = catt4)
                    def catthing5():
                        button.config(image = catt5)
                    def catthing6():
                        button.config(image = catt6)
                    def catthing7():
                        button.config(image = catt7)
                    if thing1 == 1:
                        hat1incloset = Button(window9, bg='#DEB887', image=thing1img, relief='flat')
                        hat1incloset.place(x = 53, y = 140)
                        hat1incloset.config(command=catthing1)
                    if thing2 == 1:
                        hat2incloset = Button(window9, bg='#DEB887', image=thing2img, relief='flat')
                        hat2incloset.place(x = 160, y = 140)
                        hat2incloset.config(command=catthing2)
                    if thing3 == 1:
                        hat3incloset = Button(window9, bg='#DEB887', image=thing3img, relief='flat')
                        hat3incloset.place(x=275, y=140)
                        hat3incloset.config(command=catthing3)
                    if thing4 == 1:
                        hat4incloset = Button(window9, bg='#DEB887', image=thing4img, relief='flat')
                        hat4incloset.place(x=395, y=140)
                        hat4incloset.config(command=catthing4)
                    if thing5 == 1:
                        hat5incloset = Button(window9, bg='#DEB887', image=thing5img, relief='flat')
                        hat5incloset.place(x=53, y=290)
                        hat5incloset.config(command=catthing7)
                    if thing6 == 1:
                        hat6incloset = Button(window9, bg='#DEB887', image=thing6img, relief='flat')
                        hat6incloset.place(x=175, y=290)
                        hat6incloset.config(command=catthing5)
                    if thing7 == 1:
                        hat7incloset = Button(window9, bg='#DEB887', image=thing7img, relief='flat')
                        hat7incloset.place(x=295, y=290)
                        hat7incloset.config(command=catthing6)

                    window9.mainloop()
                window.after(100, opened)
            closetc.config(command=closetopening)

        def kitchen():
            p = pygame.mixer.Sound('zvuk11.wav')
            p.play()


            fridgebutton = Button(window, image=fridge, bg='#DDA0DD', relief='flat')
            fridgebutton.place(x = 300, y = 200)

            def fridgeopened():
                global eatp
                p = pygame.mixer.Sound('zvuk11.wav')
                p.play()

                window11 = Toplevel(window)
                window11.configure(background = '#FFFFF0')
                window11.geometry('900x600')
                window11.resizable(width = False, height = False)

                labelfridge = Label(window11, bg='#FFFFF0', font=('Times New Roman', 20), text = 'Холодильник')
                labelfridge.pack()

                def tablepic1():
                    tablebutton.config(image = tablefood1)
                    def tablebtnfood1():
                        global eatp
                        tablebutton.config(image = table)
                        if eatp == 100:
                            eatp += 0
                        elif eatp < 100:
                            eatp += 5
                    tablebutton.config(command=tablebtnfood1)
                def tablepic2():
                    tablebutton.config(image=tablefood2)
                    def tablebtnfood2():
                        global eatp
                        tablebutton.config(image = table)
                        if eatp == 100:
                            eatp += 0
                        elif eatp < 100:
                            eatp += 15
                    tablebutton.config(command = tablebtnfood2)
                def tablepic3():
                    tablebutton.config(image = tablefood3)
                    def tablebtnfood3():
                        global eatp
                        tablebutton.config(image = table)
                        if eatp == 100:
                            eatp += 0
                        elif eatp < 100:
                            eatp += 15
                    tablebutton.config(command = tablebtnfood3)
                def tablepic4():
                    tablebutton.config(image = tablefood4)
                    def tablebtnfood4():
                        global eatp
                        tablebutton.config(image = table)
                        if eatp == 100:
                            eatp += 0
                        elif eatp < 100:
                            eatp += 15
                    tablebutton.config(command = tablebtnfood4)
                def tablepic5():
                    tablebutton.config(image = tablefood5)
                    def tablebtnfood5():
                        global eatp
                        tablebutton.config(image = table)
                        if eatp == 100:
                            eatp += 0
                        elif eatp < 100:
                            eatp += 2
                    tablebutton.config(command = tablebtnfood5)
                def tablepic6():
                    tablebutton.config(image = tablefood6)
                    def tablebtnfood6():
                        global eatp
                        tablebutton.config(image = table)
                        if eatp == 100:
                            eatp += 0
                        elif eatp < 100:
                            eatp += 3
                    tablebutton.config(command = tablebtnfood6)
                def tablepic7():
                    tablebutton.config(image = tablefood7)
                    def tablebtnfood7():
                        global eatp
                        tablebutton.config(image = table)
                        if eatp == 100:
                            eatp += 0
                        elif eatp < 100:
                            eatp += 10
                    tablebutton.config(command = tablebtnfood7)
                def tablepic8():
                    tablebutton.config(image = tablefood8)
                    def tablebtnfood8():
                        global eatp
                        tablebutton.config(image = table)
                        if eatp == 100:
                            eatp += 0
                        elif eatp < 100:
                            eatp += 15
                    tablebutton.config(command = tablebtnfood8)
                def tablepic9():
                    tablebutton.config(image = tablefood9)
                    def tablebtnfood9():
                        global eatp
                        tablebutton.config(image = table)
                        if eatp == 100:
                            eatp += 0
                        elif eatp < 100:
                            eatp += 10
                    tablebutton.config(command = tablebtnfood9)
                def tablepic10():
                    tablebutton.config(image = tablefood10)
                    def tablebtnfood10():
                        global eatp
                        tablebutton.config(image = table)
                        if eatp == 100:
                            eatp += 0
                        elif eatp < 100:
                            eatp += 25
                    tablebutton.config(command = tablebtnfood10)
                def tablepic11():
                    tablebutton.config(image = tablefood11)
                    def tablebtnfood11():
                        global eatp
                        tablebutton.config(image = table)
                        if eatp == 100:
                            eatp += 0
                        elif eatp < 100:
                            eatp += 15
                    tablebutton.config(command = tablebtnfood11)
                def tablepic12():
                    tablebutton.config(image = tablefood12)
                    def tablebtnfood12():
                        global eatp
                        tablebutton.config(image = table)
                        if eatp == 100:
                            eatp += 0
                        elif eatp < 100:
                            eatp += 20
                    tablebutton.config(command = tablebtnfood12)
                def tablepic13():
                    tablebutton.config(image = tablefood13)
                    def tablebtnfood13():
                        global eatp
                        tablebutton.config(image = table)
                        if eatp == 100:
                            eatp += 0
                        elif eatp < 100:
                            eatp += 3
                    tablebutton.config(command = tablebtnfood13)

                if eatp < 100 and eatp >= 80:
                    buttoneat.config(image=imgfood80)
                elif eatp < 80 and eatp >= 50:
                    buttoneat.config(image=imgfood50)
                elif eatp < 50 and eatp >= 20:
                    button.config(image=imgs)
                    buttoneat.config(image=imgfood20)

                elif eatp < 20:
                    button.destroy()
                    messagebox5 = tkinter.messagebox.showinfo('Котик ушел',
                                                              'К сожалению, вы не заботились о котенке, '
                                                              'и он ушел. Видимо вам еще слишком рано заводить питомцев.')
                    buttongame.config(command='')
                    buttonsleep.config(command='')
                    buttongame.config(command='')
                    buttoneat.config(command='')
                    coinbtn.config(command='')
                if eat1 == 1:
                    food1infridge = Button(window11, bg='#FFFFF0', image=food1, relief='flat')
                    food1infridge.place(x=20, y=30)
                    food1infridge.config(command = tablepic1)
                if eat2 == 1:
                    food2infridge = Button(window11, bg='#FFFFF0', image=food2, relief='flat')
                    food2infridge.place(x=160, y=140)
                    food2infridge.config(command=tablepic2)
                if eat3 == 1:
                    food3infridge = Button(window11, bg='#FFFFF0', image=food3, relief='flat')
                    food3infridge.place(x=265, y=140)
                    food3infridge.config(command=tablepic3)
                if eat4 == 1:
                    food4infridge = Button(window11, bg='#FFFFF0', image=food4, relief='flat')
                    food4infridge.place(x=375, y=140)
                    food4infridge.config(command=tablepic4)
                if eat5 == 1:
                    food5infridge = Button(window11, bg='#FFFFF0', image=food5, relief='flat')
                    food5infridge.place(x=53, y=300)
                    food5infridge.config(command=tablepic5)
                if eat6 == 1:
                    food6infridge = Button(window11, bg='#FFFFF0', image=food6, relief='flat')
                    food6infridge.place(x=175, y=300)
                    food6infridge.config(command=tablepic6)
                if eat7 == 1:
                    food7infridge = Button(window11, bg='#FFFFF0', image=food7, relief='flat')
                    food7infridge.place(x=280, y=300)
                    food7infridge.config(command=tablepic7)
                if eat8 == 1:
                    food8infridge = Button(window11, bg='#FFFFF0', image=food8, relief='flat')
                    food8infridge.place(x=405, y=300)
                    food8infridge.config(command=tablepic8)
                if eat9 == 1:
                    food9infridge = Button(window11, bg='#FFFFF0', image=food9, relief='flat')
                    food9infridge.place(x=53, y=440)
                    food9infridge.config(command=tablepic9)
                if eat10 == 1:
                    food10infridge = Button(window11, bg='#FFFFF0', image=food10, relief='flat')
                    food10infridge.place(x=175, y=440)
                    food10infridge.config(command=tablepic10)
                if eat11 == 1:
                    food11infridge = Button(window11, bg='#FFFFF0', image=food11, relief='flat')
                    food11infridge.place(x=295, y=440)
                    food11infridge.config(command=tablepic11)
                if eat12 == 1:
                    food12infridge = Button(window11, bg='#FFFFF0', image=food12, relief='flat')
                    food12infridge.place(x=415, y=440)
                    food12infridge.config(command=tablepic12)
                if eat13 == 1:
                    food13infridge = Button(window11, bg='#FFFFF0', image=food13, relief='flat')
                    food13infridge.place(x=535, y=440)
                    food13infridge.config(command=tablepic13)

                window11.mainloop()
            fridgebutton.config(command=fridgeopened)

            tablebutton = Button(window, image=table, bg='#DDA0DD', relief='flat')
            tablebutton.place(x = 800, y = 250)

        buttoneat.config(command=kitchen)

        shopbutton = Button(window, image=shopimg, bg='#DDA0DD', relief='flat')
        shopbutton.place(x=1270, y=150)


        def shopcommand():
            window7 = Toplevel(window)
            window7.configure(bg='#98FB98')
            window7.geometry('600x600')
            window7.resizable(width=False, height=False)
            clothshopbutton = Button(window7, image=clothshopimg, relief='flat', bg='#98FB98')
            clothshopbutton.place(x = 30, y = 120)
            foodshopbutton = Button(window7, image=shopfood, bg='#98FB98', relief='flat')
            foodshopbutton.place(x = 255, y = 30)

            def foodsh():
                global coins
                global price1
                global price2
                global price10
                global price5
                global price25
                global price80
                global price100
                global eat1
                global eat2
                global eat3
                global eat4
                global eat5
                global eat6
                global eat7
                global eat8
                global eat9
                global eat10
                global eat11
                global eat12
                global eat13

                window10 = Toplevel(window7)
                window10.configure(bg='#FFE4E1')
                window10.geometry('900x600')
                window10.resizable(width=False, height=False)

                shoplabel1 = Label(window10, bg='#FFE4E1', font=('Times New Roman', 20), text='Продуктовый магазин')
                shoplabel1.pack()

                food1button = Button(window10, bg='#FFE4E1', image=food1, relief='flat')
                food1label = Label(window10, bg='#FFE4E1', font=('Times New Roman', 20), text=price25)
                food1label.place(x=53, y=140)

                food2button = Button(window10, bg='#FFE4E1', image=food2, relief='flat')
                food2label = Label(window10, bg='#FFE4E1', font=('Times New Roman', 20), text=price1)
                food2label.place(x=160, y=140)

                food3button = Button(window10, bg='#FFE4E1', image=food3, relief='flat')
                food3label = Label(window10, bg='#FFE4E1', font=('Times New Roman', 20), text=price1)
                food3label.place(x=265, y=140)

                food4button = Button(window10, bg='#FFE4E1', image=food4, relief='flat')
                food4label = Label(window10, bg='#FFE4E1', font=('Times New Roman', 20), text=price1)
                food4label.place(x=375, y=140)

                food5button = Button(window10, bg='#FFE4E1', image=food5, relief='flat')
                food5label = Label(window10, bg='#FFE4E1', font=('Times New Roman', 20), text=price2)
                food5label.place(x=53, y=300)

                food6button = Button(window10, bg='#FFE4E1', image=food6, relief='flat')
                food6label = Label(window10, bg='#FFE4E1', font=('Times New Roman', 20), text=price5)
                food6label.place(x=175, y=300)

                food7button = Button(window10, bg='#FFE4E1', image=food7, relief='flat')
                food7label = Label(window10, bg='#FFE4E1', font=('Times New Roman', 20), text=price25)
                food7label.place(x=280, y=300)

                food8button = Button(window10, bg='#FFE4E1', image=food8, relief='flat')
                food8label = Label(window10, bg='#FFE4E1', font=('Times New Roman', 20), text=price25)
                food8label.place(x=405, y=300)

                food9button = Button(window10, bg='#FFE4E1', image=food9, relief='flat')
                food9label = Label(window10, bg='#FFE4E1', font=('Times New Roman', 20), text=price10)
                food9label.place(x=53, y=440)

                food10button = Button(window10, bg='#FFE4E1', image=food10, relief='flat')
                food10label = Label(window10, bg='#FFE4E1', font=('Times New Roman', 20), text=price100)
                food10label.place(x=175, y=440)

                food11button = Button(window10, bg='#FFE4E1', image=food11, relief='flat')
                food11label = Label(window10, bg='#FFE4E1', font=('Times New Roman', 20), text=price5)
                food11label.place(x=295, y=440)

                food12button = Button(window10, bg='#FFE4E1', image=food12, relief='flat')
                food12label = Label(window10, bg='#FFE4E1', font=('Times New Roman', 20), text=price80)
                food12label.place(x=415, y=440)

                food13button = Button(window10, bg='#FFE4E1', image=food13, relief='flat')
                food13label = Label(window10, bg='#FFE4E1', font=('Times New Roman', 20), text=price10)
                food13label.place(x=535, y=440)

                def dish1():
                    global eat1
                    global coins
                    coins -= price25
                    labelcoin.config(text=coins)
                    eat1 = 1
                    food1button.destroy()
                    food1label.destroy()

                def dish2():
                    global eat2
                    global coins
                    coins -= price1
                    labelcoin.config(text=coins)
                    eat2 = 1
                    food2button.destroy()
                    food2label.destroy()
                def dish3():
                    global eat3
                    global coins
                    coins -= price1
                    labelcoin.config(text=coins)
                    eat3 = 1
                    food3button.destroy()
                    food3label.destroy()
                def dish4():
                    global eat4
                    global coins
                    coins -= price1
                    labelcoin.config(text=coins)
                    eat4 = 1
                    food4button.destroy()
                    food4label.destroy()
                def dish5():
                    global eat5
                    global coins
                    coins -= price2
                    labelcoin.config(text=coins)
                    eat5 = 1
                    food5button.destroy()
                    food5label.destroy()
                def dish6():
                    global eat6
                    global coins
                    coins -= price5
                    labelcoin.config(text=coins)
                    eat6 = 1
                    food6button.destroy()
                    food6label.destroy()
                def dish7():
                    global eat7
                    global coins
                    coins -= price25
                    labelcoin.config(text=coins)
                    eat7 = 1
                    food7button.destroy()
                    food7label.destroy()
                def dish8():
                    global eat8
                    global coins
                    coins -= price25
                    labelcoin.config(text=coins)
                    eat8 = 1
                    food8button.destroy()
                    food8label.destroy()
                def dish9():
                    global eat9
                    global coins
                    coins -= price10
                    labelcoin.config(text=coins)
                    eat9 = 1
                    food9button.destroy()
                    food9label.destroy()
                def dish10():
                    global eat10
                    global coins
                    coins -= price100
                    labelcoin.config(text=coins)
                    eat10 = 1
                    food10button.destroy()
                    food10label.destroy()
                def dish11():
                    global eat11
                    global coins
                    coins -= price5
                    labelcoin.config(text=coins)
                    eat11 = 1
                    food11button.destroy()
                    food11label.destroy()
                def dish12():
                    global eat12
                    global coins
                    coins -= price80
                    labelcoin.config(text=coins)
                    eat12 = 1
                    food12button.destroy()
                    food12label.destroy()
                def dish13():
                    global eat13
                    global coins
                    coins -= price10
                    labelcoin.config(text=coins)
                    eat13 = 1
                    food13button.destroy()
                    food13label.destroy()


                if coins >= price25:
                    food1button.config(command=dish1)
                    food1button.place(x=20, y=30)
                elif coins < price25:
                    food1button.config(command='', image = nofood1)
                    food1button.place(x=20, y=30)

                if coins >= price1:
                    food2button.config(command=dish2)
                    food2button.place(x=130, y=30)
                elif coins < price1:
                    food2button.config(command='', image=nofood2)
                    food2button.place(x=130, y=30)

                if coins >= price1:
                    food3button.config(command=dish3)
                    food3button.place(x=240, y=30)
                elif coins < price1:
                    food3button.config(command='', image=nofood3)
                    food3button.place(x=240, y=30)
                    
                if coins >= price1:
                    food4button.config(command=dish4)
                    food4button.place(x=350, y=30)
                elif coins < price1:
                    food4button.config(command='', image=nofood4)
                    food4button.place(x=350, y=30)

                if coins >= price2:
                    food5button.config(command=dish5)
                    food5button.place(x=20, y=190)
                elif coins < price2:
                    food5button.config(command='', image=nofood5)
                    food5button.place(x=20, y=190)

                if coins >= price5:
                    food6button.config(command=dish6)
                    food6button.place(x=140, y=190)
                elif coins < price5:
                    food6button.config(command='', image = nofood6)
                    food6button.place(x=140, y=190)

                if coins >= price25:
                    food7button.config(command=dish7)
                    food7button.place(x=260, y=190)
                elif coins < price25:
                    food7button.config(command='', image=nofood7)
                    food7button.place(x=260, y=190)

                if coins >= price25:
                    food8button.config(command=dish8)
                    food8button.place(x=380, y=190)
                elif coins < price25:
                    food8button.config(command='', image=nofood8)
                    food8button.place(x=380, y=190)

                if coins >= price10:
                    food9button.config(command=dish9)
                    food9button.place(x=25, y=350)
                elif coins < price10:
                    food9button.config(command='', image=nofood9)
                    food9button.place(x=25, y=350)

                if coins >= price100:
                    food10button.config(command=dish10)
                    food10button.place(x=150, y=350)
                elif coins < price100:
                    food10button.config(command='', image = nofood10)
                    food10button.place(x=150, y=350)

                if coins >= price5:
                    food11button.config(command=dish11)
                    food11button.place(x=270, y=350)
                elif coins < price5:
                    food11button.config(command='', image=nofood11)
                    food11button.place(x=270, y=350)

                if coins >= price80:
                    food12button.config(command=dish12)
                    food12button.place(x=390, y=350)
                elif coins < price80:
                    food12button.config(command='', image=nofood12)
                    food12button.place(x=390, y=350)

                if coins >= price10:
                    food13button.config(command=dish13)
                    food13button.place(x=510, y=350)
                elif coins < price10:
                    food13button.config(command='', image = nofood13)
                    food13button.place(x=510, y=350)


                window10.mainloop()
            foodshopbutton.config(command=foodsh)

            def clothsh():
                global coins
                global thing1
                global thing2
                global thing3
                global thing4
                global thing5
                global thing6
                global thing7
                window8 = Toplevel(window7)
                window8.configure(bg='#DEB887')
                window8.geometry('900x600')
                window8.resizable(width=False, height=False)

                shoplabel = Label(window8, bg='#DEB887', font=('Times New Roman', 20), text='Магазин одежды')
                shoplabel.pack()

                thing1button = Button(window8, bg='#DEB887', image=thing1img, relief='flat')
                thing1label = Label(window8, bg='#DEB887', font=('Times New Roman', 20), text=price1)
                thing1label.place(x = 53, y = 140)

                thing2button = Button(window8, bg='#DEB887', image=thing2img, relief='flat')
                thing2label = Label(window8, bg='#DEB887', font=('Times New Roman', 20), text=price1)
                thing2label.place(x = 160, y = 140)

                thing3button = Button(window8, bg='#DEB887', image=thing3img, relief='flat')
                thing3label = Label(window8, bg='#DEB887', font=('Times New Roman', 20), text=price1)
                thing3label.place(x=275, y=140)

                thing4button = Button(window8, bg='#DEB887', image=thing4img, relief='flat')
                thing4label = Label(window8, bg='#DEB887', font=('Times New Roman', 20), text=price1)
                thing4label.place(x=395, y=140)

                thing5button = Button(window8, bg='#DEB887', image=thing5img, relief='flat')
                thing5label = Label(window8, bg='#DEB887', font=('Times New Roman', 20), text=price1)
                thing5label.place(x=53, y=290)

                thing6button = Button(window8, bg='#DEB887', image=thing6img, relief='flat')
                thing6label = Label(window8, bg='#DEB887', font=('Times New Roman', 20), text=price1)
                thing6label.place(x=175, y=290)

                thing7button = Button(window8, bg='#DEB887', image=thing7img, relief='flat')
                thing7label = Label(window8, bg='#DEB887', font=('Times New Roman', 20), text=price1)
                thing7label.place(x=295, y=290)

                def hatbtn1():
                    global thing1
                    global coins
                    coins -= price1
                    labelcoin.config(text=coins)
                    thing1 = 1
                    thing1button.destroy()
                    thing1label.destroy()

                def hatbtn2():
                    global thing2
                    global coins
                    coins -= price1
                    labelcoin.config(text=coins)
                    thing2 = 1
                    thing2button.destroy()
                    thing2label.destroy()
                def hatbtn3():
                    global thing3
                    global coins
                    coins -= price1
                    labelcoin.config(text=coins)
                    thing3 = 1
                    thing3button.destroy()
                    thing3label.destroy()
                def hatbtn4():
                    global thing4
                    global coins
                    coins -= price1
                    labelcoin.config(text=coins)
                    thing4 = 1
                    thing4button.destroy()
                    thing4label.destroy()
                def hatbtn5():
                    global thing5
                    global coins
                    coins -= price1
                    labelcoin.config(text=coins)
                    thing5 = 1
                    thing5button.destroy()
                    thing5label.destroy()
                def hatbtn6():
                    global thing6
                    global coins
                    coins -= price1
                    labelcoin.config(text=coins)
                    thing6 = 1
                    thing6button.destroy()
                    thing6label.destroy()
                def hatbtn7():
                    global thing7
                    global coins
                    coins -= price1
                    labelcoin.config(text=coins)
                    thing7 = 1
                    thing7button.destroy()
                    thing7label.destroy()

                if coins >= price1:
                    thing1button.config(command=hatbtn1)
                    thing1button.place(x=20, y=30)

                    thing2button.config(command=hatbtn2)
                    thing2button.place(x=130, y=30)

                    thing3button.config(command=hatbtn3)
                    thing3button.place(x=240, y=30)

                    thing4button.config(command=hatbtn4)
                    thing4button.place(x=350, y=30)

                    thing5button.config(command=hatbtn5)
                    thing5button.place(x=20, y=180)

                    thing6button.config(command=hatbtn6)
                    thing6button.place(x=140, y=180)

                    thing7button.config(command=hatbtn7)
                    thing7button.place(x=260, y=180)
                elif coins < price1:
                    thing1button.config(command='', image = nohat1)
                    thing1button.place(x=20, y=30)

                    thing2button.config(command='', image=nohat2)
                    thing2button.place(x=130, y=30)

                    thing3button.config(command='', image=nohat3)
                    thing3button.place(x=240, y=30)

                    thing4button.config(command='', image = noglasses)
                    thing4button.place(x=350, y=30)

                    thing5button.config(command='', image = not1)
                    thing5button.place(x=20, y=180)

                    thing6button.config(command='', image = not2)
                    thing6button.place(x=140, y=180)

                    thing7button.config(command='', image = not3)
                    thing7button.place(x=260, y=180)







                window8.mainloop()

            clothshopbutton.config(command=clothsh)
            window7.mainloop()

        shopbutton.config(command=shopcommand)
        buttonsleep.config(command=sleeppp)


        def bath1():
            p = pygame.mixer.Sound('zvuk11.wav')
            p.play()

            bathh = Button(window, bg='#DDA0DD', relief='flat', image=bathimg)
            sinkl = Label(window, bg='#DDA0DD', image=mirrors)
            sinkl.place(x = 300, y = 200)


            def wash():
                global sleepp
                global eatp
                global bathp
                global gamep
                b = 100 - bathp

                if bathp == 100:
                    bathp += 0
                elif bathp < 100:
                    bathp += b
                    gamep += 10
                    sleepp -= 2

                if sleepp < 100 and sleepp >= 80:
                    buttonsleep.config(image=imgsleep80)
                elif sleepp < 80 and sleepp >= 50:
                    buttonsleep.config(image=imgsleep50)
                elif sleepp < 50 and sleepp >= 20:
                    button.config(image=imgs)
                    buttonsleep.config(image=imgsleep20)

                elif sleepp < 20:
                    button.destroy()
                    messagebox1 = tkinter.messagebox.showinfo('Котик ушел',
                                                              'К сожалению, вы не заботились о котенке, '
                                                              'и он ушел. Видимо вам еще слишком рано заводить питомцев.')
                    buttongame.config(command='')
                    buttonsleep.config(command='')
                    buttongame.config(command='')
                    buttoneat.config(command='')
                    coinbtn.config(command='')



                if bathp < 100 and bathp >= 80:
                    buttonbath.config(image=imgbath80)
                elif bathp < 80 and bathp >= 50:
                    buttonbath.config(image=imgbath50)
                elif bathp < 50 and bathp >= 20:
                    button.config(image=imgd)
                    buttonbath.config(image=imgbath20)

                elif bathp < 20:
                    button.destroy()
                    messagebox7 = tkinter.messagebox.showinfo('Котик ушел',
                                                              'К сожалению, вы не заботились о котенке, '
                                                              'и он ушел. Видимо вам еще слишком рано заводить питомцев.')
                    buttongame.config(command='')
                    buttonsleep.config(command='')
                    buttongame.config(command='')
                    buttoneat.config(command='')
                    coinbtn.config(command='')

                if gamep < 100 and gamep >= 80:
                    buttongame.config(image=imggame80)
                elif gamep < 80 and gamep >= 50:
                    buttongame.config(image=imggame50)
                elif gamep < 50 and gamep >= 20:
                    button.config(image=imgs)
                    buttongame.config(image=imggame20)

                elif gamep < 20:
                    button.destroy()
                    messagebox8 = tkinter.messagebox.showinfo('Котик ушел',
                                                              'К сожалению, вы не заботились о котенке, '
                                                              'и он ушел. Видимо вам еще слишком рано'
                                                              ' заводить питомцев.')
                    buttongame.config(command='')
                    buttonsleep.config(command='')
                    buttongame.config(command='')
                    buttoneat.config(command='')
                    coinbtn.config(command='')
                def washed():
                    button.config(image=image1)
                    bathh.config(image=bathimg)
                    buttonbath.configure(image=imgbath100)

                bp = pygame.mixer.Sound('zvuki-puzyirey-sborka-32564 (mp3cut.net).wav')
                bp.play()
                bathh.config(image=bathcat)
                button.config(image='')
                window.after(5000, washed)
            bathh.config(command=wash)
            bathh.place(x = 800, y = 250)


        buttonbath.configure(command=bath1)


        labelcoin = Button(window, bg = '#DDA0DD', text = coins, font=('Times New Roman', 20), fg='black', relief='flat')
        labelcoin.place(x = 80, y = 10)






        window4.destroy()
    window4.title('Tamagotchi')
    window4.after(300, dwn)
    dwn = Label(window4, bg='#DDA0DD', font=('Times New Roman', 25), text='Загрузка...')
    dwn.place(y = 225, x = 615)
    l = Label(window4, bg='#DDA0DD', image=catl)
    l.place(x = 615, y = 280)
    window4.mainloop()

def btnexit():
    p = pygame.mixer.Sound('zvuk11.wav')
    p.play()
    messagebox = tkinter.messagebox.askquestion('Выход', 'Вы точно хотите выйти?', icon='error')
    if messagebox == 'yes':
        window.destroy()

def btnabout():
    p = pygame.mixer.Sound('zvuk11.wav')
    p.play()
    window3 = Toplevel(window)
    window3.geometry('700x500')
    window3.resizable(height=False, width=False)
    window3.configure(bg='#DDA0DD')
    label2 = Label(window3, text='Пока вы шли домой с работы, '
                                 'вы увидели огромную кучу '
                                 'коробок, из \nкоторых доносился '
                                 'тихий писк. Недолго думая, '
                                 'вы открыли коробку и \nувидели '
                                 'маленького белого котенка, '
                                 'который плакал, свернувшись '
                                 'в     \nклубочек. Вы сразу '
                                 'же взяли котенка на руки и '
                                 'положили в свою куртку, \nчтобы '
                                 'согреть, а затем '
                                 'продолжили идти домой. '
                                 'Что же теперь будет с \nкотенком? '
                                 'Сможете ли вы '
                                 'заботиться о нем?                            '
                                 '                  ', font=('Times New Roman', 16), fg='black', bg='#DDA0DD',
                   justify = 'left')
    label2.pack()
    label3 = Label(window3, bg='#DDA0DD', image=catgif)
    label3.place(x = 275, y = 290)
    window3.mainloop()



buttonplay.config(command=btnplay)
buttonabout.config(command=btnabout)
buttonexit.config(command=btnexit)

window.mainloop()