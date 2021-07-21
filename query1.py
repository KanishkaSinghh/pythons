class room:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
tanya=room("tanya", "singh")
yash=room("yash", "singh")
print(tanya.explain())
print(dir(yash))
