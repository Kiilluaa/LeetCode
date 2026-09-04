public class WorkoutDays {
    public static void main(String[] args) {
        for (int day = 1; day <= 5; day++) {
            System.out.println("Workout day " + day);
        }


    }

    public static void loops() {
        for (int i=0;i<10;i++) {
            System.out.println(i);
        }

        for (int i = 1; i<=10; i++) {
            System.out.println(i);
        }

        for (int i = 10; i > 0; i--) {
            System.out.println(i);
        }

        for (int i = 0; i % 2 == 0; i++){
            System.out.println(i);
        }

        for (int i = 0; i < 3; i++) {
            System.out.println("Hi");
        }

        int i = 1;
        while (i < 6) {
            System.out.println(i);
            i++;
        }

        for (int i = 1; i < 6; i++) {
            System.out.println(i);
        }
    }
}