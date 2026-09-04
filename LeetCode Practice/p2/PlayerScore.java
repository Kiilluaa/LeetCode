public class PlayerScore {
    private int score;
    private int health;

    public PlayerScore(int score){
        this.score = score;
    }

    public void addPoints(int points){
        score += points;
    }

    public int getScore(){
        return score;
    }

    public int takeDamage(int damage){
        if (damage <= health) {
            health -= damage;
            return health;
        }
        return health;
    }
}
