##################### starting with DSA ####################################

'''
1. Easy - getting user input and printing them
'''

class Solution:
    def printNumber(self):
        a = input('User given values')
        return int(a)

b = Solution()
print(f"Output:{b.printNumber()}")

'''
2. Easy - If and else statement
'''

class Solution:
    def studentGrade(self, marks):
        #marks = int(input("Enter your marks"))
        if marks>=95:
            return "A"
        elif marks>=70 & marks<95:
            return "B"
        elif marks>=50 & marks<70:
            return "C"
        elif marks>=35 & marks<50:
            return "D"
        else:
            return "Fail"
    
b = Solution()
print(f"Grade:{b.studentGrade(99)}")