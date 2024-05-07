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
        sub(x, y);
        mul(x, y);
        mod(x, y);

    }
    public static int sumar(int a, int b){
        System.out.print("La suma es: "+(a+b));
        return 0;
    }
    public static int sub(int a , int b){
        System.out.println("La resta es: " + (a-b));
        return 0;
    }
    public static int mul(int a, int b){
        System.out.println("El producto es: " + (a*b));
        return 0;
    }
    public static int div(int a, int b){
        System.out.println("La división de los numeros es: " + (a/b));
        return 0;
    }
    public static int mod(int a, int b){
        System.out.println("La respuesta del modulo entre los numeros es: " + (a % b));
        return 0;
    }
    
}
