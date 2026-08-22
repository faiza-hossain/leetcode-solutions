class Solution:
    def checkDivisibility(self, n: int) -> bool:
        c=n
        sum=0
        product=1
        while n>0:
            d=n%10
            sum=sum+d
            product=product*d
            n=n//10
        return c%(sum+product)==0
