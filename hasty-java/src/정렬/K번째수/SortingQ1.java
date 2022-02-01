package 정렬.K번째수;

import java.util.ArrayList;
import java.util.Arrays;

public class SortingQ1 {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for(int commandIndex=0; commandIndex<commands.length; commandIndex++){
            int i = commands[commandIndex][0];
            int j = commands[commandIndex][1];
            int k = commands[commandIndex][2];
//            System.out.println(String.format("i: %d, j: %d, k: %d", i, j, k));
            answer[commandIndex] = sliceAndSortArray(array, i, j)[k-1];
//            System.out.println(String.format("sliceAndSortArray %s", Arrays.toString(sliceAndSortArray(array, i, j))));
//            System.out.println(String.format("answer[%d]: %d", commandIndex, sliceAndSortArray(array, i, j)[k-1]));
        }
        return answer;
    }

    public int[] sliceAndSortArray(int[] array, int i, int j){
        int[] subList = Arrays.copyOfRange(array, i-1, j);
        Arrays.sort(subList);
        return subList;
    }
}