import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        //input
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt();
        int res;
        
        if(year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)){
            res = 1;
        } else res = 0;
 
        //output
        System.out.println(res);
    }
}