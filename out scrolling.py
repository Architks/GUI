from Tkinter import *
import time

print "If you have less than 33 people, you can just press enter"

Person_1 = raw_input("Who is the 1st person?")
Person_2 = raw_input("Who is the 2nd person?")
Person_3 = raw_input("Who is the 3rd person?")
Person_4 = raw_input("Who is the 4th person?")
Person_5 = raw_input("Who is the 5th person?")
Person_6 = raw_input("Who is the 6th person?")
Person_7 = raw_input("Who is the 7th person?")
Person_8 = raw_input("Who is the 8th person?")
Person_9 = raw_input("Who is the 9th person?")
Person_10 = raw_input("Who is the 10th person?")
Person_11 = raw_input("Who is the 11th person?")
Person_12 = raw_input("Who is the 12th person?")
Person_13 = raw_input("Who is the 13th person?")
Person_14 = raw_input("Who is the 14th person?")
Person_15 = raw_input("Who is the 15th person?")
Person_16 = raw_input("Who is the 16th person?")
Person_17 = raw_input("Who is the 17th person?")
Person_18 = raw_input("Who is the 18th person?")
Person_19 = raw_input("Who is the 19th person?")
Person_20 = raw_input("Who is the 20th person?")
Person_21 = raw_input("Who is the 21st person?")
Person_22 = raw_input("Who is the 22nd person?")
Person_23 = raw_input("Who is the 23rd person?")
Person_24 = raw_input("Who is the 24th person?")
Person_25 = raw_input("Who is the 25th person?")
Person_26 = raw_input("Who is the 26th person?")
Person_27 = raw_input("Who is the 27th person?")
Person_28 = raw_input("Who is the 28th person?")
Person_29 = raw_input("Who is the 29th person?")
Person_30 = raw_input("Who is the 30th person?")
Person_31 = raw_input("Who is the 31st person?")
Person_32 = raw_input("Who is the 32nd person?")
Person_33 = raw_input("Who is the 33rd person?")


starting = raw_input("start? (s to start)")
if starting == "s":
  start = time.time()
elif starting != "s":
  starting = raw_input("start? (s to start)")
  if starting == "s":
      start = time.time()

laps_1 = [0]
laps_2 = [0]
laps_3 = [0]
laps_4 = [0]
laps_5 = [0]
laps_6 = [0]
laps_7 = [0]
laps_8 = [0]
laps_9 = [0]
laps_10 = [0]
laps_11 = [0]
laps_12 = [0]
laps_13 = [0]
laps_14 = [0]
laps_15 = [0]
laps_16 = [0]
laps_17 = [0]
laps_18 = [0]
laps_19 = [0]
laps_20 = [0]
laps_21 = [0]
laps_22 = [0]
laps_23 = [0]
laps_24 = [0]
laps_25 = [0]
laps_26 = [0]
laps_27 = [0]
laps_28 = [0]
laps_29 = [0]
laps_30 = [0]
laps_31 = [0]
laps_32 = [0]
laps_33 = [0]


gui = Tk()
gui.geometry("200x200")
gui.title("lapping")


def end():
  end = time.time()
  elapsed = end - start
  print "%s seconds" % elapsed


def first_person():
  print "_________________________"
  print Person_1
  end()
  laps_1[0] += 1
  print "%s has run %s laps" % (Person_1, laps_1)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button1 = Button(gui, command=first_person, text="Lap %s" % Person_1)
button1.grid()
button1.pack()


def second_person():
  print "_________________________"
  print Person_2
  end()
  laps_2[0] += 1
  print "%s has run %s laps" % (Person_2, laps_2)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)


button2 = Button(gui, command=second_person, text="Lap %s" % Person_2)
button2.grid()
button2.pack()


def third_person():
  print "_________________________"
  print Person_3
  end()
  laps_3[0] += 1
  print "%s has run %s laps" % (Person_3, laps_3)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button3 = Button(gui, command=third_person, text="Lap %s" % Person_3)
button3.grid()
button3.pack()


def fourth_person():
  print "_________________________"
  print Person_4
  end()
  laps_4[0] += 1
  print "%s has run %s laps" % (Person_4, laps_4)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button4 = Button(gui, command=fourth_person, text="Lap %s" % Person_4)
button4.grid()
button4.pack()


def fifth_person():
  print "_________________________"
  print Person_5
  end()
  laps_5[0] += 1
  print "%s has run %s laps" % (Person_5, laps_5)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button5 = Button(gui, command=fifth_person, text="Lap %s" % Person_5)
button5.grid()
button5.pack()

def sixth_person():
  print "_________________________"
  print Person_6
  end()
  laps_6[0] += 1
  print "%s has run %s laps" % (Person_6, laps_6)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button6 = Button(gui, command=sixth_person, text="Lap %s" % Person_6)
button6.grid()
button6.pack()

def seventh_person():
  print "_________________________"
  print Person_7
  end()
  laps_7[0] += 1
  print "%s has run %s laps" % (Person_7, laps_7)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button7 = Button(gui, command=seventh_person, text="Lap %s" % Person_7)
button7.grid()
button7.pack()

def eigth_person():
  print "_________________________"
  print Person_8
  end()
  laps_8[0] += 1
  print "%s has run %s laps" % (Person_8, laps_8)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button8 = Button(gui, command=eigth_person, text="Lap %s" % Person_8)
button8.grid()
button8.pack()

def ninth_person():
  print "_________________________"
  print Person_9
  end()
  laps_9[0] += 1
  print "%s has run %s laps" % (Person_9, laps_9)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button9 = Button(gui, command=ninth_person, text="Lap %s" % Person_9)
button9.grid()
button9.pack()

def tenth_person():
  print "_________________________"
  print Person_10
  end()
  laps_10[0] += 1
  print "%s has run %s laps" % (Person_10, laps_10)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button10 = Button(gui, command=tenth_person, text="Lap %s" % Person_10)
button10.grid()
button10.pack()

def eleventh_person():
  print "_________________________"
  print Person_11
  end()
  laps_11[0] += 1
  print "%s has run %s laps" % (Person_11, laps_11)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button11 = Button(gui, command=eleventh_person, text="Lap %s" % Person_11)
button11.grid()
button11.pack()

def twelfth_person():
  print "_________________________"
  print Person_12
  end()
  laps_12[0] += 1
  print "%s has run %s laps" % (Person_12, laps_12)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button12 = Button(gui, command=twelfth_person, text="Lap %s" % Person_12)
button12.grid()
button12.pack()

def thirteenth_person():
  print "_________________________"
  print Person_13
  end()
  laps_13[0] += 1
  print "%s has run %s laps" % (Person_13, laps_13)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button13 = Button(gui, command=thirteenth_person, text="Lap %s" % Person_13)
button13.grid()
button13.pack()

def fourteenth_person():
  print "_________________________"
  print Person_14
  end()
  laps_14[0] += 1
  print "%s has run %s laps" % (Person_14, laps_14)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button14 = Button(gui, command=fourteenth_person, text="Lap %s" % Person_14)
button14.grid()
button14.pack()

def fifteenth_person():
  print "_________________________"
  print Person_15
  end()
  laps_15[0] += 1
  print "%s has run %s laps" % (Person_15, laps_15)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button15 = Button(gui, command=fifteenth_person, text="Lap %s" % Person_15)
button15.grid()
button15.pack()

def sixteenth_person():
  print "_________________________"
  print Person_16
  end()
  laps_16[0] += 1
  print "%s has run %s laps" % (Person_16, laps_16)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button16 = Button(gui, command=sixteenth_person, text="Lap %s" % Person_16)
button16.grid()
button16.pack()

def seventeenth_person():
  print "_________________________"
  print Person_17
  end()
  laps_17[0] += 1
  print "%s has run %s laps" % (Person_17, laps_17)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button17 = Button(gui, command=seventeenth_person, text="Lap %s" % Person_17)
button17.grid()
button17.pack()

def eighteenth_person():
  print "_________________________"
  print Person_18
  end()
  laps_18[0] += 1
  print "%s has run %s laps" % (Person_15, laps_15)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button18 = Button(gui, command=eighteenth_person, text="Lap %s" % Person_18)
button18.grid()
button18.pack()

def nineteen_person():
  print "_________________________"
  print Person_19
  end()
  laps_19[0] += 1
  print "%s has run %s laps" % (Person_19, laps_19)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button19 = Button(gui, command=nineteen_person, text="Lap %s" % Person_19)
button19.grid()
button19.pack()

def twenty_person():
  print "_________________________"
  print Person_20
  end()
  laps_20[0] += 1
  print "%s has run %s laps" % (Person_20, laps_20)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button20 = Button(gui, command=twenty_person, text="Lap %s" % Person_20)
button20.grid()
button20.pack()

def twentyone_person():
  print "_________________________"
  print Person_21
  end()
  laps_21[0] += 1
  print "%s has run %s laps" % (Person_21, laps_21)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button21 = Button(gui, command=twentyone_person, text="Lap %s" % Person_21)
button21.grid()
button21.pack()

def p22_person():
  print "_________________________"
  print Person_23
  end()
  laps_22[0] += 1
  print "%s has run %s laps" % (Person_22, laps_22)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button22 = Button(gui, command=p22_person, text="Lap %s" % Person_22)
button22.grid()
button22.pack()

def p23_person():
  print "_________________________"
  print Person_23
  end()
  laps_23[0] += 1
  print "%s has run %s laps" % (Person_23, laps_23)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button23 = Button(gui, command=p23_person, text="Lap %s" % Person_23)
button23.grid()
button23.pack()

def p24_person():
  print "_________________________"
  print Person_24
  end()
  laps_24[0] += 1
  print "%s has run %s laps" % (Person_24, laps_24)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button24 = Button(gui, command=p24_person, text="Lap %s" % Person_24)
button24.grid()
button24.pack()

def p25_person():
  print "_________________________"
  print Person_25
  end()
  laps_25[0] += 1
  print "%s has run %s laps" % (Person_25, laps_25)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button25 = Button(gui, command=p25_person, text="Lap %s" % Person_25)
button25.grid()
button25.pack()

def p26_person():
  print "_________________________"
  print Person_26
  end()
  laps_26[0] += 1
  print "%s has run %s laps" % (Person_26, laps_26)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button26 = Button(gui, command=fifteenth_person, text="Lap %s" % Person_26)
button26.grid()
button26.pack()

def p27_person():
  print "_________________________"
  print Person_27
  end()
  laps_27[0] += 1
  print "%s has run %s laps" % (Person_27, laps_27)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button27 = Button(gui, command=p27_person, text="Lap %s" % Person_27)
button27.grid()
button27.pack()

def p28_person():
  print "_________________________"
  print Person_28
  end()
  laps_28[0] += 1
  print "%s has run %s laps" % (Person_28, laps_28)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button28 = Button(gui, command=fifteenth_person, text="Lap %s" % Person_28)
button28.grid()
button28.pack()

def p29_person():
  print "_________________________"
  print Person_29
  end()
  laps_29[0] += 1
  print "%s has run %s laps" % (Person_29, laps_29)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button29 = Button(gui, command=fifteenth_person, text="Lap %s" % Person_29)
button29.grid()
button29.pack()

def p30_person():
  print "_________________________"
  print Person_30
  end()
  laps_30[0] += 1
  print "%s has run %s laps" % (Person_30, laps_30)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button30 = Button(gui, command=p30_person, text="Lap %s" % Person_30)
button30.grid()
button30.pack()

def p31_person():
  print "_________________________"
  print Person_31
  end()
  laps_31[0] += 1
  print "%s has run %s laps" % (Person_31, laps_31)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button31 = Button(gui, command=p31_person, text="Lap %s" % Person_31)
button31.grid()
button31.pack()

def p32_person():
  print "_________________________"
  print Person_32
  end()
  laps_32[0] += 1
  print "%s has run %s laps" % (Person_32, laps_32)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button32 = Button(gui, command=p32_person, text="Lap %s" % Person_32)
button32.grid()
button32.pack()

def p33_person():
  print "_________________________"
  print Person_33
  end()
  laps_33[0] += 1
  print "%s has run %s laps" % (Person_33, laps_33)
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

button33 = Button(gui, command=p33_person, text="Lap %s" % Person_33)
button33.grid()
button33.pack()


def finish_button():
  print "_________________________"
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_1, laps_1, Person_2, laps_2, Person_3, laps_3, Person_4, laps_4, Person_5, laps_5)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_6, laps_6, Person_7, laps_7, Person_8, laps_8, Person_9, laps_9, Person_10, laps_10)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_11, laps_11, Person_12, laps_12, Person_13, laps_13,Person_14, laps_14, Person_15, laps_15)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_16, laps_16, Person_17, laps_17, Person_18, laps_18, Person_19, laps_19, Person_20, laps_20)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_21, laps_21, Person_22, laps_22, Person_23, laps_23, Person_24, laps_24, Person_25, laps_25)
  print "%s:%s, %s:%s, %s:%s, %s:%s, %s:%s" % (Person_26, laps_26, Person_27, laps_27, Person_28, laps_28, Person_29, laps_29, Person_30, laps_30)
  print "%s:%s, %s:%s, %s:%s" % (Person_31, laps_31, Person_32, laps_32, Person_33, laps_33)

finished_button = Button(gui,command=finish_button,text="Finish")
finished_button.grid()
finished_button.pack()

gui.mainloop()








