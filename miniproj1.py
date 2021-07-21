# creating a library class
class Library():
   def __init__(self,list,name):
       self.bookslist=list
       self.name=name
       self.lendDict={}

   def displaybooks(self):
       print("we have following books in our library: {self.name}")
       for book in self.bookslist:
           print(book)
   def lendbooks(self,user,book):
       if book not in self.lendDict.keys():
           self.lendDict.update({book:user})
           print("the library datbase has been updated you can take the book.")
       else:
           print(f"the book  is used by {self.lendDict[book]}")
   def addbooks(self,book):
       self.bookslist.append(book)
       print("the book has been added to the list{self.booklist}")
   def returnbooks(self,book):
       self.bookslist.remove(book)
       print("the book has been added to the list{self.booklist}")
if __name__=='__main__':
    harry= Library(["harry potter","python","1984","da vinci","little women"],"codewithharry")


    while (True):
        print(f"welcome to {harry.name} library enter your choice to continue")
        print("1. To display books")
        print("2. To lend books")
        print("3. To add books")
        print("4. To return books")
        user_choice=int(input())
        if user_choice==1:
            harry.displaybooks()

        elif  user_choice==2:
            harry.displaybooks()
            book=input("Enter the book you you want to lend:")
            user=input("enter your name")
            harry.lendbooks(user,book)
        elif user_choice==3:
            book=input("enter the book you want to add:")
            harry.addbooks(book)

        elif user_choice==4:
            book = input("enter the book you want to return:")
            harry.returnbooks(book)
        else :
            print("this is not vslid")


        print("press q to quit and c to continue")
        user_choice2=""
        user_choice2=input()
        while (user_choice2 != "c" and user_choice2 != "q"):
            if user_choice2=="q" :
                exit()
            elif user_choice2 =="c":
                   continue