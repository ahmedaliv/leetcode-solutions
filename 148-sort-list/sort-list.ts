

function merge(left: ListNode | null, right: ListNode | null): ListNode | null {
    const dummy: ListNode = new ListNode();
    let current: ListNode | null = dummy;

    while (left && right) {
        if (left.val < right.val) {
            current.next = left;
            left = left.next;
        } else {
            current.next = right;
            right = right.next;
        }
        current = current.next;
    }

    if (left) {
        current.next = left;
    }
    if (right) {
        current.next = right;
    }

    return dummy.next;
}

function sortList(head: ListNode | null): ListNode | null {
    if (!head || !head.next) {
        return head;
    }

    // Find the middle of the list using the two-pointer approach
    let slow: ListNode | null = head;
    let fast: ListNode | null = head.next;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    // Split the list into two halves
    const right: ListNode | null = slow.next;
    slow.next = null;

    // Recursively sort each part
    const leftSorted: ListNode | null = sortList(head);
    const rightSorted: ListNode | null = sortList(right);

    // Merge the sorted parts
    return merge(leftSorted, rightSorted);
}
