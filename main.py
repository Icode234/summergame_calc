pl1=0
pl2=0
pl3=0
pl4=0
king=1
queen=2
police=3
theif=4
print("Hello")
cycle_count = int(input("How many cycles is this game? "))

pl1Name=input("What is your Name Player 1")
pl2Name = input("What is your Name Player 2")
pl3Name = input("What is your Name Player 3")
pl4Name = input("What is your Name Player 4")
for cycle_count in range(1,cycle_count+1):
    pl1q = int(input("Who is player 1? (1,2,3,4): "))

    pl2q = int(input("Who is player 2? (1,2,3,4): "))

    pl3q = int(input("Who is player 3? (1,2,3,4): "))

    pl4q = int(input("Who is player 4? (1,2,3,4): "))

    if pl1q==1:
        pl1+=100
    elif pl1q==2:
        pl1+=50
    elif pl1q==3:
        result=bool(input("Did the player catch the thief"))
        if result==1:
            pl1+=25
        elif result==0:
            pl1+=0
    elif pl1q==4:
        result=bool(input("Was the thief caught?"))
        if result==1:
            pl1+=0
        else:
            pl1+=25
    if pl2q==1:
        pl2+=100
    elif pl2q==2:
        pl2+=50
    elif pl2q==3:
        result=bool(input("Did the player catch the thief"))
        if result==1:
            pl2+=25
        elif result==0:
            pl2+=0
    elif pl2q==4:
        result=bool(input("Was the thief caught?"))
        if result==1:
            pl2+=0
        else:
            pl2+=25
    if pl3q==1:
        pl3+=100
    elif pl3q==2:
        pl3+=50
    elif pl3q==3:
        result=bool(input("Did the player catch the thief"))
        if result==1:
            pl3+=25
        elif result==0:
            pl3+=0
    elif pl3q==4:
        result=bool(input("Was the thief caught?"))
        if result==1:
            pl3+=0
        else:
            pl3+=25
    if pl4q == 1:
        pl4 += 100
    elif pl4q == 2:
        pl4 += 50
    elif pl4q == 3:
        result = bool(input("Did the player catch the thief"))
        if result == 1:
            pl4 += 25
        elif result == 0:
            pl4 += 0
    elif pl4q == 4:
        result = bool(input("Was the thief caught?"))
        if result ==1:
            pl4 += 0
        else:
            pl4 += 25
print("The Scores are\n",pl1Name," ",pl1," ","Pts")
print("\n",pl2Name," ",pl2," ","Pts")
print("\n",pl3Name," ",pl3," ","Pts")
print("\n",pl4Name," ",pl4," ","Pts")
highest_score=max(pl1,pl2,pl3,pl4)
if pl1 == highest_score:
    print("Player 1 has the highest score of", pl1,"and has won the match")
if pl2 == highest_score:
    print("Player 2 has the highest score of", pl2,"and has won the match")
if pl3 == highest_score:
    print("Player 3 has the highest score of", pl3,"and has won the match")
if pl4 == highest_score:
    print("Player 4 has the highest score of", pl4,"and has won the match")
print("Thanks for playing!")





