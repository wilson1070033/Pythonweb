import random
from collections import Counter

suits=['♠','♥','♦','♣']
ranks=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
dic_ranks={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}
dic_suits={'♠':4,'♥':3,'♦':2,'♣':1}
dic_combinations={'Straight Flush':9,'Four of a kind':8,'Full house':7,'Flush':6,'Straight':5,'Three of a kind':4,'Two pairs':3,'One pair':2,'High card':1}

def create_deck():
    deck=[]
    for i in ranks:
        for j in suits:
            deck.append(j+i)
    random.shuffle(deck)
    return deck

def deal_cards(num_players,num_cards):
    hands=[]
    for i in range(num_players):
        hand=[]
        for j in range(num_cards):
            hand.append(deck.pop(0))
        hands.append(hand)
    return hands

def check_suit(player_hand, table_cards):
    all_cards=player_hand+table_cards

    suit=[]
    for card in all_cards:
      suit.append(card[0])
      f_suit,num_f_suit=Counter(suit).most_common(1)[0]
    return f_suit

def check_rank(player_hand, table_cards):
    all_cards=player_hand+table_cards

    rank=[]
    mid=0
    for card in all_cards:
      rank.append(sorted([dic_ranks[card[1:]]])[0])
    rank.sort()
    mid=rank[3]
    return mid

def check_hand(player_hand, table_cards):
    all_cards=player_hand+table_cards

    suit=[]
    rank=[]
    mid=0
    flush=0
    straight=0
    for card in all_cards:
      suit.append(card[0])
      rank.append(sorted([dic_ranks[card[1:]]])[0])
    rank.sort()
    mid=rank[3]

    c_suit=Counter(suit)
    c_rank=Counter(rank)
    f_suit,num_f_suit=c_suit.most_common(1)[0]
    if num_f_suit>=5:
      flush=1


    for i in range(len(rank)-1):
      if [mid-3,mid-2,mid-1,mid+1] in rank or [mid-2,mid-1,mid+1,mid+2] in rank or [mid-1,mid+1,mid+2,mid+3] in rank:
        straight=1

    #同花順超慢 反正幾乎不會出現
    if flush==1 and straight==1:
      sf_rank=[]
      for card in all_cards:
        if card[0]==f_suit:
          sf_rank.append(sorted([dic_ranks[card[1:]]]))
      sf_mid=sf_rank[3]
      for i in range(len(rank)-1):
        if [sf_mid-3,sf_mid-2,sf_mid-1,sf_mid+1] in sf_rank or [sf_mid-2,sf_mid-1,sf_mid+1,sf_mid+2] in sf_rank or [sf_mid-1,sf_mid+1,sf_mid+2,sf_mid+3] in sf_rank:
          return 'Straight Flush'

    if 4 in c_rank.values():
      return 'Four of a kind'

    if 3 in c_rank.values() and 2 in c_rank.values():
      return 'Full house'

    if flush==1:
      return 'Flush'

    if straight==1:
      return 'Straight'

    if 3 in c_rank.values():
      return 'Three of a kind'

    pairs=[rank for rank,count in c_rank.items() if count==2]
    if len(pairs)>=2:
      return 'Two pairs'

    if 2 in c_rank.values():
      return 'One pair'

    return 'High card'


deck=create_deck()
num_players=int(input('玩家人數:'))
num_table_cards=5 #有空加入下注系統改2
table_cards=deal_cards(1,num_table_cards)[0]
players={}
handcard_point=[]
dic_point={}
mid=0
f_suit=''
all_players_hand=deal_cards(num_players,2)
print('tablecards are '+(' '.join(table_cards)))
for i in range(num_players):
  players['player'+str(i+1)]=all_players_hand[i]

for k,v in players.items():
  print(k+"'s handcards are "+(' ').join(v),check_hand(players[k], table_cards))


  tmpstr = str(hex(dic_combinations[check_hand(players[k], table_cards)]))[2:]+str(hex(check_rank(players[k], table_cards)))[2:]+str(hex(dic_suits[check_suit(players[k], table_cards)]))[2:]
  point=(int(tmpstr,16))
  dic_point[point]=k
winner=dic_point[max(dic_point.keys())]

print('winner is '+winner+', '+check_hand(players[winner], table_cards))