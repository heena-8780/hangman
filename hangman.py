
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random


w=Tk()
w.title("HangMan")
window=Frame(w)
window.pack()
frame=Frame(w)
frame.pack()
spet=0
word_list=["AEROPLANE", "ADMINISTRATOR", "ACTIVITY", "ADDRESS", "APPLE", "ANACONDA",
           "BALLOON", "BEAR", "BILLION", "BEAUTIFUL", "BEHAVIOR", "BUSINESS", "BUILDING",
           "CAMEL", "COBRA", "CARROT", "CHALLENGE", "CHARACTER", "CONFERENCE", "CUSTOMER", "CENTURY", "CHOICE",
           "DONKEY", "DUCK", "DEVELOPMENT", "DIRECTION", "DINNER", "DISEASE", "DOCTOR", "DREAM",
           "EAGLE", "EXPERIENCE", "EVERYTHING", "ENVIRONMENT", "ENJOY","EMPLOYEE", "EVIDENCE", "EVENING",
           "FINGER", "FINANCIAL", "FEELING", "FINISH", "FORWARD", "FUTURE", "FARMER", "FRIEND",
           "GENERATION", "GIRL", "GOAL", "GOVERNMENT", "GENERAL", "GROWTH", "GUESS",
           "HEALTH", "HEART", "HISORY", "HUMAN", "HUNDRED", "HOTEL", "HOUSE",
           "INSTITUTION", "INDIVIDUAL", "ICECREAM", "IMAGINE", "INSIDE", "INVESTMENT", "IDENTITY", "INTERNATIONAL",
           "JOB", "JOIN",
           "KNOWLEDGE", "KITCHEN", "KID", "KITE", "KIND",
           "LANGUAGE", "LAWYER", "LIGHT", "LISTEN", "LOVE", "LIFE", "LOST",
           "MACHINE", "MAGAZINE", "MAJORITY", "MOUNTAIN", "MARRIAGE", "MEDICAL", "MONEY", "MANAGEMENT", "MESSAGE", "MOMENT", "MOVEMENT", "MUSIC", "MATERIAL", "MEETING", "MINUTE", "MISSION", "MUSIC", "MOVIE",
           "NATIONAL", "NATION", "NATURAL", "NATURE", "NECESSARY", "NETWORK", "NEWSPAPER", "NOTICE", "NUMBER",
           "OPPORTUNITY", "ORGANIZATION", "OPERATION", "OUTSIDE", "OFFICER", "OFFICE", "OFFICIAL", "OWNER",
           "PERSONAL", "PHYSICAL", "PLAYER", "POLITICAL", "POLICE", "POSITIVE", "POPULATION", "POWER", "PRESSURE", "POETRY", "POSITION", "PICTURE", "PERFORMANCE", "PATIENT", "PAINT", "PAINTING", "PARTNER", "PARTICIPANT", "PARENT", "PEOPLE", "PARROT", "PROGRAM", "PROFESSOR", "PUBLIC", "PURPOSE", "PROJECT", "PRODUCTION", "PROFESSIONAL", "PROTECT",
           "QUESTION", "QUALITY", "QUANTITY", "QUICKLY", "QUITE", "QUEEN",
           "RADIO", "REALITY", "REFLECT", "RESPONSIBILITY", "RESEARCH", "RESPOND", "RELATIONSHIP", "RELIGIOUS", "REPUBLICAN", "RESOURCE",
           "SUCCESSFUL", "SUGGEST", "SUPPORT", "SUFFER", "SURFACE", "SCIENTIST", "SEASON", "SECURITY", "SCHOOL", "SCIENCE", "SECTION", "SERVICE", "SUBMISSION", "SOCIAL", "SERIOUS", "SIGNIFICANT", "SITUATION", "SOCIETY", "SOLUTION", "SIMILAR", "SISTER", "SOMETHING", "STATEMENT", "STANDARD", "STRUCTURE", "STREET", "STRATEGY", "STUDENT", "SUBJECT", "TELIVISION",
           "TEACHER", "TECHNOLOGY", "THOUSAND", "THANK", "TOGETHER", "TONIGHT", "THEORY", "TRADITIONAL", "TRAINING", "TRAVEL", "TREATMENT", "TROUBLE", "TIME", "TRIP",
           "UNDERSTAND", "USUALLY", "UMBRELLA",
           "VARIOUS", "VICTIM", "VIOLENCE", "VISIT", "VALUE", "VOICE", "VOTE",
           "WATCH", "WHATEVER", "WAIT", "WEATHER", "WILD", "WOMEN", "WORLD", "WRITER", "WINDOW", "WATER", "WONDER",
           "YOUNG", "YARD", "YOURSELF",
           "ZEBRA"]


def newgame():
    global the_word_withSpaces
    global numberOfGuesses
    global the_word
    numberOfGuesses=0
    global spet
    spet=0
    messagebox.showinfo("No_Of_Attempts", "Total Attempt is 15")
    the_word=random.choice(word_list)
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))

def getm():
    if spet==1:
        import urllib.request
        from bs4 import BeautifulSoup
        url = "https://www.vocabulary.com/dictionary/" + the_word + ""
        htmlfile = urllib.request.urlopen(url)
        soup = BeautifulSoup(htmlfile, 'lxml')
        
        soup1 = soup.find(class_="short")
        
        try:
            soup1 = soup1.get_text()
        except AttributeError:
            messagebox.showinfo('Cannot find such word! Check spelling.')
            exit()
        messagebox.showinfo("SHORT MEANING: \n\n",soup1)
    
        soup2 = soup.find(class_="long")
        soup2 = soup2.get_text()
        messagebox.showinfo("LONG MEANING: \n\n",soup2)
    else:
        messagebox.showinfo('Cannot Get Meaning','Finish all Attempts and\n try again !')
        
def guess(letter):
    global numberOfGuesses
    if numberOfGuesses!=14:
        txt=list(the_word_withSpaces)
        guessed=list(lblWord.get())
        numberOfGuesses+=1
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):
                if(txt[c]==letter):
                    guessed[c]=letter
                lblWord.set("".join(guessed))
                if lblWord.get()==the_word_withSpaces:
                    messagebox.showinfo("HangMan","YOU GUESSED WORD CORRECTLY!\nCONGRATS, YOU WON!")
                    lblWord.set(the_word_withSpaces)
                    break
        if numberOfGuesses==5:
            messagebox.showinfo("HangMan ", "ATTEMPTS COMPLETED: 5\nATTEMPTS LEFT: 10")
        elif numberOfGuesses==10:
                messagebox.showinfo("HangMan ", "ATTEMPTS COMPLETED: 10\nATTEMPTS LEFT: 5\nBE CAREFUL")
        else:
            if numberOfGuesses==12:
                        messagebox.showinfo("HangMan ", "ATTEMPTS COMPLETED: 12\nATTEMPTS LEFT: 3\nBE CAREFUL")
    else:
        messagebox.showinfo("HangMan","GAME OVER...!\nTRY NEXT TIME!!")
        global spet
        spet=1
        lblWord.set(the_word_withSpaces)
               
lblWord=StringVar()
Label(window, textvariable=lblWord, font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)

n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda d=c: guess(d), font=("Consolas 18"), width=4).grid(row=1+n//9, column=n%9)
    n+=1

Button(window, text="New\nGame", command=lambda:newgame(), font=("Helvetica 10 bold"), width=4).grid(row=3, column=8, sticky="NSWE")
newgame()

Button(frame, text="Get Meaning", command=lambda:getm(), font=("Helvetica 15 bold"),width=46).grid(row=3, column=8, sticky="NSWE")

window.mainloop()