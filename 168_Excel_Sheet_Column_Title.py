import string
class Solution:
    def convertToTitle(self, columnNumber: int) ->str:
        #we have 26 alphabet so every number belongs to an alphabet
        # print(string.ascii_uppercase)
        #make it an array every letter should be in an index so i need to make it in list
        alphabets = string.ascii_uppercase
        listedAlphabets = list(alphabets)
        # Now i found them inside index. now i need to match the index to column numbers
        # print(listedAlphabets[0])
        # for assing index to letter i need to use unumerate function that use to pair 

        for index,letter in enumerate(listedAlphabets):
            print(index + 1,letter)
solution = Solution()
print(solution.convertToTitle(271))