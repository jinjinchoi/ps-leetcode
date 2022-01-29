import java.util.ArrayList;
import java.util.List;

/**
 * [PROGRAMMERS] 코딩테스트 연습>완전탐색>모의고사
 * https://programmers.co.kr/learn/courses/30/lessons/42840?language=java
 * */
class BruteForceQ1 {
    int[][] patterns = {
            {1,2,3,4,5},
            {2, 1, 2, 3, 2, 4, 2, 5},
            {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
    };
    int[] patternSizes = {5, 8, 10};

    public int[] solution(int[] answers) {
        int scorePersonOne = getScore(answers, 0);
        int scorePersonTwo = getScore(answers, 1);
        int scorePersonThree = getScore(answers, 2);
        int[] scores = {scorePersonOne,scorePersonTwo, scorePersonThree};
        int[] answer = getSmartestPeople(scores);
        return answer;
    }

    public int getScore(int[] answers, int personId){
        int numQuestions = answers.length;
        int score = 0;
        for(int i=0; i<numQuestions; i++){
            int[] pattern = patterns[personId];
            int patternSize = patternSizes[personId];
            if(pattern[i % patternSize] == answers[i]) score+=1;
        }
        return score;
    }

    public int[] getSmartestPeople(int[] scores){
        int numPeople = scores.length;
        int highestScore = scores[0];
        List<Integer> smartPeople = new ArrayList<>();
        for(int i=0; i<numPeople; i++){
            if(highestScore < scores[i]) {
                highestScore = scores[i];
                smartPeople.clear();
                smartPeople.add(i+1);
            }else if(highestScore == scores[i]){
                smartPeople.add(i+1);
            }
        }
        int[] answer = new int[smartPeople.size()];
        int cnt = 0;
        for(int num : smartPeople) answer[cnt++] = num;
        return answer;
    }
}