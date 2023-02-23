public class prost_chisla {
    public static void main(String[] args) {
        for (int i = 2; i <100 ; i++) {
            if (IsPrime(i)) {
                System.out.println(i);
            }
        }
    }
    public static boolean IsPrime(int a){
        boolean count = true;
        for (int i = 2; i <= a/i ; i++) {
            if (a%i == 0){
                count = false;
            }
        }
        return count;
    }
}
