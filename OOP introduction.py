class Character():
    #Public CharacterName : STRING
    #Public Colour : STRING
    def __init__(self, CharacterName,Colour, SuperStrength, Fly, Invisible):
        self.CharacterName = CharacterName
        self.Colour = Colour
        self.SuperStrength = SuperStrength
        self.Fly = Fly
        self.Invisible = Invisible



    def GetCharacterName(self):
        return self.CharacterName

    def GetColour(self):
        return self.Colour

    def GetSuperStrength(self):
        return self.SuperStrength

    def GetFly(self):
        return self.Fly

    def GetInvisible(self):
        return self.Invisible

name = input()
colour = input()
strength = input()
fly = input()
invisible = input()
char1 = Character(name,colour,strength,fly,invisible)
print(char1.GetCharacterName())