class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letter = list(columnTitle)
        letter = letter + 1
        
        print(letter[1])

# Create an object so Python can pass it to the method as self.
# object তৈরি করি, যাতে Python method-এর self-এ সেটি দিতে পারে।
solution = Solution()
# Result: solution is now a Solution object; nothing is printed here.
# ফল: solution এখন একটি Solution object; এখানে কিছু print হয় না।
solution.titleToNumber("AB")
