import 완전탐색.소수찾기.BruteForce02;
import 정렬.K번째수.SortingQ1;
import 정렬.가장큰수.SortingQ2;
import 해시.완주하지못한선수.Hash01;
import 해시.전화번호목록.Hash02;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) {
        SortingQ2 sol = new SortingQ2();

        int[] numbers1 = {0, 1, 11, 12, 110};
        int[] numbers2 = {3, 30, 56, 5, 9};
        int[] numbers3 = {3, 30, 34, 5, 50, 54, 56, 9};

        System.out.println(sol.solution(numbers1)); // "121111100"
        System.out.println(sol.solution(numbers2)); // "9565330"
        System.out.println(sol.solution(numbers3));

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
