public class Solution {

    public static boolean treeSolution(Node head) {
        Node currentHead = head;

        while (currentHead.left != null) {
            if (!checkLeftSubtree(currentHead.left, head.value)) {
                return false;
            } else {
                currentHead = currentHead.left;
            }
        }

        currentHead = head;
        while (currentHead.right != null) {
            if (!checkRightSubtree(currentHead.right, head.value)) {
                return false;
            } else {
                currentHead = currentHead.right;
            }
        }

        return true;
    }

    private static boolean checkLeftSubtree(Node current, int headValue) {
        if (current.value >= headValue) {
            return false;
        } else if (current.left != null) {
            if (current.left.value >= headValue || current.left.value >= current.value) {
                return false;
            }
        } else if (current.right != null) {
            if (current.right.value >= headValue || current.right.value <= current.value) {
                return false;
            }
        }
        return true;
    }

    private static boolean checkRightSubtree(Node current, int headValue) {
        if (current.value <= headValue) {
            return false;
        } else if (current.left != null) {
            if (current.left.value <= headValue || current.left.value >= current.value) {
                return false;
            }
        } else if (current.right != null) {
            if (current.right.value <= headValue || current.right.value <= current.value) {
                return false;
            }
        }
        return true;
    }
}