
class Library:
    def __init__(self,list,name):
        self.BookList=list
        self.name=name
        self.lend={}
    def displayBook(self):
        print(f"We have following boooks: {self.name}")
        for book in self.BookList:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lend.keys():
            self.lend.update({book:user})
            print("Database has been updated. Now you can take book.")
        else:
            print(f"Book is already being taken by {self.lend[book]}")
              
    def addBook (self,book):
        self.BookList.append(book)
        print("Book has been added to the book list")

        
    def returnBook(self,book):
        self.lend.pop(book)
if __name__=='__main__':
    Vishal=Library(['Python','Rich Dad Poor Dad','Psychology of Money','Concept of Physics','Godan'],"Central Library")

    while(True):
        print(f"Welcome to the {Vishal.name}.Enter your Choice to Continue")
        print("1. Display a Book")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice=int(input())

        if user_choice==1:
            Vishal.displayBook()

        elif user_choice==2:
            book=input("Enter the book You want to Lend:")
            user=input("Enter your name :")
            Vishal.lendBook(user,book)
        elif user_choice==3:
            book=input("Enter the book you want to add:")
            Vishal.addBook(book)
        elif user_choice==4:
            book=input("Enter the book you want to return:")
        
            Vishal.returnBook(book)
        else:
            print("Not a valid option")

        print('Press q to quit and c to continue')

        user_choice2=""
        while(user_choice2!='q' and user_choice2!='c'):
            user_choice2=input()
            if user_choice2=='q':
                exit()
            elif user_choice2=='c':
                continue
        
        

        
