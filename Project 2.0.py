#!/usr/bin/env python
# coding: utf-8

# # Rock, Paper & Scissors Game

# In[6]:


player1= str(input("Enter player1 name:"))
player2= str(input("Enter player2 name:"))
print("Lets play the game")
p1= str(input("{player} choose your option between rock,paper and scissors:".format(player=player1)))
p2= str(input("{player} choose your option between rock,paper and scissors:".format(player=player2)))


if(p1=="rock") and (p2=="rock"):
    print("{Player1} choose the {option1} and {Player2} choose the {option2}".format(Player1=player1,option1=p1,Player2=player2,option2=p2))
    print("That's a tie between {Player1} and {Player2}".format(Player1=player1,Player2=player2))
elif(p1=="rock") and (p2=="paper"):
    print("{Player1} choose the {option1} and {Player2} choose the {option2}".format(Player1=player1,option1=p1,Player2=player2,option2=p2))
    print("{Player2} won the game".format(Player2=player2))
elif(p1=="rock") and (p2=="scissors"):
    print("{Player1} choose the {option1} and {Player2} choose the {option2}".format(Player1=player1,option1=p1,Player2=player2,option2=p2))
    print("{Player1} won the game".format(Player1=player1))

elif(p1=="paper") and (p2=="rock"):
    print("{Player1} choose the {option1} and {Player2} choose the {option2}".format(Player1=player1,option1=p1,Player2=player2,option2=p2))
    print("{Player1} won the game".format(Player1=player1))
elif(p1=="paper") and (p2=="paper"):
    print("{Player1} choose the {option1} and {player2} choose the {option2}".format(Player1=player1,option1=p1,Player2=player2,option2=p2))
    print("That's a tie between {Player1} and {Player2}".format(Player1=player1,Player2=player2))
elif(p1=="paper") and (p2=="scissors"):
    print("{Player1} choose the {option1} and {Player2} choose the {option2}".format(Player1=player1,option1=p1,Player2=player2,option2=p2))
    print("{Player2} won the game".format(Player2=player2))

elif(p1=="scissors") and (p2=="rock"):
    print("{Player1} choose the {option1} and {Player2} choose the {option2}".format(Player1=player1,option1=p1,Player2=player2,option2=p2))
    print("{Player2} won the game".format(Player2=player2))
elif(p1=="scissors") and (p2=="paper"):
    print("{Player1} choose the {option1} and {Player2} choose the {option2}".format(Player1=player1,option1=p1,Player2=player2,option2=p2))
    print("{Player1} won the game".format(Player1=player1))
elif(p1=="scissors") and (p2=="scissors"):
    print("{Player1} choose the {option1} and {Player2} choose the {option2}".format(Player1=player1,option1=p1,Player2=player2,option2=p2))
    print("That's a tie between {Player1} and {Player2}".format(Player1=player1,Player2=player2))

else:
    print("Enter a valid option")
    


# In[ ]:





# In[ ]:




