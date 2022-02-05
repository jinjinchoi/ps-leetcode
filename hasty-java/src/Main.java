import BFSDFS.타겟넘버.BFSDFS01;
import BFSDFS.타겟넘버.BFSDFS02;
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
        BFSDFS02 sol = new BFSDFS02();

        int numCount1 = 3;
        int[][] computers1 = {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};
        System.out.println(sol.solution(numCount1, computers1)); // 2

        int numCount2 = 3;
        int[][] computers2 = {{1, 1, 0}, {1, 1, 1}, {0, 1, 1}};
        System.out.println(sol.solution(numCount2, computers2)); // 1


        int numCount3 = 4;
        int[][] computers3 = {{1, 0, 0, 1}, {0, 1, 1, 0}, {0, 1, 1, 0}, {1, 0, 0, 1}};
        System.out.println(sol.solution(numCount3, computers3)); // 2

        int numCount4 = 5;
        int[][] computers4 = {{1, 0, 0, 1, 0}, {0, 1, 1, 0, 0}, {0, 1, 1, 0, 0}, {1, 0, 0, 1, 0}, {0, 0, 0, 0, 1}};
        System.out.println(sol.solution(numCount4, computers4)); // 3


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
