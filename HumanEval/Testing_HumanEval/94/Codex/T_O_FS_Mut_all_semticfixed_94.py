def skjkasdkd(lst):
    
    def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False

        return True
    maxx = 0
    i = 0
    while i < len(lst):
        if(lst[i] > maxx and isPrime(lst[i])):
            maxx = lst[i]
        i+=1
    result = sum(int(digit) for digit in str(maxx))
    return result





def test():
    assert skjkasdkd([1,2,3]) == 3
    assert skjkasdkd([0,0,7,7,7,0,0,0]) == 7
    assert skjkasdkd([1,2,3,5,6,7,8])== 7
    assert skjkasdkd([0,0,7,7,7,0,0,0])==7
    assert skjkasdkd([1,2,3]) == 3
    assert skjkasdkd([0,0,7,7,7,0,0,0]) == 7
    assert skjkasdkd([1,2,3]) == 3
    assert skjkasdkd([9,3,3]) == 3
    assert skjkasdkd([0,0,7,7,7,0,0,0]) == 7
    assert skjkasdkd([11,2,3]) == 2
