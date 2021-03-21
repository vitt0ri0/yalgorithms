public class Solution {


    public static int siftUp(int[] heap, int idx) {
        int sifted = idx;

        if (idx == 0) {
            return idx;
        }

        int parentIdx = idx / 2;

        if (heap[parentIdx] < heap[idx]) {
            swap(heap, parentIdx, idx);
            return siftUp(heap, parentIdx);
        }

        return sifted;
    }

    private static void swap(int[] arr, int from, int to) {
        int temp = arr[from];
        arr[from] = arr[to];
        arr[to] = temp;
    }
}
