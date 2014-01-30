import pickle

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
        
def main():
    inp = '0'
    while inp != 'x':
        print fibo(int(inp))
        inp = raw_input('Enter a number => ')
    with open('fibo.pk1', 'wb') as f:
        pickle.dump(fibdict, f)
    

if __name__ == "__main__":
        main()
