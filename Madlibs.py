#import module
from tkinter import *

#initialize window
root = Tk()
root.geometry('300x300')
root.title('Pavan-Mad Libs Generator')
Label(root, text='Mad Libs Generator \n Have Fun!', font='arial 20 bold').pack()
Label(root, text='Click Any One :', font='arial 15 bold').place(x=40, y=80)




def madlib1():
    animals = input("Enter a name of animal =")
    profession = input("Enter a profession name: ")
    cloth = input("Enter a piece of cloths name: ")
    things = input("Enter a thing name: ")
    name = input("Enter a name: ")
    place = input("Enter a place name: ")
    verb = input("Enter a verb in ing form: ")
    food = input("Enter a food name: ")

    print('say "'+food+'", the photographer said as camera flashes! ' + name + 'and i had gone to ' + place +' to get our photos taken today. The first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession + ' . When we saw the second photo, it was exactly what i had in mind')


def madlib2():
    adjective = input('enter adjective : ')
    color = input('enter a color name : ')
    thing = input('enter a thing name : ')
    place = input('enter a place name : ')
    person = input('enter a person name : ')
    adjactive1 = input('enter a adjective : ')
    insect = input('enter a insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb name : ')

    print('Last night i dreamed i was a ' + adjective + ' butterfly with ' + color + ' splocthes that looked like ' + thing +' .I flew to ' + place + ' with my bestfriend and ' + person + 'who was a ' + adjactive1 + ' ' + insect + ' . we ate stone ' + food + ' when we got there and then decide to ' + verb + ' and the dream ended when i said-- lets ' + verb + '.')



def madlib3():
    person = input('enter person name : ')
    color = input('enter color : ')
    foods = input('enter food name : ')
    adjective = input('enter aa adjective name : ')
    thing = input('enter a thing name : ')
    place = input('enter place : ')
    verb = input('enter verb : ')
    adverb = input('enter adverb : ')
    food = input('enter food name : ')
    things = input('enter a thing name : ')

    print('Today we picked apple from ' + person + "'s Orchard. I had no idea there were so many differnt varities of apples. I ate " + color + 'apples that looked like a ' + thing + ' .When our bag were full, we went on a free hay ride to ' + place + 'and back. It ended at a hay pile where we got to ' + verb + ' ' + adverb + '. I can hardly wait to get home and cook with the apples ' + food + ' and ' + things + 'pies!.')


##BUTTONS##
Button(root, text='The Photographer', font='arial 15', command=madlib1, bg='ghost white').place(x=60, y=120)
Button(root, text='apple and apple', font='arial 15', command=madlib3, bg='ghost white').place(x=70, y=180)
Button(root, text='The Butterfly', font='arial 15', command=madlib2, bg='ghost white').place(x=80, y=240)

root.mainloop()
