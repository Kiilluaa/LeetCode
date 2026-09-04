public class TemperatuteTools {
    public static void main(String[] args) {
        printWelcome();

        printDouble(5);
        printDouble(12);

        int answer = doubleNumber(6);
        System.out.println(answer);
    }

    public static void printWelcome() {
        System.out.println("Temperature Tools");
    }

    public static void printDouble(int number){
        System.out.println(number * 2);
    }

    public static int doubleNumber(int number) {
        int result = number * 2;
        return result;
    }
}
