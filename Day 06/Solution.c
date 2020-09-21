#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    char str[10000];
    int i,j,l,k,n;
    scanf("%d\n",&n);
    for(i=0;i<n;i++)
    {
         gets(str);
         j=strlen(str);
         for(k=0;k<j;k++)
         {
             if(k%2==0)
             {
                 printf("%c",str[k]);
             }

         }
         printf(" ");
         for(l=0;l<j;l++)
         {
             if(l%2!=0)
             {
                 printf("%c",str[l]);
             }

         }
      printf("\n");
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
