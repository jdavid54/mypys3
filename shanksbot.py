# Reprocicals of prime : 1/p

# link : https://www.youtube.com/watch?v=DmfxIhmGPP4

'''

https://github.com/babymotte/shanksbot-rs/blob/master/src/lib.rs

pub fn shanks(number: u64) -> u64 {
    let mut known_remainders = HashSet::new();

    let mut counter = 0u64;
    let mut remainder = 1;

    while {
        while number > remainder {
            counter += 1;
            remainder *= 10;
            known_remainders.insert(remainder);
        }
        known_remainders.insert(remainder);
        let div = remainder / number;
        remainder = (remainder - (div * number)) * 10;
        remainder != 0 && !known_remainders.contains(&remainder)
    } {
        counter += 1;
    }

    counter
}


test

fn shanks7() {
    assert_eq!(shanks(7), 6);
} 
1/7
0.142857 142857 14285

fn shanks60013() {
    assert_eq!(shanks(60013), 5001);
}
#[test]

fn shanks60017() {
    assert_eq!(shanks(60017), 60016);
}

#[test]
fn shanks60037() {
    assert_eq!(shanks(60037), 10006);
}

#[test]
fn shanks61561() {
    assert_eq!(shanks(61561), 405);
'''
from decimal import *

def test():
    getcontext().prec = 6
    v = Decimal(1) / Decimal(7)
    print(v)

    getcontext().prec = 415
    v = Decimal(1) / Decimal(7)
    print(v)
    print()
    v = Decimal(1) / Decimal(61561)
    print(v)

    print(len('000016244050616461720894722307954711586881304722145514205422264095774922434658306395282727700979516252172641769951755169669108688942674745374506586962524975227822809895875635548480369064830006010298728090836731047253943243287146082747193840256006237715436721300823573366254609249362421013303877454882149412777570214908789655788567437176134240834294439661473985152937736553987102223810529393609590487483959'))

    getcontext().prec = 50
    v = Decimal(1) / Decimal(7)
    print(v)


debug = False

def shanks(number):
    
    counter = 0
    remainder = 1
    known_remainders = []

    while remainder != 0 and remainder not in known_remainders:
        if debug:print(remainder)
        while number > remainder:
            counter += 1
            remainder *= 10
            known_remainders.append(remainder)
        #known_remainders.append(remainder)           
        div = remainder // number
        known_remainders.append(remainder+div)
        remainder = (remainder - (div*number))*10
         
        if debug:print('div',remainder,number,div,known_remainders)
        counter += 1
    if debug:print(number,counter,known_remainders)    
    return counter-1, Decimal(1) / Decimal(number)

if __name__ == '__main__':
    print('\nShanking.....\nThe result must be less or equal to n-1')
    print(7,shanks(7))           #6
    print(23,shanks(23))         #22
    print(60013,shanks(60013))   #5001
    #print(60017,shanks(60017))  #60016 very long time to compute
    print(60037,shanks(60037))   #10006
    print(61561,shanks(61561))   #405

