import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        try(Scanner scan = new Scanner(System.in);){
            System.out.println( Integer.parseInt(scan.nextLine()) );
        }
        catch(NumberFormatException e){
            System.out.println("Bad String");
        }
    }
}
