class Customer():

    def __init__(self, id, name, pnr):
        self.id = id
        self.name = name
        self.pnr = pnr
        
    def __str__(self):
        return self.id + " " + self.name + " " + self.pnr

    def __repr__(self):
        return "{} {}".format(self.name, self.pnr)