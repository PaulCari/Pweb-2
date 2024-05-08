import java.util.Scanner;

public class Calculator {
  private static Scanner scanner = new Scanner(System.in);

  public static void main(String[] args) {
    int num1 = getNumber("Ingrese el primer número: ");
    int num2 = getNumber("Ingrese el segundo número: ");

    System.out.println("Resultados:");
    System.out.println("Suma: " + add(num1, num2));
    System.out.println("Resta: " + subtract(num1, num2));
    System.out.println("Multiplicación: " + multiply(num1, num2));
    System.out.println("División: " + divide(num1, num2)); 
    System.out.println("Módulo: " + modulo(num1, num2)); 
  }

  private static int getNumber(String prompt) {
    System.out.println(prompt);
    return scanner.nextInt();
  }

  private static int add(int a, int b) {
    return a + b;
  }

  private static int subtract(int a, int b) {
    return a - b;
  }

  private static int multiply(int a, int b) {
    return a * b;
  }

  private static double divide(int a, int b) {
    if (b == 0) {
      System.out.println("Error: No se puede dividir entre cero.");
      return Double.NaN; 
    }
    return (double) a / b; 
  }

  private static int modulo(int a, int b) {
    if (b == 0) {
      System.out.println("Error: No se puede realizar el módulo entre cero.");
      return 0;
    }
    return a % b;
  }
}

