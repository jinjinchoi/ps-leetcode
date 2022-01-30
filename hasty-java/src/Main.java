import 완전탐색.소수찾기.BruteForce02;
import 해시.완주하지못한선수.Hash01;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) {
        Hash01 sol = new Hash01();

        String[] participants1 = {"leo", "kiki", "eden"};
        String[] completions1 = {"eden", "kiki"};
        System.out.println(sol.solution(participants1, completions1)); // "leo"

        String[] participants2 = {"marina", "josipa", "nikola", "vinko", "filipa"};
        String[] completions2 = {"josipa", "filipa", "marina", "nikola"};
        System.out.println(sol.solution(participants2, completions2)); // "vinko"

        String[] participants3 = {"mislav", "stanko", "mislav", "ana"};
        String[] completions3 = {"stanko", "ana", "mislav"};
        System.out.println(sol.solution(participants3, completions3)); // "mislav"
//        executionTime();
    }

    public static void executionTime(){
        File file = new File("/Users/jc/ps-leetcode/hasty-java/src/time.txt");
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
                parse(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void parse(String line){
        String pattern = "테스트 [0-9]+ 〉\t통과 ([0-9]+.[0-9]+ms, [0-9]+.[0-9]+MB)";
//        String pattern = "테스트 [0-9]+ 〉\t통과 ([0-9]+.[0-9]+ms, [0-9]+.[0-9]+MB)";
        String val = line;

        boolean regex = Pattern.matches(pattern, val);
        System.out.println(regex);
    }
}
