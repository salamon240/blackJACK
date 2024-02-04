import random
deler_card=[]
player_card=[]
suits=["hearts","diamonds","spades","clubs"]
cards=[2,3,4,5,6,7,8,9,10,"princ","queen","king","ace"]
deler_sum=0
player_sum=0
player_mony=100

# here we creat the dec of crads
dec_of_card=[]
for suit in suits:
    for card in cards:
        dec_of_card.append((suit,card))

# func that shuffle the card and pop out one card from the list
def shuffle_card():
    cardindex=random.randint(0,len(dec_of_card)-1)
    shafel_card=dec_of_card[cardindex]
    dec_of_card.pop(cardindex)
    return shafel_card


# func that sum all the cards  together and returen it back
def sum_card(name,card):
    sum=0
    ok=True
    for cards in card:
        print( f"{name} cards",cards[1])
        if cards[1]=="ace":
            while ok:
                try:
                    number=int(input("you have ace do you want it to rnet like 11 or like 1 ?  "))
                    print(f"you chois the number{number}")
                    ok=False
                except Exception as e:
                    print(type(e))
                
            if number==1 or number==11:
                sum+=number                 
        elif cards[-1] in ["princ","queen","king"]:
            sum+=10
        else:
            print("else card",cards[-1])
            sum+=cards[-1]
    return sum  
 
#start the game by asking the user if he want to play we cheking if he have more then 50 in his money
#and whe give 2 card to the dealer  and 2 to the player
playing=input("do you want to play blackjack yes or no? ")   
while playing=="yes"and player_mony>50:  
    for i in range(2):
        deler_card.append(shuffle_card())
        player_card.append(shuffle_card())
    
    player_sum=sum_card("player",player_card)
    deler_sum=sum_card("deler",deler_card)

    print("deler card:\t\t",deler_card,deler_sum)
    print("player card:\t\t",player_card,player_sum)

    status=False





  
#after we give the card we ask the player if he want to take anther card
    
    anser=input("do you want to take anther card?  yes or no  ")
    while anser=="yes" and player_sum<21 and player_mony>50:
        player_card=[]
        player_card.append(shuffle_card())
        player_sum+=sum_card("player",player_card)
        
        print("player card:\t\t",player_card,player_sum)
        if player_sum>21:
            print("PLAYER YOU LOSE !!")
            player_mony-=50
            status=True
            break
        anser=input(" PLAYER do u wnat to take anther card? yes or no  ")
    
    while deler_sum<17:
        deler_card=[]
        deler_card.append(shuffle_card())
        deler_sum+=sum_card("deler",deler_card)
        print("deler card:\t\t",deler_card,deler_sum)

        if deler_sum>21:
            print(" PLAYER YOU WIN!!!!")
            player_mony+=100
            status=True
            break
        anser=input(" DELERdo you wnat to take anther card? yes or no  ")

    if status==False :
        if deler_sum<player_sum:
          print(" OUT YOU WIN!!!")
          player_mony+=100
        else:
          print(" OUT YOU LOSE!!!")
          player_mony-50
    deler_card=[]
    deler_sum=0
    player_card=[]
    player_sum=0
    print(f"you have {player_mony}$")
    playing=input("do you want to  keep play yes or no? ") 