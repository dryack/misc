import pickle

#attempt to load fibo.pk1 in order to populate
#fibdict.  if this fails for any reason
#define fibdict with starter values
try:
    with open('fibo.pk1', 'rb') as f:
        fibdict = pickle.load(f)
except:
    fibdict = {0:1, 1:1}

def fibo(num):
    if fibdict.has_key(num):
        return fibdict[num]
    else:
        newvalue = fibo(num-1)+fibo(num-2)
        fibdict[num] = newvalue
        return newvalue

def get_input(prompt):
    input = raw_input(prompt)
    #checking user request against the highest key already in fibdict
    #anything more than 500 higher is rejected to prevent recursion limit
    #errors    
    if (input.isdigit() == True) and \
    (int(input) > (int(fibdict.keys()[-1]) + 500)):
        print "Exceeds safe recursion depth, try a lower number"
        return get_input(prompt)
    #ensure we're getting a valid command
    elif (input.isdigit() == True) or input == 'x' or input == 'X':
        return input
    else:
        print "Enter a number or \'x\'"
        return get_input(prompt)
        
def main():
    inp = '0'
    while inp != 'x':
        print fibo(int(inp))
        inp = get_input('Enter a number (or x to quit) => ')
    with open('fibo.pk1', 'wb') as f:
        pickle.dump(fibdict, f, -1)
    

if __name__ == "__main__":
