class Cookie:
    def __init__(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

cookieOne = Cookie('green')
cookieTwo = Cookie('blue')

print("Cooke One is", cookieOne.getColor())
print("Cooke Two is", cookieTwo.getColor())

print("Cooke One is", cookieOne.color)
print("Cooke Two is", cookieTwo.color)

cookieOne.setColor("yellow")

print("Cooke One is", cookieOne.color)
print("Cooke Two is", cookieTwo.color)
