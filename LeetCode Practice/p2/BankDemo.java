public class BankDemo {
    public static void main(String[] args) {
        BankAccount account = new BankAccount("Maya", 100);

        account.deposit(50);
        boolean success = account.withdraw(30);

        System.out.println(account.getOwner());
        System.out.println(account.getBalance());
        System.out.println(success);
    }
}
