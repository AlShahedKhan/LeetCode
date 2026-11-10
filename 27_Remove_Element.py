# Problem: Remove every value equal to val.
# সমস্যা: val-এর সমান সব মান বাদ দিতে হবে।
# For nums = [3, 2, 2, 3] and val = 2, the kept values are [3, 3].

# Strategy: Check each value. Copy values that do not match val to the front.
# কৌশল: প্রতিটি মান পরীক্ষা করব। val-এর সঙ্গে না মিললে সেটি list-এর সামনে রাখব।
# Return how many values were kept.
# শেষে কতটি মান রাখা হয়েছে, সেই সংখ্যা ফেরত দেব।

# Pattern: Two pointers.
# প্যাটার্ন: দুটি index ব্যবহার করা।
# i checks each value; k marks where the next kept value should go.
# i প্রতিটি মান পরীক্ষা করে; k পরের রাখা মানটি কোথায় বসবে তা মনে রাখে।


# Define the class LeetCode expects.
# LeetCode যে class চায়, সেটি তৈরি করি।
class Solution:
    # Result: The class is defined; nothing is printed.
    # ফল: class তৈরি হয়; কিছু print হয় না।

    # Receive the list and val, then return the count of kept values.
    # list ও val নিয়ে রাখা মানগুলোর সংখ্যা ফেরত দেওয়ার method তৈরি করি।
    def removeElement(self, nums: list[int], val: int) -> int:
        # Example input: nums = [3, 2, 2, 3], val = 2.
        # উদাহরণ: nums = [3, 2, 2, 3], val = 2।

        # Start the kept-value count at 0; no values have been checked yet.
        # রাখা মানের সংখ্যা 0 থেকে শুরু করি; এখনো কোনো মান পরীক্ষা করিনি।
        k = 0
        # Result: k = 0.
        # ফল: k-এর মান 0।

        # Visit every original position; the list length stays the same during this loop.
        # শুরুর list-এর প্রতিটি index দেখি; loop চলার সময় list-এর দৈর্ঘ্য বদলায় না।
        for i in range(len(nums)):
            # i goes through 0, 1, 2, 3.
            # i-এর মান হবে 0, 1, 2, 3।

            # Keep the current value only when it is different from val.
            # বর্তমান মান val-এর সমান না হলেই সেটি রাখি।
            if nums[i] != val:
                # Checks: 3 != 2 is True; 2 != 2 is False;
                # 2 != 2 is False; 3 != 2 is True.
                # পরীক্ষা: প্রথম 3 রাখা হবে; মাঝের দুইটি 2 বাদ যাবে;
                # শেষের 3-টিও রাখা হবে।

                # Copy this non-matching value to the next open position at the front.
                # না-মেলা মানটি সামনে পরের খালি জায়গায় কপি করি।
                nums[k] = nums[i]
                # First kept 3: nums[0] = 3. Last kept 3: nums[1] = 3.
                # প্রথম 3 বসে nums[0]-তে; শেষ 3 বসে nums[1]-তে।

                # Increase k because one more value has been kept.
                # আরেকটি মান রাখলাম, তাই k এক বাড়াই।
                k = k + 1
                # Result: k becomes 1 after the first 3, then 2 after the last 3.
                # ফল: প্রথম 3-এর পর k = 1; শেষ 3-এর পর k = 2।

        # Return the count; LeetCode uses this to know how many front values are valid.
        # সংখ্যাটি ফেরত দিই; LeetCode জানবে সামনের কয়টি মান রাখা হয়েছে।
        return k
        # Returned value: 2. The first two nums values are [3, 3].
        # ফেরত মান: 2। nums-এর প্রথম দুইটি মান হলো [3, 3]।