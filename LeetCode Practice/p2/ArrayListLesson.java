import java.util.ArrayList;

public class ArrayListLesson {
    public static void main(String[] args) {
        ArrayList<String> names = new ArrayList<>();
        // Elements must be a string, var name is names, create an empty ArrayList object
        // names -> [] size = 0

        names.add("Maya");
        names.add("Alex");
        names.add("Stan");

        //System.out.println(names.get(1));
        names.set(1, "Jordan");
        //System.out.println(names);

        names.remove(0);
        //System.out.println(names);

        for(int i = 0;i<names.size();i++){
            System.out.println(i + " " + names.get(i));
        }

        ArrayList<Integer> scores = new ArrayList<>();
        scores.add(10);
        scores.add(25);
        scores.add(7);

        int total = 0;

        for(int i=0;i<scores.size();i++){
            total += scores.get(i);
        }

        System.out.println("Scores: " + scores);
        System.out.println("Total: " + total);

        ArrayList<String> foods = new ArrayList<>();
        foods.add("pizza");
        foods.add("tacos");
        foods.add("rice");
        
        System.out.println(foods.get(1));
        
        foods.set(2, "pasta");
        
        foods.remove(0);
        System.out.println(foods);

        for(int i=0;i<foods.size();i++){
            System.out.println(foods.get(i));
        }

        ArrayList<Integer> numbers = new ArrayList<>();
        numbers.add(4);
        numbers.add(9);
        numbers.add(2);
        numbers.add(11);

        int count = 0;
        for(int i=0;i<numbers.size();i++){
            if(numbers.get(i) > 5){
                count++;
            }
        }
        System.out.println(count);

        // 9: .size()
        // 10: int is a primitive type and ArrayList needs a generic type
    }
}
