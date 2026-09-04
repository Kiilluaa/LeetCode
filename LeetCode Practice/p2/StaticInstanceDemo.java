public class StaticInstanceDemo {
    public static void main(String[] args) {
        int result = MathTools.square(6);
        System.out.println(result);

        PlayerScore player = new PlayerScore(10);
        player.addPoints(7);
        System.out.println(player.getScore());
    }
}

/*
1: access
2: ownership
3: 
6: int result = MathTools.square(4);
7: hero.takeDamage(3);
8: It changes the stored value of an object. it is not the same number
9: Square only needs its argument and does not depend on one MathTools object's field
10: access, class level ownership, return type, method name, parameter type, parameter name
11: 
*/