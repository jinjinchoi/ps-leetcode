package 정렬.가장큰수;

import java.util.*;

public class SortingQ2 {
    public String solution(int[] numbers) {
        String answer = "";
        TreeMap<String, ArrayList<String>> numberMap = new TreeMap<>(Collections.reverseOrder());
        for(int number : numbers){
            String firstDigit = String.valueOf(number).substring(0,1);
            ArrayList<String> numberList = numberMap.getOrDefault(firstDigit, new ArrayList<>());
            numberList.add(String.valueOf(number));
            numberMap.put(firstDigit, numberList);
        }

        for (String key : numberMap.keySet()){
            answer += getSortedString(numberMap.get(key).toArray(new String[]{}));
        }

        if(answer.startsWith("0")) return "0";
        return answer;
    }

    // 5, 50, 54, 56 -> 56 5 54 50
    // 3(33), 30(3), 34(3) -> 34 3 30
    // 5(55), 50(5), 55(5), 555, 551 -> 555 55 5 551 50
    public String getSortedString(String[] numberArray){
        Arrays.sort(
                numberArray, (o1, o2) -> (o2+o1).compareTo(o1+o2)
        );
        String concatenatedString = "";
        for(String numberStr : numberArray) concatenatedString += numberStr;
        return concatenatedString;
    }
}
