# Import statements
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
import sys, re

# Class for the nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

# Linked list class
class LinkedList:
    # Initialization function
    def __init__(self, nodes=None):
        self.head = None
        self.tail = None
        # Creates the linked list from the given nodes
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
        self.tail = node

    # Function to iterate through the linked list and yield the value of each node
    def iterate(self):
        node = self.head
        while node is not None:
            value = node.data
            node = node.next
            yield value

    # Function to show the linked list
    def show(self):
        l = []
        for i in self.iterate():
            l.append(i)
        return l

    # Function to return the length of the list
    def checkLen(self):
        count = 0
        for i in self.iterate():
            count += 1
        return count

    # Function to determine whether an item is in the linked lsit
    def inList(self, item):
        for i in self.iterate():
            if i == item:
                return True
        return False

    # Function to append an item to the list
    def append(self, item):
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(item)

    # Function to prepend an item to the list
    def prepend(self, item):
        temp = Node(item)
        temp.next, self.head = self.head, temp

    # Function to add an item to the list at a given index
    def insert(self,item,index):
        if index == 0:
            self.prepend(item)                          # If the given index is 0 the prepend function will be called
        elif index == self.checkLen():
            self.append(item)                           # If the given index is one more than the last index the append function will be called
        elif index < self.checkLen():
            temp = Node(item)
            node = self.head
            previous = None
            count = 0
            while count != index:                       # Loops until at the given index
                previous, node = node, node.next
                count += 1
            previous.next = temp                        # Inserts the new node in the given index
            temp.next = node

    # Function to remove an item from the list at a given index
    def remove(self,index):
        if index == 0:
            self.head = self.head.next                  # If the given index is 0 then the second item in the list will be made the first
        else:
            count = 0
            previous = None
            node = self.head
            while count != index:                       # Loops until at the given index
                previous, node = node, node.next
                count += 1
            previous.next = node.next                   # Removes the item at the given index


# Window interface class
class Window(QMainWindow):
    # Initialization function
    def __init__(self): 
        super().__init__()
        self.title = 'Linked Lists'
        self.x, self.y, self.w, self.h = 400, 300, 500, 300
        self.insert = False
        self.delete = False
        self.llist = LinkedList(['a', 'b', 'c', 'd', 'e'])
        self.initUI()

    # UI initialization function
    def initUI(self):
        # Sets the window title and size
        self.setWindowTitle(self.title) 
        self.setGeometry(self.x, self.y, self.w, self.h)

        # Creates the text on the screen
        self.l1 = QLabel('Pick a way to manipulate the following linked list', self) 
        self.l1.move(100, 10)
        self.l1.resize(300,30)

        self.l2 = QLabel('Item:', self) 
        self.l2.move(130, 95)
        self.l2.resize(300,30)
        self.l2.hide()

        self.l3 = QLabel('Index:', self) 
        self.l3.move(260, 95)
        self.l3.resize(300,30)
        self.l3.hide()

        self.l4 = QLabel(str(self.llist.show()), self)
        self.l4.setFont(QFont('Arial',30))
        self.l4.resize(500,30)
        self.l4.move(130,180)

        # Creates the input boxes
        self.t1 = QLineEdit(self)
        self.t1.move(170,100)
        self.t1.resize(50,20)
        self.t1.hide()

        self.t2 = QLineEdit(self)
        self.t2.move(300, 100)
        self.t2.resize(50,20)
        self.t2.hide()

        # Creates the buttons
        self.b1 = QPushButton('Insert', self)
        self.b1.move(180,40)
        self.b1.clicked.connect(self.showInsert)
        self.b1.resize(60,30)

        self.b2 = QPushButton('Delete', self)
        self.b2.move(270,40)
        self.b2.clicked.connect(self.showDelete)
        self.b2.resize(70,30)

        self.b3 = QPushButton('Go', self)
        self.b3.move(220,130)
        self.b3.clicked.connect(self.onClick)
        self.b3.resize(60,30)
        self.b3.hide()

        self.show()

    # Function to show the input boxes if the user selects the 'Insert' button
    def showInsert(self):
        self.delete = False
        self.insert = True
        self.l3.move(260, 95)
        self.t2.move(300, 100)
        self.l2.show()
        self.l3.show()
        self.t1.show()
        self.t2.show()
        self.b3.show()

    # Function to show the input boxes if the user selects the 'Delete' button
    def showDelete(self):
        self.insert = False
        self.delete = True
        self.l3.move(210, 95)
        self.t2.move(250, 100)
        self.l3.show()
        self.t2.show()
        self.b3.show()
        self.l2.hide()
        self.t1.hide()

    # Function called when the submit button is clicked
    def onClick(self):
        # Checks if the insert button was clicked and if the given index is valid
        if self.insert and int(self.t2.text()) <= self.llist.checkLen() and int(self.t2.text()) >= 0:
            self.llist.insert(self.t1.text(),int(self.t2.text()))                                           # Calls the insert function
            self.l4.setText(str(self.llist.show()))                                                         # Changes the displayed list
        # Checks if the delete button was clicked and if the given index is valid
        if self.delete and int(self.t2.text()) < self.llist.checkLen() and int(self.t2.text()) >= 0:
            self.llist.remove(int(self.t2.text()))                                                          # Calls the remove function
            self.l4.setText(str(self.llist.show()))                                                         # Changes the displayed list
         
# Runs the code       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
