public class ArrayReporter {
    public static void main(String[] args) {
        int[] values = {4, 7, 2, 9};
        int answer = sumArray(values);
        System.out.println(answer);
    }

    public static int sumArray(int[] nums) {
        int total = 0;
        for (int i=0;i<nums.length;i++){
            total+=nums[i];
        }
        return total;
    }
}

// 1: public static void printAll(int[] nums)
// 2: nums[i]
// 3: public static int sumArray(int[] nums)
// 4: total is found using the parameter
// 5: outside of the for loop at the start of the method
// 6: its initialized at 0 and added as the array is traversed
/* 7:
public static int sumArray(int[] nums){
    int total = 0;
    for(int i=0;i<nums.length;i++){
        total+=nums[i];
    }
    return total;
}
*/
// 8: int answer = sumArray(values);
/* 9:
public static int countElements(int[] nums){
    return nums.length;
}
 */
/* 10:
public static int firstValue(int[] nums){
    return nums[0];
}
 */
/* 11:
public static int lastValue(int[] nums){
    return nums[nums.length - 1];
}
 */
/* 12:
public static int countPositive(int[] nums){
    int count = 0;
    for(int i=0;i<nums.length;i++){
        if(nums[i]>0){
            count++;
        }
    }
    return count;
}
*/
// 13: int
// 14: int[] nums
// 15: count
/* 16:
public class Count {
    public static void main(String[] args) {
        int[] values = {13, -3, 5, 1, -19};
        int pos = countPositive(values);
    }

    public static int countPositive(int[] nums) {
        int count = 0;
        for(int i=0;i<nums.length;i++) {
            if(nums[i] > 0) {
                count++;
            }
        }
        return count;
    }
}
*/
/* 17:
public static boolean containsZero(int[] nums) {
    for(int i=0;i<nums.length;i++){
        if(nums[i] == 0) {
            return true
        }
    }
    return false
}
*/
// 18: the method only needs to know if a zero is present in the array. not how many
// 19: false
// 20: int[] nums is the parameter for the method. it is saying that there is an array/list of integers that is being passed through
// 21: nums[i] is saying that there is an array and i is used to index that array in a loop. as i changes in the loop,
//     the array is traversed to use the different integers at the different indexes