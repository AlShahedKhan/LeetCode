class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleLength = len(needle)
        
        if needleLength == 0:
            return 0
        startCount = len(haystack) - needleLength + 1
        for start in range(startCount):
            offset = 0
            while offset < needleLength:
                # if haystack 
            
            
                

            
        # print(needle)
solution = Solution()
solution.strStr('sadbutsad','sad')

# # Problem: Find the first position where needle occurs in haystack.
# # প্রশ্ন: haystack-এর কোথায় প্রথম পুরো needle পাওয়া যায়, সেই index বের করতে হবে।
# # Example: haystack = "sadbutsad", needle = "sad" → answer = 0.

# # Strategy: Try each starting position and compare the letters one by one.
# # কৌশল: প্রতিটি সম্ভাব্য শুরুর জায়গা থেকে অক্ষরগুলো একে একে তুলনা করব।
# # Return the starting index if every letter matches; otherwise return -1.
# # সব অক্ষর মিললে শুরুর index ফেরত দেব; কোথাও পুরোটা না মিললে -1 দেব।

# # Pattern: Brute-force string matching using nested loops.
# # প্যাটার্ন: দুটি loop দিয়ে সম্ভাব্য জায়গাগুলো সরাসরি পরীক্ষা করা।
# # Clue: We need to find a complete sequence of letters inside another string.
# # চেনার সূত্র: একটি string-এর ভেতরে আরেকটি string-এর পুরো অক্ষরক্রম খুঁজতে হচ্ছে।

# # Key trick: Compare haystack[start + offset] with needle[offset].
# # মূল কৌশল: haystack-এর শুরুর জায়গা থেকে যত দূরে যাব, needle-এও তত দূরে যাব।
# # Strings support indexes directly, so converting them to lists is unnecessary.
# # string থেকেও সরাসরি index দিয়ে অক্ষর নেওয়া যায়, তাই list বানানোর প্রয়োজন নেই।


# # Define the class LeetCode expects.
# # LeetCode-এর প্রয়োজনীয় class তৈরি করি।
# class Solution:
#     # Result: The class is defined; nothing is printed.
#     # ফল: class তৈরি হয়; কিছু print হয় না।

#     # Receive both strings and return the index where the match starts.
#     # দুটি string নিয়ে মিলের শুরুর index ফেরত দেওয়ার method তৈরি করি।
#     def strStr(self, haystack: str, needle: str) -> int:
#         # Example: haystack = "sadbutsad", needle = "sad".
#         # উদাহরণ: haystack-এ "sadbutsad", needle-এ "sad" আসে।

#         # Count the needle's letters to know how many must match.
#         # কয়টি অক্ষর মিলতে হবে জানতে needle-এর দৈর্ঘ্য নিই।
#         needleLength = len(needle)
#         # Result: needleLength = 3.
#         # ফল: needleLength হলো 3।

#         # An empty needle matches at the beginning.
#         # needle খালি হলে শুরুতেই মিল পাওয়া গেছে ধরি।
#         if needleLength == 0:
#             # Result for "sad": False, so skip this branch.
#             # "sad"-এর জন্য ফল False, তাই এই অংশে ঢুকবে না।

#             # Return the beginning index for an empty needle.
#             # খালি needle-এর জন্য শুরুর index ফেরত দিই।
#             return 0
#             # Returned value: 0, only when needle is empty.
#             # ফেরত মান: 0, শুধু needle খালি হলে।

#         # Count valid starting positions so needle can fit completely.
#         # পুরো needle বসতে পারে এমন শুরুর জায়গাগুলোর সংখ্যা বের করি।
#         startCount = len(haystack) - needleLength + 1
#         # Result: 9 - 3 + 1 = 7, so possible starts are 0 through 6.
#         # ফল: সম্ভাব্য শুরুর index হলো 0 থেকে 6।

#         # Try each possible start; range(7) gives 0, 1, ..., 6.
#         # প্রতিটি সম্ভাব্য শুরু পরীক্ষা করি; range(7) দেয় 0, 1, ..., 6।
#         for start in range(startCount):
#             # For this example, start = 0 matches, so later starts are not visited.
#             # এই উদাহরণে start = 0-তেই মিলবে, তাই পরের জায়গাগুলো দেখতে হবে না।

#             # Begin at the first needle letter for this starting position.
#             # এই শুরুর জায়গার জন্য needle-এর প্রথম অক্ষর থেকে শুরু করি।
#             offset = 0
#             # Result: offset = 0.
#             # ফল: offset হলো 0।

#             # Compare letters until a mismatch occurs or every needle letter matches.
#             # অক্ষর না মেলা পর্যন্ত অথবা সব অক্ষর মিলে যাওয়া পর্যন্ত তুলনা করি।
#             while offset < needleLength:
#                 # Checks: 0 < 3, 1 < 3, 2 < 3 are True; 3 < 3 is False.
#                 # ফল: তিনটি অক্ষর পরীক্ষা করার পর loop থামে।

#                 # Stop this attempt if the current letters are different.
#                 # বর্তমান অক্ষর দুটি আলাদা হলে এই জায়গার চেষ্টা থামাই।
#                 if haystack[start + offset] != needle[offset]:
#                     # Comparisons: s != s, a != a, d != d are all False.
#                     # ফল: s, a, d—প্রতিবারই অক্ষর মেলে, তাই এখানে ঢোকে না।

#                     # Leave the inner loop so the outer loop can try the next start.
#                     # বাইরের loop যেন পরের শুরু পরীক্ষা করে, তাই ভেতরের loop ছাড়ি।
#                     break
#                     # Result on a mismatch: offset is not increased.
#                     # অমিল হলে ফল: offset আর বাড়ে না।

#                 # Move to the next letter because this letter matched.
#                 # এই অক্ষর মিলেছে, তাই পরের অক্ষরে যাই।
#                 offset = offset + 1
#                 # Results: offset becomes 1, then 2, then 3.
#                 # ফল: offset প্রথমে 1, তারপর 2, শেষে 3 হয়।

#             # Check whether we matched every needle letter.
#             # needle-এর সব অক্ষর মিলেছে কি না দেখি।
#             if offset == needleLength:
#                 # Result: 3 == 3 is True.
#                 # ফল: 3 == 3 সত্য, অর্থাৎ সব অক্ষর মিলেছে।

#                 # Return where the complete match started.
#                 # পুরো মিলটি যেখানে শুরু হয়েছে, সেই index ফেরত দিই।
#                 return start
#                 # Returned value: 0.
#                 # ফেরত দেওয়া মান: 0।

#         # Return -1 if no starting position produced a complete match.
#         # কোনো জায়গায় পুরো needle না মিললে -1 ফেরত দিই।
#         return -1
#         # Example: haystack = "hello", needle = "xyz" would return -1.
#         # উদাহরণ: "hello"-এর মধ্যে "xyz" খুঁজলে -1 ফেরত দেবে।


# # Create an object so we can call the method.
# # method চালানোর জন্য object তৈরি করি।
# solution = Solution()
# # Result: An object is created; nothing is printed.
# # ফল: object তৈরি হয়; কিছু print হয় না।

# # Call the method and display its returned index.
# # method চালিয়ে ফেরত পাওয়া index দেখাই।
# print(solution.strStr("sadbutsad", "sad"))
# # Printed output: 0.
# # স্ক্রিনে দেখাবে: 0।