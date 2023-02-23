import java.util.Scanner;
public class revers_slova {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.next();
        if (IsPalindrome(s)) {
            System.out.println("Слово " + "\"" + s + "\"" + " является полиндромом");
        }
        else {
            System.out.println("Слово " + "\"" + s + "\"" + " не являеися полиндромом");
        }
    }
    public static String reversString(String s){
        return new StringBuilder(s).reverse().toString();
    }
    public static boolean IsPalindrome(String s){
        return s.equals(reversString(s));
    }
}
