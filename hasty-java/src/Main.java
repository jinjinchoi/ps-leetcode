import 완전탐색.소수찾기.BruteForce02;
import 해시.완주하지못한선수.Hash01;
import 해시.전화번호목록.Hash02;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) {
        Hash02 sol = new Hash02();

        String[] phoneBook1 = {"119", "97674223", "1195524421"};
        System.out.println(sol.solution(phoneBook1)); // false

        String[] phoneBook2 = {"123","456","789"};
        System.out.println(sol.solution(phoneBook2)); // true

        String[] phoneBook3 = {"12","123","1235","567","88"};
        System.out.println(sol.solution(phoneBook3)); // false

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
