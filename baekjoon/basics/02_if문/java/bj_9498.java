import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        //input
        Scanner sc = new Scanner(System.in);
        int score = sc.nextInt();
 
        
        //logic
        char grade = 'F';
        if(score >= 90) grade = 'A';
        else if (score >= 80) grade ='B';
        else if (score >= 70) grade = 'C';
        else if (score >= 60) grade = 'D';
        else grade = 'F'; 
  
      

        //output
        System.out.println(grade);
    }
}