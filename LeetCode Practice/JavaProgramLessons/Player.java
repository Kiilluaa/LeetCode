public class Player {
    private String name; // each Player object gets its own name
    private int score; // each Player stores its own score

    public Player(String name){ // constructor - runs when a new Player object is created
        this.name = name; // store the parameter name into its object's field
        this.score = 0;
    }

    public void addPoints(int points){ // Instance method - changes the score of a particular Player
        score += points;
    }

    public int getScore(){ // instance method - returns this Player's score
        return score;
    }

    public String getName(){
        return name;
    }
}
