'''
Nicholas Cali

I pledge my honor that I have abided by the Stevens Honor System

'''



# nim template DNaumann (2018), for assignment nim_hw11.txt 

# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)


def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    
    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:

            print('Congratulations you have won')

            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:

           print('Sorry the computer has won')

           break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles

    num_piles = (int(input('How many piles would you like....')))

    if num_piles <= 0:
        return init_piles()
    piles= [0] * num_piles

    for x in range(num_piles):
        print("How many in pile" + str(x))
        y = int(input())
        while y <= 0:
            print('How many in pile' + str(x))
            y = int(input())
        piles[x] = y   
    
def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles

    x = 0
    while x < int(num_piles):
        print("pile" + str(x) + ':' + str(piles[x]))
        x+=1
  
def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles


    i = int(input("What pile do you want?"))
    while i < 0 or i >= num_piles or piles[i] <= 0:
        i = int(input("Please choose a different pile"))
    choose = i
    return choose
        
def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles

    y = int(input("How many?"))
    while y <= 0 or y >=piles[pnum]:
        y = int(input('How many?'))
    return y
    

def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles 

    xor = 0
    for x in piles:
        xor ^= x
    return xor

def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles
    pileSums = []
    for n in piles:
        pileSums += [n^game_nim_sum()]
    for a in range(len(pileSums)):
        if pileSums[a] < piles[a]:
            h = a
            x = (piles[a] - pileSums[a])
            return (h,x)
    for y in range(len(piles)):
        if piles[y] != 0:
            h = y
            x = 1
            return (h,x)


def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles

    y = opt_play()
    piles[y[0]] = piles[y[0]] - y[1]

    print("I removed " + str(y[1]) + " from pile " + str (y[0]))

    


#   start playing automatically
if __name__ == "__main__" : play_nim()
