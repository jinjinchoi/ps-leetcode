package BFSDFS.타겟넘버;

import java.util.Arrays;

public class BFSDFS01 {
    public int solution(int[] numbers, int target) {
        int size = numbers.length;
        int sum = 0;
        for(int i=0; i<size; i++) sum += numbers[i];
        if(Math.abs(sum) == Math.abs(target)) return 1;
        else if(Math.abs(sum) < Math.abs(target)) return 0;
        else if(size<2) return 0;

        int plusCase = solution(Arrays.copyOfRange(numbers, 1, size), target - numbers[0]);
        int minusCase = solution(Arrays.copyOfRange(numbers, 1, size), target + numbers[0]);
        return plusCase + minusCase;
    }


}
