class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(num) for num in digits]
        stringNum = "".join(digits)
        num = int(stringNum) + 1
        stringNum = str(num)
        answer = []
        for char in stringNum:
            answer.append(int(char))
        return answer