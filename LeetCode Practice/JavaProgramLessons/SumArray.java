public class SumArray {
    public static void main(String[] args) {
        int[] nums = {3,1,4,2};
        int total = 0;
        for(int i=0;i<nums.length;i++){
            total += nums[i];
        }
        System.out.println(total);
    }
}
