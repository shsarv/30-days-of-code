#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main() {
    int n; 
    scanf("%d", &n);
    int *a = malloc(sizeof(int) * n);
    for(int a_i = 0; a_i < n; a_i++){
    	scanf("%d",&a[a_i]);
    }
        
        // Number of swaps for all array iterations
        int totalSwaps = 0; 

        for (int i = 0; i < n; i++) {
            // Track if a swap was made
            bool swapped = false;
            
            for (int j = 0; j < n - 1; j++) {
                if (a[j] > a[j + 1]) {
                    int tmp = a[j];
                    a[j] = a[j + 1];
                    
                    a[j + 1] = tmp;
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
        printf("Array is sorted in %d swaps.\n", totalSwaps);
        printf("First Element: %d\n", a[0]);
        printf("Last Element: %d\n", a[n - 1]);
    return 0;
}
