

class PokerCard:
    #faces = '23456789TJQKA'
    #suits = 'cdhs'
    facePrimes = {'2':11, '3':13, '4': 17, '5':19, '6':23, '7':29, '8':31, '9':37, 'T':41, 'J':43, 'Q':53, 'K':59, 'A':61}
    suitPrimes = {'c':2, 'd':3, 'h':5, 's':7}
    hashCode = 1
    
    def __init__(self, hand):
        for k in range(0,len(hand),2):
            print(k, hand[k],hand[k+1], self.facePrimes[hand[k]], self.suitPrimes[hand[k+1]],end=':')
            self.hashCode *= self.facePrimes[hand[k]]*self.suitPrimes[hand[k+1]]
            print(self.hashCode)
    
    def HashVal(self):
      return self.hashCode
    
    def Decode_suit(self):
        for k in self.suitPrimes.keys():
            h=self.hashCode
            d=self.suitPrimes[k]
            while h%d==0:
                print(k,end=',')
                h=h//d
            print()

    def Decode_face(self):
            for k in self.facePrimes.keys():
                h=self.hashCode
                d=self.facePrimes[k]
                while h%d==0:
                    print(k,end=',')
                    h=h//d
                #print()
    
hand = 'AcAdAhThKsKhQs'

h1 = PokerCard(hand)
print(h1.HashVal())
print(hand)
h1.Decode_suit()
h1.Decode_face()