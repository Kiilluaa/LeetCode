public class GameDemo {
    public static void main(String[] args) {
        Player p1 = new Player("Alex");
        Player p2 = new Player("Maya");

        p1.addPoints(10);
        p2.addPoints(25);

        System.out.println(p1.getScore());
        System.out.println(p2.getScore());
    }
}
