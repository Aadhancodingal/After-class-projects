class fruit:
  def __init__(self,name,smell):
    self.name = name
    self.smell = smell
  def intro(self,name,smell):
   print("Hello, I am {} ,  I am also {}".format(self.name,self.smell))   

lemon = fruit("Lemon","sour")
strawberry =fruit("Strawberry","sweet")

lemon.intro("Lemon","sour")
strawberry.intro("Strawberry","sweet")