public class ScorePrinter {
    public static void main(String[] args) {
        int[] scores = {82, 91, 76, 95};

        int total = 0;
        for (int i = 0; i < scores.length; i++) {
            total = total + scores[i];
            //System.out.println(scores[i]);
        }

        System.out.println(total);

        for (int score : scores) {
            System.out.println(score);
        }
    }
}

// 1: for(int i=0; i<nums.length; i++)
// 2: an array index starts with 0
// 3: nums.length is 1 longer than the last index, < does not include the extra number
// 4: element of the array nums at index of i
// 5: i=0 nums[0]=5, i=1 nums[1]=8, i=2 nums[2]=2
// 6: System.out.println(nums[0]);, System.out.println(nums[1]);, System.out.println(nums[2]);
// 7: System.out.println(nums[i]*2);
// 8: total += nums[i];
// 9: count = 0; count++;

// 10:
int[] nums = {10, 7, -19, -18, 30};
int count = 0;
for(i=0;i<nums.length;i++){
    if(nums[i]>0){
        count++;
    }
}
System.out.println(count);
