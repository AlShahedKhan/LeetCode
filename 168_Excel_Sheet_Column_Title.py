#Problem: Convert 271 into its Excel column title
#Strategy: Find each letter from right and add it to the front
#Pattern: Repeated division with reminder
#Clue: We must convert a number into positions using 26 letters
#key Trick: Subtract 1 because Excel counts from 1, but indexes start at 0

#Because we need all alphabet
import string
    #Because leetCode need this class  
class Solution:
        # Define function so it takes integer and return string
    def convertToTitle(self, columnNumber: int) ->str:
        # We need all uppercase alphabet
        letters = string.ascii_uppercase
        # We need to make them in to list to find index
        letters = list(letters)
        
              
solution = Solution()
print(solution.convertToTitle(271))




# # Problem: Convert 271 into its Excel column title.
# # প্রশ্ন: 271-কে Excel column title-এ বদলাতে হবে।

# # Strategy: Find each letter from right to left and add it to the front.
# # কৌশল: ডান থেকে বামে অক্ষর বের করে উত্তরের সামনে বসাব।

# # Pattern: Repeated division with remainder.
# # প্যাটার্ন: বারবার ভাগ করে ভাগশেষ থেকে অক্ষর বের করা।
# # Clue: We must convert a number into positions using 26 letters.
# # চেনার সূত্র: 26টি অক্ষর দিয়ে সংখ্যাটির বিভিন্ন স্থান প্রকাশ করতে হচ্ছে।

# # Key trick: Subtract 1 because Excel counts from 1, but indexes start at 0.
# # মূল কৌশল: Excel-এর গণনা 1 থেকে, কিন্তু index 0 থেকে—তাই 1 কমাই।


# # Import string to get uppercase English letters.
# # বড় হাতের ইংরেজি অক্ষর পেতে string module আনি।
# import string
# # Result: The module is available; nothing is printed.
# # ফল: module ব্যবহার করা যাবে; কিছু print হয়নি।


# # Define the class that LeetCode expects.
# # LeetCode-এর প্রয়োজনীয় Solution class তৈরি করি।
# class Solution:
#     # Result: A class is defined; nothing is printed.
#     # ফল: class তৈরি হয়; কিছু print হয়নি।

#     # Define a method that receives an integer and returns a string.
#     # পূর্ণসংখ্যা নেওয়া ও string ফেরত দেওয়ার method তৈরি করি।
#     # int and str describe the types; self refers to the object.
#     # int ও str মানের ধরন বোঝায়; self object-কে বোঝায়।
#     def convertToTitle(self, columnNumber: int) -> str:
#         # Result: When called with 271, columnNumber starts as 271.
#         # ফল: 271 দিয়ে চালালে শুরুতে columnNumber = 271।

#         # Make a list so we can select each letter by its index.
#         # index দিয়ে অক্ষর বাছতে alphabet-গুলো list-এ রাখি।
#         letters = list(string.ascii_uppercase)
#         # Result: letters[0] = "A", letters[9] = "J", letters[10] = "K".
#         # ফল: index 0-তে A, 9-তে J এবং 10-তে K আছে।

#         # Start with an empty answer because no letters have been found yet.
#         # এখনো অক্ষর বের হয়নি, তাই উত্তর খালি রাখি।
#         title = ""
#         # Result: title = "".
#         # ফল: title খালি string।

#         # Continue while there is still a number to convert.
#         # রূপান্তরের জন্য সংখ্যা বাকি থাকলে loop চালাই।
#         while columnNumber > 0:
#             # Checks: 271 > 0 → True; 10 > 0 → True; 0 > 0 → False.
#             # ফল: প্রথম দুইবার loop চলে; শেষে 0 হলে থামে।

#             # Subtract 1 to match Excel's counting with list indexes.
#             # Excel-এর গণনাকে list index-এর সঙ্গে মেলাতে 1 কমাই।
#             columnNumber = columnNumber - 1
#             # Round 1: 271 → 270. Round 2: 10 → 9.
#             # ফল: প্রথমবার 270; দ্বিতীয়বার 9।

#             # Use % to get the remainder and choose a letter's index.
#             # % দিয়ে ভাগশেষ বের করে অক্ষরের index বাছি।
#             index = columnNumber % 26
#             # Round 1: 270 % 26 = 10. Round 2: 9 % 26 = 9.
#             # ফল: প্রথমবার index = 10; দ্বিতীয়বার index = 9।

#             # Read the letter at the chosen index.
#             # বেছে নেওয়া index-এর অক্ষরটি নিই।
#             letter = letters[index]
#             # Round 1: letter = "K". Round 2: letter = "J".
#             # ফল: প্রথমবার K; দ্বিতীয়বার J।

#             # Add the letter in front because the rightmost letter comes first.
#             # ডানদিকের অক্ষর আগে পাই, তাই নতুন অক্ষর সামনে বসাই।
#             title = letter + title
#             # Round 1: "K" + "" = "K". Round 2: "J" + "K" = "JK".
#             # ফল: প্রথমবার title = "K"; দ্বিতীয়বার title = "JK"।

#             # Use // to keep the whole-number quotient for the next round.
#             # পরেরবারের জন্য // দিয়ে পূর্ণসংখ্যার ভাগফল রাখি।
#             columnNumber = columnNumber // 26
#             # Round 1: 270 // 26 = 10. Round 2: 9 // 26 = 0.
#             # ফল: প্রথমবার 10 থাকে; দ্বিতীয়বার 0 হয়, তাই loop থামে।

#         # Return after the loop finishes, so every letter is included.
#         # সব অক্ষর তৈরি হওয়ার পরে ফেরত দিতে return-কে loop-এর বাইরে রাখি।
#         return title
#         # Returned value: "JK"; return itself does not print anything.
#         # ফেরত দেওয়া মান: "JK"; return নিজে print করে না।


# # Create an object so we can call the method.
# # method চালানোর জন্য object তৈরি করি।
# solution = Solution()
# # Result: solution refers to an object; nothing is printed.
# # ফল: object তৈরি হয়; কিছু print হয়নি।

# # Call the method with 271 and print the returned title.
# # 271 দিয়ে method চালিয়ে ফেরত পাওয়া title print করি।
# print(solution.convertToTitle(271))
# # Printed output: JK
# # স্ক্রিনে দেখাবে: JK