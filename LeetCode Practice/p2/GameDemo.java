public class GameDemo {
    public static void main(String[] args) {
        Player player1 = new Player();

        player1.name = "Alex";
        player1.score = 50;

        Player player2 = new Player();

        player2.name = "Maya";
        player2.score = 25;

        Player player3 = new Player();

        player3.name = "Sam";
        player3.score = 5;
        player3.level = 2;

        //System.out.println(player1.name);
        //System.out.println(player1.score);

        System.out.println(player1.name + ": " + player1.score);
        System.out.println(player2.name + ": " + player2.score);
    }
}

/*
1: Player.java is the type that defined what fields each player object will have.
   player1 is the object created using Player which stores the values for each instance field
2: Player
3: player1
4: new Player()
5: 
6: 
7: 0
8: no each player object stores its own reference fields
9: 
10: Player p = new Player();
*/