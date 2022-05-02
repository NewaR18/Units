import webbrowser
import random
text='y'
print("Enter 1 for Software Engineering")
print("ENter 2 for Net Centric")
print("Enter 3 for Compiler Design")
print("Enter 4 for Technical Writing")
print("Enter 5 for E-Governance")
while(text=='y'):
    s=int(input("Enter the subject you want to study: "))
    if(s==1):
        with open("software_engineering.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
            a=int(input("Which Chapter do you want to study(Enter in number): "))
            if(a>9):
                print("There are only 9 Chapters, Please try again")
            else:
                hell=words[a-1]
                webbrowser.open(f'https://www.collegenote.net/note/CSIT/53/sixth-semester/software-engineering/{hell}/view/#gsc.tab=0')
    if(s==2):
        with open("netcentric.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
            a=int(input("Which Chapter do you want to study(Enter in number): "))
            if(a>9):
                print("There are only 9 Chapters, Please try again")
            else:
                hell=words[a-1]
                webbrowser.open(f'https://www.collegenote.net/note/CSIT/53/sixth-semester/software-engineering/{hell}/view/#gsc.tab=0')
    if(s==3):
        with open("Compiler.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
            a=int(input("Which Chapter do you want to study(Enter in number): "))
            hell=words[a-1]
            if(a==3):
                hell=words[4]
            if(a==4):
                hell=words[5]
            if(a>4):
                print("There are only 4 Chapters, Please try again")
            else:
                webbrowser.open(f'https://www.collegenote.net/note/CSIT/54/sixth-semester/complier-design-and-construction/{hell}/view/#gsc.tab=0')
    if(s==4):
        print("Notes not available for Technical Writing")
    if(s==5):
            webbrowser.open(f'https://drive.google.com/drive/folders/1lmhPiJmcYY4Bh7-lAjawWfE3Ve_DUT0x')

    text=input("Do you want to continue(y/n): ")
    
