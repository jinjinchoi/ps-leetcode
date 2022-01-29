package 완전탐색.소수찾기;

import java.util.*;

public class BruteForce02 {
    Set<Integer> combinationSet = new HashSet<>();

    public int solution(String numbers) {
        int answer = 0;
        String combination = "";
        getCombinations(combination, numbers, combinationSet);

        for(int comb : combinationSet){
            if(isPrime(comb)) answer += 1;
        }

        return answer;
    }

    public void getCombinations(String current, String remaining, Set<Integer> combinationSet){
        if(current!="") combinationSet.add(Integer.parseInt(current));
        for(int i = 0; i<remaining.length(); i++){
            String updatedCurrent = current + remaining.charAt(i);
            String updatedRemaining = remaining.substring(0, i) + remaining.substring(i+1);
            getCombinations(updatedCurrent, updatedRemaining, combinationSet);
        }
    }

    public boolean isPrime(int number){
        if(number<2) return false;
        else if (number == 2 || number == 3) return true;
        else if (number%2 == 0) return false;

        int sqrt = (int) Math.sqrt(number);
        for(int dividend = 3; dividend<=sqrt; dividend+=2){
            if(number%dividend==0) return false;
        }
        return true;
    }
}
