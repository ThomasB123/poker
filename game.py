from pygame_functions import *
import random
import itertools

def setup():
    # 5 10 20 25 50 100
    # red pink blue purple orange brown

    Pred = makeSprite('chips/redChip.png') # 5
    Ppink = makeSprite('chips/pinkChip.png') # 10
    Pblue = makeSprite('chips/LblueChip.png') # 20
    Ppurple = makeSprite('chips/purpleChip.png') # 25
    Porange = makeSprite('chips/orangeChip.png') # 50
    Pbrown = makeSprite('chips/brownChip.png') # 100
    transformSprite(Pred,0,0.08)
    transformSprite(Ppink,0,0.08)
    transformSprite(Pblue,0,0.08)
    transformSprite(Ppurple,0,0.08)
    transformSprite(Porange,0,0.08)
    transformSprite(Pbrown,0,0.08)
    moveSprite(Pred,700,500)
    moveSprite(Ppink,750,500)
    moveSprite(Pblue,800,500)
    moveSprite(Ppurple,850,500)
    moveSprite(Porange,900,500)
    moveSprite(Pbrown,950,500)
    showSprite(Pred)
    showSprite(Ppink)
    showSprite(Pblue)
    showSprite(Ppurple)
    showSprite(Porange)
    showSprite(Pbrown)
    showLabel(makeLabel('5',20,717,550))
    showLabel(makeLabel('10',20,761,550))
    showLabel(makeLabel('20',20,812,550))
    showLabel(makeLabel('25',20,862,550))
    showLabel(makeLabel('50',20,912,550))
    showLabel(makeLabel('100',20,955,550))

    Ored = makeSprite('chips/redChip.png') # 5
    Opink = makeSprite('chips/pinkChip.png') # 10
    Oblue = makeSprite('chips/LblueChip.png') # 20
    Opurple = makeSprite('chips/purpleChip.png') # 25
    Oorange = makeSprite('chips/orangeChip.png') # 50
    Obrown = makeSprite('chips/brownChip.png') # 100
    transformSprite(Ored,0,0.08)
    transformSprite(Opink,0,0.08)
    transformSprite(Oblue,0,0.08)
    transformSprite(Opurple,0,0.08)
    transformSprite(Oorange,0,0.08)
    transformSprite(Obrown,0,0.08)
    moveSprite(Ored,700,25)
    moveSprite(Opink,750,25)
    moveSprite(Oblue,800,25)
    moveSprite(Opurple,850,25)
    moveSprite(Oorange,900,25)
    moveSprite(Obrown,950,25)
    showSprite(Ored)
    showSprite(Opink)
    showSprite(Oblue)
    showSprite(Opurple)
    showSprite(Oorange)
    showSprite(Obrown)
    showLabel(makeLabel('5',20,717,0))
    showLabel(makeLabel('10',20,761,0))
    showLabel(makeLabel('20',20,812,0))
    showLabel(makeLabel('25',20,862,0))
    showLabel(makeLabel('50',20,912,0))
    showLabel(makeLabel('100',20,955,0))

    potLabel = makeLabel(str(pot),50,850,250)
    playerLabel = makeLabel(str(playerChips),40,575,525)
    opponentLabel = makeLabel(str(opponentChips),40,575,10)
    showLabel(potLabel)
    showLabel(playerLabel)
    showLabel(opponentLabel)

    playerB = makeSprite('redCircle.png')
    opponentB = makeSprite('redCircle.png')
    transformSprite(playerB,0,0.02)
    transformSprite(opponentB,0,0.02)
    moveSprite(playerB,465,525)
    moveSprite(opponentB,465,10)
    showSprite(playerB)
    showSprite(opponentB)

    plaFold = makeSprite('fold.png')
    plaCall = makeSprite('call.png')
    plaRaise = makeSprite('raise.png')
    transformSprite(plaFold,0,0.6)
    transformSprite(plaCall,0,0.6)
    transformSprite(plaRaise,0,0.6)
    moveSprite(plaFold,0,525)
    moveSprite(plaCall,100,525)
    moveSprite(plaRaise,200,525)
    showSprite(plaFold)
    showSprite(plaCall)
    showSprite(plaRaise)

    oppFold = makeSprite('fold.png')
    oppCall = makeSprite('call.png')
    oppRaise = makeSprite('raise.png')
    transformSprite(oppFold,0,0.6)
    transformSprite(oppCall,0,0.6)
    transformSprite(oppRaise,0,0.6)
    moveSprite(oppFold,0,0)
    moveSprite(oppCall,100,0)
    moveSprite(oppRaise,200,0)
    showSprite(oppFold)
    showSprite(oppCall)
    showSprite(oppRaise)
    # 5 10 20 25 50 100
    # red pink blue purple orange brown
    Pchips = [Pred,Ppink,Pblue,Ppurple,Porange,Pbrown]
    Ochips = [Ored,Opink,Oblue,Opurple,Oorange,Obrown]
    return Pchips,Ochips,potLabel,playerLabel,opponentLabel,playerB,opponentB,plaFold,plaCall,plaRaise,oppFold,oppCall,oppRaise

#suitDict = {'C':'Clubs','D':'Diamonds','H':'Hearts','S':'Spades'}
#rankDict = {'2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten','J':'Jack','Q':'Queen','K':'King','A':'Ace'}

def createDeck():
    suits = ['C','D','H','S']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    deck = [[rank,suit] for rank in ranks for suit in suits]
    return deck

def randomiseDeck(deck):
    random.shuffle(deck)

def getHand(hand):
    numKey = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}
    def getNum(card):
        return numKey[card[0]]
    hand = sorted(hand,key=getNum)
    ranks = [numKey[x[0]] for x in hand]
    suits = [x[1] for x in hand]
    flush = False
    straight = True
    if suits[0]==suits[1]==suits[2]==suits[3]==suits[4]:
        flush = True
    for x in range(len(ranks)-1):
        if ranks[x]+1 != ranks[x+1]:
            straight = False
    # straight flush
    if straight and flush:
        return 145400 + ranks[4]
    # four of a kind
    if ranks[1]==ranks[2]==ranks[3]==ranks[4]:
        return 145200 + ranks[1]*8 + ranks[0]
    if ranks[0]==ranks[1]==ranks[2]==ranks[3]:
        return 145200 + ranks[3]*8 + ranks[4]
    # full house
    if ranks[0]==ranks[1] and ranks[2]==ranks[3]==ranks[4]:
        return 145000 + ranks[4]*8 + ranks[0]
    if ranks[0]==ranks[1]==ranks[2] and ranks[3]==ranks[4]:
        return 145000 + ranks[0]*8 + ranks[4]
    # flush
    if flush:
        return 80000 + ranks[4]*8**4 + ranks[3]*8**3 + ranks[2]*8**2 + ranks[1]*8 + ranks[0]
    # straight
    if straight:
        return 79000 + ranks[4]
    # three of a kind
    if ranks[2]==ranks[3]==ranks[4]:
        return 77000 + ranks[2]*8**2 + ranks[1]*8 + ranks[0]
    if ranks[1]==ranks[2]==ranks[3]:
        return 77000 + ranks[1]*8**2 + ranks[4]*8 + ranks[0]
    if ranks[0]==ranks[1]==ranks[2]:
        return 77000 + ranks[0]*8**2 + ranks[4]*8 + ranks[3]
    # two pair
    if ranks[1]==ranks[2] and ranks[3]==ranks[4]:
        return 75000 + ranks[4]*8**2 + ranks[2]*8 + ranks[0]
    if ranks[0]==ranks[1] and ranks[3]==ranks[4]:
        return 75000 + ranks[4]*8**2 + ranks[1]*8 + ranks[2]
    if ranks[0]==ranks[1] and ranks[2]==ranks[3]:
        return 75000 + ranks[3]*8**2 + ranks[1]*8 + ranks[4]
    # one pair
    if ranks[3]==ranks[4]:
        return 65000 + ranks[3]*8**3 + ranks[2]*8**2 + ranks[1]*8 + ranks[0]
    if ranks[2]==ranks[3]:
        return 65000 + ranks[2]*8**3 + ranks[4]*8**2 + ranks[1]*8 + ranks[0]
    if ranks[1]==ranks[2]:
        return 65000 + ranks[1]*8**3 + ranks[4]*8**2 + ranks[3]*8 + ranks[0]
    if ranks[0]==ranks[1]:
        return 65000 + ranks[0]*8**3 + ranks[4]*8**2 + ranks[3]*8 + ranks[2]
    # high card
    return ranks[4]*8**4 + ranks[3]*8**3 + ranks[2]*8**2 + ranks[1]*8 + ranks[0]

def whatHand(score):
    if score > 145400:
        return 'straight flush'
    elif score > 145200:
        return 'four of a kind'
    elif score > 145000:
        return 'full house'
    elif score > 80000:
        return 'flush'
    elif score > 79000:
        return 'straight'
    elif score > 77000:
        return 'three of a kind'
    elif score > 75000:
        return 'two pair'
    elif score > 65000:
        return 'one pair'
    else:
        return 'high card'

def showAll(x): # x is who folded, 0 for no-one (game reached end), 1 for player, 2 for opponent
    global game
    global pot
    global playerChips
    global opponentChips
    global r
    pHigh = 0
    for i in list(itertools.combinations(flop + player,5)):
        pHigh = max(pHigh,getHand(i))
    #print(pHigh)
    oHigh = 0
    for i in list(itertools.combinations(flop + opponent,5)):
        oHigh = max(oHigh,getHand(i))
    #print(oHigh)
    print('Player has {}'.format(whatHand(pHigh)))
    print('Opponent has {}'.format(whatHand(oHigh)))
    if x == 0:
        if pHigh > oHigh:
            playerChips += pot
            pot = 0
            changeLabel(potLabel,str(pot))
            changeLabel(playerLabel,str(playerChips))
            winner = makeLabel('Player Wins!',120,150,200)
        elif oHigh > pHigh:
            opponentChips += pot
            pot = 0
            changeLabel(potLabel,str(pot))
            changeLabel(opponentLabel,str(opponentChips))
            winner = makeLabel('Opponent Wins!',120,100,200)
        else:
            winner = makeLabel('It\'s a Tie!',120,250,200)
    elif x == 1:
        opponentChips += pot
        pot = 0
        changeLabel(potLabel,str(pot))
        changeLabel(opponentLabel,str(opponentChips))
        winner = makeLabel('Opponent Wins!',120,100,200)
    elif x == 2:
        playerChips += pot
        pot = 0
        changeLabel(potLabel,str(pot))
        changeLabel(playerLabel,str(playerChips))
        winner = makeLabel('Player Wins!',120,150,200)
    showLabel(winner)
    game = False
    r = 1
    return winner

def deal():
    deck = createDeck()
    randomiseDeck(deck)
    flop = deck[:5]
    player = deck[5:7]
    opponent = deck[7:9]
    f1 = makeSprite('cards/red_back.png')
    f2 = makeSprite('cards/red_back.png')
    f3 = makeSprite('cards/red_back.png')
    f4 = makeSprite('cards/red_back.png')
    f5 = makeSprite('cards/red_back.png')
    addSpriteImage(f1,'cards/' + deck[0][0]+deck[0][1] + '.png')
    addSpriteImage(f2,'cards/' + deck[1][0]+deck[1][1] + '.png')
    addSpriteImage(f3,'cards/' + deck[2][0]+deck[2][1] + '.png')
    addSpriteImage(f4,'cards/' + deck[3][0]+deck[3][1] + '.png')
    addSpriteImage(f5,'cards/' + deck[4][0]+deck[4][1] + '.png')
    transformSprite(f1,0,0.1)
    transformSprite(f2,0,0.1)
    transformSprite(f3,0,0.1)
    transformSprite(f4,0,0.1)
    transformSprite(f5,0,0.1)
    moveSprite(f1,250,230)
    moveSprite(f2,350,230)
    moveSprite(f3,450,230)
    moveSprite(f4,550,230)
    moveSprite(f5,650,230)
    showSprite(f1)
    showSprite(f2)
    showSprite(f3)
    showSprite(f4)
    showSprite(f5)
    p1 = makeSprite('cards/red_back.png')
    p2 = makeSprite('cards/red_back.png')
    addSpriteImage(p1,'cards/' + deck[5][0]+deck[5][1] + '.png')
    addSpriteImage(p2,'cards/' + deck[6][0]+deck[6][1] + '.png')
    transformSprite(p1,0,0.1)
    transformSprite(p2,0,0.1)
    moveSprite(p1,400,400)
    moveSprite(p2,500,400)
    showSprite(p1)
    showSprite(p2)
    o1 = makeSprite('cards/red_back.png')
    o2 = makeSprite('cards/red_back.png')
    addSpriteImage(o1,'cards/' + deck[7][0]+deck[7][1] + '.png')
    addSpriteImage(o2,'cards/' + deck[8][0]+deck[8][1] + '.png')
    transformSprite(o1,0,0.1)
    transformSprite(o2,0,0.1)
    moveSprite(o1,400,75)
    moveSprite(o2,500,75)
    showSprite(o1)
    showSprite(o2)
    return flop,player,opponent,f1,f2,f3,f4,f5,p1,p2,o1,o2

def play():
    global game
    global r
    global pot
    global playerChips
    global opponentChips
    # Fold, Call, Raise buttons
    # Once all called, flop, then after all called reveal 4th, then 5th, then all call then show
    game = True
    r = 1
    while game:
        if spriteClicked(plaCall) or spriteClicked(oppCall):
            if r == 1:
                nextSpriteImage(f1)
                nextSpriteImage(f2)
                nextSpriteImage(f3)
            if r == 2:
                nextSpriteImage(f4)
            if r == 3: # game reached end
                nextSpriteImage(f5)
                winner = showAll(0)
            r += 1
            allCall = False
        elif spriteClicked(playerB): # toggle player cards
            nextSpriteImage(p1)
            nextSpriteImage(p2)
        elif spriteClicked(opponentB): # toggle opponent cards
            nextSpriteImage(o1)
            nextSpriteImage(o2)
        # 5 10 20 25 50 100
        # red pink blue purple orange brown
        elif spriteClicked(Pred) and playerChips >= 5:
            pot += 5
            playerChips -= 5
        elif spriteClicked(Ppink) and playerChips >= 10:
            pot += 10
            playerChips -= 10
        elif spriteClicked(Pblue) and playerChips >= 20:
            pot += 20
            playerChips -= 20
        elif spriteClicked(Ppurple) and playerChips >= 25:
            pot += 25
            playerChips -= 25
        elif spriteClicked(Porange) and playerChips >= 50:
            pot += 50
            playerChips -= 50
        elif spriteClicked(Pbrown) and playerChips >= 100:
            pot += 100
            playerChips -= 100
        elif spriteClicked(Ored) and opponentChips >= 5:
            pot += 5
            opponentChips -= 5
        elif spriteClicked(Opink) and opponentChips >= 10:
            pot += 10
            opponentChips -= 10
        elif spriteClicked(Oblue) and opponentChips >= 20:
            pot += 20
            opponentChips -= 20
        elif spriteClicked(Opurple) and opponentChips >= 25:
            pot += 25
            opponentChips -= 25
        elif spriteClicked(Oorange) and opponentChips >= 50:
            pot += 50
            opponentChips -= 50
        elif spriteClicked(Obrown) and opponentChips >= 100:
            pot += 100
            opponentChips -= 100
        # done betting button, turn over
        elif spriteClicked(plaFold): # player folds
            winner = showAll(1)
        elif spriteClicked(oppFold): # opponent folds
            winner = showAll(2)
        changeLabel(potLabel,str(pot))
        changeLabel(playerLabel,str(playerChips))
        changeLabel(opponentLabel,str(opponentChips))
        pause(100)
    return winner

def reset():
    global r
    global pot
    r = 1
    pot = 0

if __name__ == '__main__':
    screenSize(1024,576)
    setBackgroundImage('felt.jpg')
    playerChips = 1000
    opponentChips = 1000
    pot = 0
    r = 1 # round
    game = True
    Pchips,Ochips,potLabel,playerLabel,opponentLabel,playerB,opponentB,plaFold,plaCall,plaRaise,oppFold,oppCall,oppRaise = setup()
    [Pred,Ppink,Pblue,Ppurple,Porange,Pbrown] = Pchips
    [Ored,Opink,Oblue,Opurple,Oorange,Obrown] = Ochips
    while True:

        flop,player,opponent,f1,f2,f3,f4,f5,p1,p2,o1,o2 = deal()
        winner = play()
        pause(1000)
        hideLabel(winner)
        # play again

# add instructions such as, must bet at least x amount to call or raise etc
# add button to finish turm, replace call and raise buttons
# get message if not bet enough or anything, or can't bet


endWait()