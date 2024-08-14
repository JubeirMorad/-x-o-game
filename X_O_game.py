
import os 
def clear():
    os.system("cls")
class Menu:

    def start_menu(self):
        print("""Welcome  in ( X , O ) .
Press 1 to start game :
Press 2 to exit game :""")
        choice=input("")
        return choice
     
    def end_menu(self): 
        print("""Game over !!
Press 1 to restart game :
Press 2 to exit game :""")
        choice=input("")
        return choice 
class Players :
    def __init__ (self):
        self.name=""
        self.symbol=""
        self.symbollist=[]
        
    def choose_name(self):
        while True:
            name=input("Please enter your name (only letter) :")
            
            if name.isalpha()  :
                self.name=name
                break 
            else :
                print("Wrong !! please enter only LETTER :\n")
                 

    def choose_symbol(self):
        while True :
            symbol=input("Please enter your sympol ( X , O  'or other..' )").upper()
            if symbol.isalpha() and len(symbol)==1  :
                self.symbol=symbol
                break
            else:
                print("Invalid choose enter only letter please !!!")                
class Board:
    def __init__(self):
        self.board=[str(i) for i in range(1,10)]

    def update_board(self,choice,symbol):
        if self.is_valid_move(choice):
            self.board[choice-1]=symbol
            return True
        return False
    
    def is_valid_move(self,choice):
        return self.board[choice-1].isdigit()
    
    def display_board(self):
        for x in range(0,9,3):
            print(" | ".join(self.board[x:x+3]))
            if x < 6 :
                print("-"*9)
    def reset_board(self):
        self.board=[str(i) for i in range(1,10)]     
class Game :
    def __init__(self):
        self.players = [Players(),Players()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0
        self.treis = 0
        self.namelist=[]
        self.symbollist = []

    def start_game(self):
        if self.menu.start_menu() == "1" :
            clear()
            self.setup_player()
            clear()
            self.play_game()
        else :
            self.quit_game()

    def setup_player(self):       
        for i , person in enumerate(self.players,1) :
            print(f"\nPlayer {i} enter your details :")
            while True :
                person.choose_name()
                if person.name not in self.namelist :                 
                    self.namelist.append(person.name)
                    while True :
                        person.choose_symbol()
                        if person.symbol not in self.symbollist :
                            self.symbollist.append(person.symbol)
                            break
                        else :
                            print("\n!!! This symbol exist choose another symbol !!!")
                    break
                else :
                    print("\n!!! This name exist choose another name !!!")
                


    def quit_game(self):
        print("***Than you for playing .***")

    def play_game(self):
        while True :
            self.play_turn()
            if self.check_win() or self.check_drow():
                self.board.display_board()
                if self.check_win()==True :
                    if self.treis%2 ==0 :
                        print(f"**** {self.players[1].name} , IS THE WINNER ****")
                    else:
                        print(f"**** {self.players[0].name} , IS THE WINNER ****")
                    break
                if self.check_drow()==True :
                    print("**** NO WINNER ****")
                print("\nThank you for playing .\n")
                break
        
        self.end_game()
        
    def check_win(self):
        for x in range(0,9,3):
            if self.board.board[x]==self.board.board[x+1]==self.board.board[x+2] :
                return True
        for x in range(0,3):
            if self.board.board[x]==self.board.board[x+3]==self.board.board[x+6]:
                return True
        if self.board.board[0]==self.board.board[4]==self.board.board[8] or  self.board.board[2]==self.board.board[4]==self.board.board[6]:
            return True
        return False
    def check_drow(self):
        if self.treis == 9 and self.check_win() == False :
            return True
        else:
            return False
    def default_data(self):
        self.board.reset_board()
        self.treis=0
        self.current_player_index=0
        self.namelist=[]
        self.symbollist=[]

    def end_game(self):
        print("""\nPress 1 to return game :
Press 2 to restart game :
Press other key to exit game :""")
        choice = input ("")
        self.default_data()
        clear()
        if choice == "1" :
            self.play_game()
        elif choice =="2" :
            self.start_game()
        else :
            self.quit_game()
        
    
    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name} you can turn {player.symbol}")
        while True :
            try:
                choice =int(input("Choose a number from the list :")) 
                if 1 <= choice <= 9 and self.board.update_board(choice,player.symbol) :
                    break
                else :
                    print("Invalid choice try again !!!! ")
            except ValueError :
                print("Please choose number between 1 - 9 :")
        self.treis += 1
        self.current_player_index = 1 - self.current_player_index
        clear()
game = Game().start_game()



