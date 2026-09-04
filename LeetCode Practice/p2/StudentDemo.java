public class StudentDemo {
    public static void main(String[] args) {
        Student student1 = new Student("Maya", 92, 0001);
        Student student2 = new Student("Alex", 81, 0002);

        System.out.println(student1.name + " " + student1.grade);
        System.out.println(student2.name + " " + student2.grade);
    }
}


/*
1: A constructor must contain all the parameters identified to create an object
2: A constructor does not have a return automatically
3: 2
4: "Kai" and 88
5: grade is the parameter and this.grade is the field the parameter is linked to
6: 
*/