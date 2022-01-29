import java.util.*;

class BruteForce02 {

    public int solution(String numbers) {
        int answer = 0;
        String combination = "";
        Set<Integer> combinationSet = new HashSet<>();
        getCombinations(combination, numbers, combinationSet);
        for(int comb : combinationSet){
//            System.out.println(String.format("comb: %s", comb));
            if(isPrime(comb)) {
//                System.out.println(String.format("prime: %s", comb));
                answer += 1;
            }
        }
        return answer;
    }

    public Set<Integer> getCombinations(String current, String remaining, Set<Integer> combinationSet){
//        System.out.println(String.format("current: %s, remaining %s", current, remaining));
        for(int i = 0; i<remaining.length(); i++){
            String updatedCurrent = current + remaining.charAt(i);
            String updatedRemaining = remaining.substring(0, i) + remaining.substring(i+1);
            combinationSet.add(Integer.parseInt(updatedCurrent));
//            System.out.println(String.format("updatedCurrent: %s", updatedCurrent));
            getCombinations(updatedCurrent, updatedRemaining, combinationSet);
        }
        return combinationSet;
    }

    public boolean isPrime(int number){
        if(number<2) return false;
        else if (number == 2 || number == 3) return true;
        else if (number%2==0) return false
        for(int dividend = 3; dividend<=Math.sqrt(number); dividend+=2){
            if(number%dividend==0) return false;
        }
        return true;
    }
}
