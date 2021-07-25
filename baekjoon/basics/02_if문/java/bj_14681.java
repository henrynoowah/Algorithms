import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //input
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();
        int y = scanner.nextInt();
        
        int q;
        //logic
        if(x > 0){
            if(y > 0) q = 1;
            else q = 4;
        } else {
            if (y > 0) q = 2;
            else q = 3;
        }
            
        //output
        System.out.println(q);
    }
}