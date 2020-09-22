import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {



    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        int s=0;
        int t=0;
        int rem;
    while (n>0){
        rem=n%2;
        n= n/2;
        if(rem==1){
            s=s+1;
            if(s>=t){
                t=s;}}
        else{
            s=0;}}
            System.out.println(t);

        scanner.close();
    }
}
