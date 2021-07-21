#multilevel inheritance

class dad:
    basketball=1
class son(dad):
    dance=1
    def isdance(self):
           return f"yes i dance{self.dance} no of times"
class grandson(son):
    dance=6
    def isdance(self):
        return f"jackson yeah!" \
              f"yes i dance very awesome {self.dance} no. of time"
darry=dad()
larry=son()
harry=grandson()
print(harry.basketball)