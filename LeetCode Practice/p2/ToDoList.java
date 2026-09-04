import java.util.ArrayList;

public class ToDoList {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList();

        list.add("Task 1");
        list.add("Task 2");
        list.add("Task 3");

        for(int i=0;i<list.size();i++){
            System.out.println(i + " " + list.get(i));
        }
    }
}
