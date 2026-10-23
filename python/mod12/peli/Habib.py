class ShbShb :
    def __init__ (self , sakhab , noom):
        self.sakhab = sakhab
        self.noom=noom

    def print_tiedot(self):
        print(f"kadesh shakhab {self.sakhab} kadesh naam {self.noom}")


    def lie_or_right (self):
        if self.sakhab > 50 :
            return f"right"
        elif self.noom > 18 :
            return f"right"
        else : 
            return f"lie "

x_on=lie_or_right()
print(x)

##huoneita 
## esineit 