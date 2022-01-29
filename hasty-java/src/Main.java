import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] answer1 = {1,2,3,4,5};
        int[] answer2 = {1,3,2,4,2};
        System.out.println(Arrays.toString(sol.solution(answer1)));
        System.out.println(Arrays.toString(sol.solution(answer2)));
        executionTime();
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
