#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
   int n=0;
   int i=0;
   scanf("%d",&n);
   for(i=1;i<11;i++){
       printf("%d x %d = %d\n",n,i,n*i);
   }

    return 0;
}
