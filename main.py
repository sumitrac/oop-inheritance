class Pokemon:
  def __init__(self,name,type):
    self.name = name
    self.type = type 
    self.energy = 50
    # name
    # type
    # energy is always 50

  def status(self):
    print f"{self.name}, {self.type}, {self.energy}"
    # print out the name, the type, and how much energy the Pokemon has


  def attack(self, opponent):
    print f"{self.name}attacks {opponent.name} for 10 demage!"
    oppenent.energy -= 10 
    
    # this method should output the following:
    # "[name] attacks [opponent's name] for 10 damage!"
    # then decrease the opponent's energy by 10

  