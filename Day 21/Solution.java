import java.util.*;

class Printer <T> {

    /**
    *    Method Name: printArray
    *    Print each element of the generic array on a new line. Do not return anything.
    *    @param A generic array
    **/
    
    // Write your code here
static <E>  void printArray( E[] inputArray)
{
for( E e : inputArray)
    {
    System.out.println(""+e);
}

}
}
