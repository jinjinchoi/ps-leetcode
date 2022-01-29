import 완전탐색.소수찾기.BruteForce02;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) {
        BruteForce02 sol = new BruteForce02();

        String numbers1 = "17";
        String numbers2 = "011";
        System.out.println(sol.solution(numbers1));
        System.out.println(sol.solution(numbers2));
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
