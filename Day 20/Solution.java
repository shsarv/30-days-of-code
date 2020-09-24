import java.util.Scanner;

public class Solution {
    private static int[] array;

    private static void bubbleSort() {
        int n = array.length;
        
        // Number of swaps for all array iterations
        int totalSwaps = 0; 

        for (int i = 0; i < n; i++) {
            // Track if a swap was made
            boolean swapped = false;
            
            for (int j = 0; j < array.length - 1; j++) {
                if (array[j] > array[j + 1]) {
                    int tmp = array[j];
                    array[j] = array[j + 1];
                    
                    array[j + 1] = tmp;
                    swapped = true; 
                    totalSwaps++;
                }
            }

            // Terminate loop as soon as array is sorted
            if (!swapped) {
                break;
            }
        }
        
        // Print answer
        System.out.printf("Array is sorted in %d swaps.\n", totalSwaps);
        System.out.printf("First Element: %d\n", array[0]);
        System.out.printf("Last Element: %d\n", array[n - 1]);
    }
    
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        array = new int[n];
        for (int i = 0; i < n; i++) {
            array[i] = in.nextInt();
        }
        in.close();

        bubbleSort();
    }
}
