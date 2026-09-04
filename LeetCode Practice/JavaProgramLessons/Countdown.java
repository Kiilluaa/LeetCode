public class Countdown {
    public static void main(String[] args) {
        int number = 1;
        int total = 0;

        while (number <= 4) {
            total = total + number;
            number++;
        }

        System.out.println(total);
    }
}
