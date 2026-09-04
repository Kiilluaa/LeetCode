public class BankAccount {
    private String owner;
    private int balance;

    public BankAccount(String owner, int balance){
        this.owner = owner;
        this.balance = balance;
    }

    public String getOwner(){
        return owner;
    }

    public int getBalance(){
        return balance;
    }

    public void deposit(int amount){
        if(amount > 0){
            balance += amount;
        }
    }

    public boolean withdraw(int amount){
        if(amount > 0 && amount <= balance){
            balance -= amount;
            return true;
        }
        
        return false;
    }
}
