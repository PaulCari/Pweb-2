import java.util.*;
public class Calculator{
    static Scanner scan = new Scanner(System.in);
    public static void main (String [] args){
        int x,y;
        System.out.println("Numero 1: ");
        x = scan.nextInt();
        System.out.println("Numero 2: ");
        y = scan.nextInt();
        sumar(x,y);
    }
    public static int sumar(int a, int b){
        System.out.print("La suma es: "+(a+b));
        return 0;
    }
}
