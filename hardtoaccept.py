import random
import matplotlib.pyplot as plt

# each prisoner opens the first box corresponding to his number
# then goes to the next box with the label he found in it.
# his goal is to find his own number in one box then he stops

# global variables
rings = []
labels = []
keys_rings = []
sequences = []

def do_ring(prisoner): 
    '''
    get ring for each prisoner whose number gives the box to open first to get the label of the next box to be opened
    the lenght of the ring is the number of box he has opened to find his number
    '''
    box_to_open = prisoner-1
    # contains the box numbers which have been opened before achieving his goal
    ring = []
    for k in range(100):    
        ring.append(box_to_open+1)
        label = labels[box_to_open]
        #print(box_to_open+1,label)
        box_to_open = label - 1        
        if box_to_open == prisoner-1:
            break
        #print(ring)
    return ring,len(ring)


def round():
    global rings, key_rings, sequences
    ok = 0
    lucky_prisoners = []
    '''
    do the ring for all 100 prisoners with the random sequence obtained
    '''
    rings = []
    sequences = []
    key_rings = []
    for prisoner in range(1,101):
        #print('ring:', prisoner)
        _r, r = do_ring(prisoner)        
#         sequences.append(_r)
#         if r not in rings or r==1:
#             key_rings.append(r)
        sequences.append(_r)
        rings.append(r)    
        #print(prisoner,l)
        if r <= 50:
            lucky_prisoners.append(prisoner)
            ok += 1
    #print('result',ok)
    return ok, lucky_prisoners


def compute_stats(n=100, debug=False, only_free=False):
    global labels
    free = 0
    executed = 0
    # launch 100 sequences to get statistics
    for r in range(1,n+1):
        if debug:
            print()
        # randomize another sequence
        labels = list(range(1,101))
        random.shuffle(labels)
        
        stats, unlucky_guys = round()
        
        # if all 100 prisoners are successful, they are all free
        if stats == 100:
            free += 1
            if only_free:
                if debug:
                    print(r,'All free with max lenght=',max(rings),', min lenght=',min(rings))
                    print('Safe sequence:',labels)
                print(r,'Rings lenght',rings)
                            
        # 
        else:
            executed +=1
            if debug:
                print(r,'All executed with max lenght=',max(rings), 'min lenght=',min(rings))
                print('Rings lenght',rings)
                print('Deadly sequence:',labels)             
                print('Unfortunate guys', unlucky_guys)
        #print(rings,'max lenght=',max(rings),'min lenght=',min(rings))

    print(f"\nStatistics result : Free pct:{free*100/n:.2f}%, Execution pct:{executed*100/n:.2f}%")


def count_elements(seq) -> dict:
    """Tally elements from `seq`."""
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist

def ascii_histogram(seq) -> None:
    """A horizontal frequency-table/histogram plot."""
    counted = count_elements(seq)
    for k in sorted(counted):
        print('{0:5d} {1}'.format(k, '+' * counted[k]))
    print(counted)

def about_rings():   
#     if max(rings) <= 50:
    for r,s in zip(key_rings, sequences):
        print(r,s)
    plt.hist(rings,bins=100, color='#0504aa',alpha=0.7, rwidth=0.85)
    
    ascii_histogram(rings)
    plt.show()
    
def about_sequences():
    tags = []
    key_seqs = []
    for s in sequences:
        if s[0] not in tags:
            tags += s
            key_seqs.append(s)
    return key_seqs, len(key_seqs)

def about_labels():
    for i,l in enumerate(labels):
        print((i+1,l),end=';')
        if (i+1)%10 == 0:print()

def test():
    # this sequence is safe for the prisoners
    labels = [38, 76, 41, 29, 67, 12, 78, 77, 57, 52, 6, 83, 81, 42, 24, 63, 62, 58, 7, 13, 31, 26, 15, 89, 8, 17, 4, 92, 99, 45, 75, 30, 95, 61, 49, 70, 86, 9, 44, 97, 56, 33, 73, 88, 43, 84, 64, 19, 14, 66, 85, 72, 51, 59, 100, 28, 22, 65, 53, 48, 2, 90, 50, 34, 11, 37, 69, 23, 18, 35, 96, 16, 68, 27, 94, 46, 47, 71, 21, 36, 93, 55, 87, 82, 54, 80, 60, 40, 3, 98, 74, 25, 79, 10, 39, 1, 20, 5, 91, 32]
    print('\nThis sequence is always safe for the prisoners :')
    print(labels,round()[0])

    labels = [83, 69, 13, 12, 41, 62, 99, 34, 8, 46, 15, 90, 84, 50, 42, 67, 59, 4, 27, 7, 91, 80, 21, 45, 51, 54, 25, 5, 87, 52, 81, 61, 10, 56, 38, 16, 70, 79, 23, 93, 55, 40, 98, 43, 76, 29, 64, 22, 94, 39, 89, 14, 65, 20, 78, 60, 48, 58, 49, 72, 1, 85, 3, 31, 2, 28, 30, 96, 9, 74, 68, 88, 66, 33, 77, 53, 82, 44, 37, 35, 11, 92, 75, 95, 63, 100, 71, 17, 26, 57, 6, 36, 24, 32, 18, 47, 86, 73, 97, 19]
    print('\nThis prisoners are doomed with this sequence:')
    print(labels,round()[0])

compute_stats(True)
# if max(rings)<= 50:
about_rings()
print('Key sequences:',about_sequences())