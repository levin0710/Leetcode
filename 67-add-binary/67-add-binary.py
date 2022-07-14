class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        carry, a, b = 0, a[::-1], b[::-1]
        answer = ""
        for i in range(max(len(a), len(b))):
            num1 = int(a[i]) if i < len(a) else 0
            num2 = int(b[i]) if i < len(b) else 0
            
            numOnes = carry + num1 + num2
            
            answer = str(numOnes % 2) + answer
            
            carry = numOnes // 2
            
        if carry != 0:
             answer = "1" + answer
                
        return answer