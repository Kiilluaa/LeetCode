public class MathTools {
    public static int square(int n){
        return n*n;
    }
}



/*
elsewhere
int x = MathTools.square(6);
No MathTools object is needed. 'Square' only uses the parameter n

Instance Method
Player p1 = new Player("Alex");
p1.addPoints(10);
addPoints changes p1's private score. It needs a specific object, so it is not static

A static field shared by every object
public class VisitCounter{
    private static int visits = 0;

    public VisitCounter(){
        visits++;
    }

    public static int getVisits(){
        return visits;
    }
}
There is one shared visits value for the class, not one copy per object

Why main is static
Java needs a starting method before creating any objects.
It can call ClassName.main() at the class level.
The standard main method is static

1: access
2: ownership
3: so only itself can access it
4: 
*/