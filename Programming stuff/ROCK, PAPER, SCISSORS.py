
#--Choices dictionary--
choices={"S": "Scissors", "P": "Paper", "R": "Rock"}


#--Game code--
p1_score=[]
p2_score=[]

for game in range(1000000): #loop whole game
    
    print("---Welcome to James' Rock, Paper, Scissors Programme!---")

    print("Player 1 Score:{0}".format(len(p1_score)))
    print("Player 2 Score:{0}".format(len(p2_score)))
    
    
    

    #Player 1 choice
    print("Player 2 look away while Player 1 chooses,")
    p1_input=input("Player 1's Choice(R/P/S):") 
    if p1_input == "S" or p1_input == "s" or p1_input =="scissors" or p1_input =="Scissors" or p1_input =="scissor" or p1_input =="Scissor":
        p1=choices["S"]
    elif p1_input == "P" or p1_input =="Paper" or p1_input =="paper" or p1_input =="p":
        p1=choices["P"]
    elif p1_input == "R" or p1_input == "rock" or p1_input == "stone" or p1_input == "r" or p1_input == "Stone":
        p1=choices["R"]
    else:
        p1="Wrong"

    for cover in range(40):
        print("THIS IS TO COVER PLAYER 1's ANSWER")
        

    #Player 2 choice
    p2_input=input("Player 2's Choice(R/P/S):") 
    if p2_input == "S" or p2_input =="s" or p2_input =="scissors" or p2_input =="Scissors" or p2_input =="scissor" or p2_input =="Scissor":
        p2=choices["S"]
    elif p2_input == "P" or p2_input == "Paper" or p2_input == "paper" or p2_input == "p":
        p2=choices["P"]
    elif p2_input == "R" or p2_input == "rock" or p2_input == "stone" or p2_input == "r" or p2_input == "Stone":
        p2=choices["R"]
    else:
        p2="Wrong"

#--Formula--
    def Game_FormulaP1(c1, c2):
        if p1 == c1 and p2 == c2:
            print("                                                 ***Player 1 Wins!***")
            p1_score.append("point")
            
    def Game_FormulaP2(c1, c2):
        if p1 == c1 and p2 == c2:
            print("                                                 ***Player 2 Wins!***")
            p2_score.append("point")

    def Game_FormulaDraw(c1, c2):
        if p1 == c1 and p2 == c2:
            print("                                                 ***It's a Draw!***")

    def Game_FormulaWrongP1():
        if p1 != "Scissors" and p1 != "Paper" and p1 != "Rock":
            print("                                     ***!!ERROR!! PLAYER 1 TYPED:{0} ***".format(p1_input))
            
    def Game_FormulaWrongP2():
        if p2 != "Scissors" and p2 != "Paper" and p2 != "Rock":
            print("                                     ***!!ERROR!! PLAYER 2 TYPED:{0} ***".format(p2_input))

#--Run game--
    Game_FormulaP1("Scissors", "Paper")
    Game_FormulaP2("Scissors", "Rock")
    Game_FormulaDraw("Scissors", "Scissors")
    Game_FormulaP2("Paper", "Scissors")
    Game_FormulaP1("Paper", "Rock")
    Game_FormulaDraw("Paper", "Paper")
    Game_FormulaP1("Rock", "Scissors")
    Game_FormulaP2("Rock", "Paper")
    Game_FormulaDraw("Rock", "Rock")
    Game_FormulaWrongP1()
    Game_FormulaWrongP2()

    


