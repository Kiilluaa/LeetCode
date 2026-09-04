public class ShoppingTotal {
    public static void main(String[] args) {
        double shirtPrice = 24.50;
        int quantity = 3;
        double subtotal = shirtPrice * quantity;
        double tax = subtotal * 0.08;
        double total = subtotal + tax;

        System.out.println("Total: " + total);
    }
}
