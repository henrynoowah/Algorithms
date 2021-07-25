import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //input
        Scanner scanner = new Scanner(System.in);
        int h = scanner.nextInt();
        int m = scanner.nextInt();
        
        m -= 45;
        //logic
        if(m < 0) {
            m += 60;
            h--;
            if(h < 0) {
                h = 23;
            }
        } 
        //output
        System.out.println(h + " " +m);
    }
}