import BFSDFS.타겟넘버.BFSDFS01;
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
        BFSDFS01 sol = new BFSDFS01();


        int[] numbers1 = {1, 1, 1, 1, 1};
        int target1 = 3;
        System.out.println(sol.solution(numbers1, target1)); // 5

        int[] numbers2 = {4, 1, 2, 1};
        int target2 = 4;
        System.out.println(sol.solution(numbers2, target2)); // 2

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
