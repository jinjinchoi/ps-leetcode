package 탐욕법.체육복;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Set;
import java.util.TreeMap;
import java.util.stream.Collectors;

/**
 * Memo : https://stackoverflow.com/a/1074017
 * ArrayList(Arrays.asList(reserve)) 이런식으로 변환하면
 * List<Integer>가 아닌 List<int[]> 를 만들어버린다,
 * */

public class Greedy01 {
    public int solution(int n, int[] lost, int[] reserve) {
        TreeMap<Integer, Integer> extraClothesCount = new TreeMap<>();
        for(int reserveStudent : reserve) extraClothesCount.put(reserveStudent, extraClothesCount.getOrDefault(reserveStudent, 0)+1);
        for(int lostStudent : lost) extraClothesCount.put(lostStudent, extraClothesCount.getOrDefault(lostStudent, 0)-1);

        Set<Integer> updatedLostStudent = extraClothesCount.entrySet()
                .stream().filter(map -> map.getValue().equals(-1))
                .collect(Collectors.toMap(map -> map.getKey(), map -> map.getValue())).keySet();

        int answer = n - updatedLostStudent.size();
        for(int lostStudent : updatedLostStudent) if (canJoinClass(lostStudent, extraClothesCount)) answer += 1;
        return answer;
    }

    public boolean canJoinClass(int lostStudent, TreeMap<Integer, Integer> extraClothesCount){
        if(extraClothesCount.getOrDefault(lostStudent-1, 0)>0) {
            extraClothesCount.put(lostStudent-1, 0);
            return true;
        }if(extraClothesCount.getOrDefault(lostStudent + 1, 0)>0) {
            extraClothesCount.put(lostStudent+1, 0);
            return true;
        }
        return false;
    }
}


class TestGreedy01{
    @org.junit.jupiter.api.Test
    public void checkAnswer() {
        int n1 = 5;
        int[] lost1 = {2, 4};
        int[] reserve1 = {1, 3, 5};

        int n2 = 5;
        int[] lost2 = {2, 4};
        int[] reserve2 = {3};

        int n3 = 3;
        int[] lost3 = {3};
        int[] reserve3 = {1};

        Greedy01 sol = new Greedy01();
        System.out.println(String.format("answer %s", sol.solution(n1, lost1, reserve1)));
        System.out.println(String.format("answer %s", sol.solution(n2, lost2, reserve2)));
        System.out.println(String.format("answer %s", sol.solution(n3, lost3, reserve3)));
    }
}