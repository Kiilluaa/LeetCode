public class DailyScores {
    public static void main(String[] args) {
        int[] scores = {82, 91, 76, 95};

        scores[2] = 80;

        System.out.println(scores[0]);
        System.out.println(scores[2]);
        System.out.println(scores.length);

        int[] nums = {4, 7, 9};

        System.out.println(nums[0]);
        System.out.println(nums[nums.length - 1]);

        nums[1] = 100;

        // 9: array of integers 'int[]'

        // 10: int

        // 11: 5

        // 12: the index starts at 0. the length is one too long

        String[] colors = {"red", "green", "blue"};

        System.out.println(colors[1]);
    }
}
