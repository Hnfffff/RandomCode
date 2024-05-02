from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

import sys

Wood = 1
Brick = 1
Ore = 1
Wool = 1
Wheat = 1

Scores = []




class Main(QMainWindow):


    def AddWood(self):
        global Wood
        Wood += 1
        self.Woodtext.setText(f"{Wood}")

    def RemoveWood(self):
        global Wood
        Wood -= 1
        self.Woodtext.setText(f"{Wood}")

    def AddBrick(self):
        global Brick
        Brick += 1
        self.Bricktext.setText(f"{Brick}")

    def RemoveBrick(self):
        global Brick
        Brick -= 1
        self.Bricktext.setText(f"{Brick}")

    def AddOre(self):
        global Ore
        Ore += 1
        self.oretext.setText(f"{Ore}")

    def RemoveOre(self):
        global Ore
        Ore -=1
        self.oretext.setText(f"{Ore}")

    def AddWheat(self):
        global Wheat
        Wheat += 1
        self.Wheattext.setText(f"{Wheat}")

    def RemoveWheat(self):
        global Wheat
        Wheat -= 1
        self.Wheattext.setText(f"{Wheat}")

    def AddWool(self):
        global Wool
        Wool +=1
        self.Wooltext.setText(f"{Wool}")

    def RemoveWool(self):
        global Wool
        Wool -=1
        self.Wooltext.setText(f"{Wool}")

    def Road(self):
        global Brick
        global Wood
        if Wood >= 1 and Brick >= 1:
            Wood -= 1
            Brick -= 1
            self.Woodtext.setText(f"{Wood}")
            self.Bricktext.setText(f"{Brick}")
        else:
            pass

    def Settlement(self):
        global Brick
        global Wood
        global Wool
        global Wheat
        if Brick >= 1 and Wood >= 1 and Wool >= 1 and Wheat >= 1:
            Brick -= 1
            Wood -= 1
            Wool -= 1
            Wheat -= 1
            self.Woodtext.setText(f"{Wood}")
            self.Bricktext.setText(f"{Brick}")
            self.Wooltext.setText(f"{Wool}")
            self.Wheattext.setText(f"{Wheat}")
        else:
            pass

    def City(self):
        global Wheat
        global Ore
        if Wheat >= 2 and Ore >= 3:
            Wheat -= 2
            Ore -= 3
            self.Wheattext.setText(f"{Wheat}")
            self.oretext.setText(f"{Ore}")
        else:
            pass

    def DevelopmentCard(self):
        global Wheat
        global Ore
        global Wool
        if Wheat >= 1 and Ore >= 1 and Wool >= 1:
            Wheat -= 1
            Ore -= 1
            Wool -= 1
            self.Wheattext.setText(f"{Wheat}")
            self.oretext.setText(f"{Ore}")
            self.Wooltext.setText(f"{Wool}")
        else:
            pass

    def Save(self):
        global Wood
        global Wool
        global Brick
        global Ore
        global Wheat

        with open('save.txt', 'w') as f:
            f.write(f"{Wood}")
            f.write('\n')
            f.write(f"{Wool}")
            f.write('\n')
            f.write(f"{Brick}")
            f.write('\n')
            f.write(f"{Ore}")
            f.write('\n')
            f.write(f"{Wheat}")
            f.write('\n')

    def load(self):
        global Wood
        global Wool
        global Brick
        global Ore
        global Wheat
        global Scores

        with open('save.txt', 'r') as f:
            while True:
                line = f.read().splitlines()
                if not line:
                    break
                print(line)
                Scores = line

        Wood = int(Scores[0])
        self.Woodtext.setText(f"{Wood}")
        Wool = int(Scores[1])
        self.Wooltext.setText(f"{Wool}")
        Brick = int(Scores[2])
        self.Bricktext.setText(f"{Brick}")
        Ore = int(Scores[3])
        self.oretext.setText(f"{Ore}")
        Wheat = int(Scores[4])
        self.Wheattext.setText(f"{Wheat}")


    def __init__(self):
        super().__init__()

        #Setup
        self.acceptDrops()
        self.setWindowTitle("Catan Resource Manager")
        self.setGeometry(0,0,1070, 750)

        self.title = QLabel("""Catan Resource Manager""", self)
        self.title.move(150, 10)
        self.title.setStyleSheet("""
                font-size: 70px;
        """)
        self.title.adjustSize()

        #Wood Image
        self.woodlabel = QLabel(self)
        self.woodpixmap = QPixmap('wood.png')
        self.woodlabel.setPixmap(self.woodpixmap)
        self.woodlabel.move(10, 100)
        self.woodlabel.resize(self.woodpixmap.width(), self.woodpixmap.height())

        #Wood Text
        self.Woodtext = QLabel(f"{Wood}", self)
        self.Woodtext.move(96, 300)
        self.Woodtext.setStyleSheet("""
                font-size: 20px;
                """)

        #Wood Buttons
        #Add
        buttonWoodadd = QPushButton("+", self)
        buttonWoodadd.setGeometry(20, 20, 30, 30)
        buttonWoodadd.clicked.connect(lambda:self.AddWood())
        buttonWoodadd.move(30, 300)
        buttonWoodadd.setStyleSheet("""
                        font-size: 11px;
                        """)

        #Subtract
        buttonWoodremove = QPushButton("-", self)
        buttonWoodremove.setGeometry(20, 20, 30, 30)
        buttonWoodremove.clicked.connect(lambda: self.RemoveWood())
        buttonWoodremove.move(150, 300)
        buttonWoodremove.setStyleSheet("""
                                font-size: 11px;
                                """)

        #Wool Image
        self.woollabel = QLabel(self)
        self.woolpixmap = QPixmap('wool.png')
        self.woollabel.setPixmap(self.woolpixmap)
        self.woollabel.move(225, 100)
        self.woollabel.resize(self.woolpixmap.width(), self.woolpixmap.height())

        #Wool Text
        self.Wooltext = QLabel(f"{Wool}", self)
        self.Wooltext.move(310, 300)
        self.Wooltext.setStyleSheet("""
                font-size: 20px;
                """)

        #Wool Buttons
        #Add
        buttonWooladd = QPushButton("+", self)
        buttonWooladd.setGeometry(20, 20, 30, 30)
        buttonWooladd.clicked.connect(lambda:self.AddWool())
        buttonWooladd.move(240, 300)
        buttonWooladd.setStyleSheet("""
                        font-size: 11px;
                        """)

        #Subtract
        buttonWoolremove = QPushButton("-", self)
        buttonWoolremove.setGeometry(20, 20, 30, 30)
        buttonWoolremove.clicked.connect(lambda: self.RemoveWool())
        buttonWoolremove.move(360, 300)
        buttonWoolremove.setStyleSheet("""
                                font-size: 11px;
                                """)

        #Brick Image
        self.bricklabel = QLabel(self)
        self.brickpixmap = QPixmap('brick.png')
        self.bricklabel.setPixmap(self.brickpixmap)
        self.bricklabel.move(440, 100)
        self.bricklabel.resize(self.brickpixmap.width(), self.brickpixmap.height())

        #Brick Text
        self.Bricktext = QLabel(f"{Brick}",self)
        self.Bricktext.move(530,300)
        self.Bricktext.setStyleSheet("""
                font-size: 20px;
        """)

        #Brick Buttons
        #Add
        buttonBrickadd = QPushButton("+", self)
        buttonBrickadd.setGeometry(20, 20, 30, 30)
        buttonBrickadd.clicked.connect(lambda: self.AddBrick())
        buttonBrickadd.move(460, 300)
        buttonBrickadd.setStyleSheet("""
                        font-size: 11px;
                        """)

        #Subtract
        buttonBrickremove = QPushButton("-", self)
        buttonBrickremove.setGeometry(20, 20, 30, 30)
        buttonBrickremove.clicked.connect(lambda: self.RemoveBrick())
        buttonBrickremove.move(580, 300)
        buttonBrickremove.setStyleSheet("""
                                font-size: 11px;
                                """)

        #Ore Image
        self.orelabel = QLabel(self)
        self.orepixmap = QPixmap('ore.png')
        self.orelabel.setPixmap(self.orepixmap)
        self.orelabel.move(650, 100)
        self.orelabel.resize(self.orepixmap.width(), self.orepixmap.height())

        #Ore Text
        self.oretext = QLabel(f"{Ore}", self)
        self.oretext.move(740, 300)
        self.oretext.setStyleSheet("""
                        font-size: 20px;
                """)

        #Ore Buttons
        #Add
        buttonOreadd = QPushButton("+", self)
        buttonOreadd.setGeometry(20, 20, 30, 30)
        buttonOreadd.clicked.connect(lambda: self.AddOre())
        buttonOreadd.move(670, 300)
        buttonOreadd.setStyleSheet("""
                        font-size: 11px;
                        """)

        #Subtract
        buttonOreremove = QPushButton("-", self)
        buttonOreremove.setGeometry(20, 20, 30, 30)
        buttonOreremove.clicked.connect(lambda: self.RemoveOre())
        buttonOreremove.move(790, 300)
        buttonOreremove.setStyleSheet("""
                                font-size: 11px;
                                """)


        #Wheat Image
        self.wheatlabel = QLabel(self)
        self.wheatpixmap = QPixmap('wheat.png')
        self.wheatlabel.setPixmap(self.wheatpixmap)
        self.wheatlabel.move(860, 100)
        self.wheatlabel.resize(self.wheatpixmap.width(), self.wheatpixmap.height())

        #Wheat Text
        self.Wheattext = QLabel(f"{Brick}", self)
        self.Wheattext.move(950, 300)
        self.Wheattext.setStyleSheet("""
                        font-size: 20px;
                """)

        # Ore Buttons
        # Add
        buttonWheatadd = QPushButton("+", self)
        buttonWheatadd.setGeometry(20, 20, 30, 30)
        buttonWheatadd.clicked.connect(lambda: self.AddWheat())
        buttonWheatadd.move(880, 300)
        buttonWheatadd.setStyleSheet("""
                           font-size: 11px;
                           """)

        # Subtract
        buttonWheatremove = QPushButton("-", self)
        buttonWheatremove.setGeometry(20, 20, 30, 30)
        buttonWheatremove.clicked.connect(lambda: self.RemoveWheat())
        buttonWheatremove.move(1000, 300)
        buttonWheatremove.setStyleSheet("""
                                   font-size: 11px;
                                   """)

        #Build Buttons
        #Road
        buttonRoad = QPushButton("Build Road", self)
        buttonRoad.setGeometry(20,20,150,40)
        buttonRoad.clicked.connect(lambda: self.Road())
        buttonRoad.move(10, 400)
        buttonRoad.setStyleSheet("""
                font-size: 24px;
        """)

        #Settlement
        buttonSettlement = QPushButton("Build Settlement", self)
        buttonSettlement.setGeometry(20,20, 200, 40)
        buttonSettlement.clicked.connect(lambda: self.Settlement())
        buttonSettlement.move(180, 400)
        buttonSettlement.setStyleSheet("""
                font-size: 24px;
        """)

        #City
        buttonCity = QPushButton("Build City", self)
        buttonCity.setGeometry(20,20,150,40)
        buttonCity.clicked.connect(lambda: self.City())
        buttonCity.move(400, 400)
        buttonCity.setStyleSheet("""
                font-size: 24px;
        """)

        #Development Card
        buttonDevelopment = QPushButton("Buy Development Card", self)
        buttonDevelopment.setGeometry(20,20,270,40)
        buttonDevelopment.clicked.connect(lambda: self.DevelopmentCard())
        buttonDevelopment.move(560, 400)
        buttonDevelopment.setStyleSheet("""
                font-size: 24px;
        """)

        #Save
        buttonSave = QPushButton("Save", self)
        buttonSave.setGeometry(20,20,270,40)
        buttonSave.clicked.connect(lambda: self.Save())
        buttonSave.move(560, 500)
        buttonSave.setStyleSheet("""
                font-size: 24px;
        """)

        #Load
        buttonSave = QPushButton("Load", self)
        buttonSave.setGeometry(20,20,270,40)
        buttonSave.clicked.connect(lambda: self.load())
        buttonSave.move(260, 500)
        buttonSave.setStyleSheet("""
                font-size: 24px;
        """)

        self.show()

app = QApplication(sys.argv)

window = Main()

sys.exit(app.exec())