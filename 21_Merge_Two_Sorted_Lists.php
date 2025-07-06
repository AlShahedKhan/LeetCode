<?php

// ✅ Linked List এর জন্য Node ক্লাস
class ListNode {
    public $val = 0;
    public $next = null;

    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

// ✅ মূল Solution ক্লাস
class Solution {

    function mergeTwoLists($list1, $list2) {
        echo "👉 Starting Merge Process...\n";

        $dummy = new ListNode(-1);
        $current = $dummy;

        while ($list1 !== null && $list2 !== null) {
            echo "🔍 Comparing list1->val = {$list1->val} and list2->val = {$list2->val}\n";

            if ($list1->val < $list2->val) {
                echo "✅ list1->val is smaller, adding {$list1->val} to merged list\n";
                $current->next = $list1;
                $list1 = $list1->next;
            } else {
                echo "✅ list2->val is smaller or equal, adding {$list2->val} to merged list\n";
                $current->next = $list2;
                $list2 = $list2->next;
            }

            $current = $current->next;
        }

        if ($list1 !== null) {
            echo "📌 list2 finished, attaching remaining list1 starting from {$list1->val}\n";
            $current->next = $list1;
        } else if ($list2 !== null) {
            echo "📌 list1 finished, attaching remaining list2 starting from {$list2->val}\n";
            $current->next = $list2;
        }

        echo "✅ Merge Complete.\n";
        return $dummy->next;
    }
}

// ✅ ইউটিলিটি ফাংশন: লিস্ট প্রিন্ট করার জন্য
function printList($node) {
    echo "🔁 Final Merged List: ";
    while ($node !== null) {
        echo $node->val . ' ';
        $node = $node->next;
    }
    echo "\n";
}

// ✅ টেস্ট ডেটা তৈরি
$list1 = new ListNode(1, new ListNode(2, new ListNode(4)));
$list2 = new ListNode(1, new ListNode(3, new ListNode(4)));

// ✅ মেইন এক্সিকিউশন
$solution = new Solution();
$merged = $solution->mergeTwoLists($list1, $list2);

// ✅ আউটপুট দেখাও
printList($merged);

?>
