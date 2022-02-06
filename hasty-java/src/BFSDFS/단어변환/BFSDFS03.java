package BFSDFS.단어변환;

import java.util.HashMap;

public class BFSDFS03 {
    public int solution(String begin, String target, String[] words) {
        HashMap<String, Boolean> markedMap = new HashMap();
        for(String word : words) markedMap.put(word, false);
        if(!markedMap.containsKey(target)) return 0;
        return dfs(begin, target, markedMap);
    }

    public int dfs(String word, String target, HashMap<String, Boolean> markedMap){
        markedMap.put(word, true);
        if(convertible(word, target)) {
            markedMap.put(word, false);
            return 1;
        }
        else{
            for(String candidate : markedMap.keySet()){
                if(!markedMap.get(candidate) && convertible(word, candidate))
                    return dfs(candidate, target, markedMap) + 1;
            }
        }
        return 0;
    }

    public boolean convertible(String fromWord, String toWord){
        int difference = 0;
        for(int i=0; i<fromWord.length(); i++) if (fromWord.charAt(i) != toWord.charAt(i)) difference += 1;
        return difference == 1;
    }
}


class TestBFSDFS03{
    @org.junit.jupiter.api.Test
    public void checkAnswer() {
        String begin1 = "hit";
        String target1 = "cog";
        String[] words1 = {"hot", "dot", "dog", "lot", "log", "cog"};

        String begin2 = "hit";
        String target2 = "cog";
        String[] words2 = {"hot", "dot", "dog", "lot", "log"};

        BFSDFS03 sol = new BFSDFS03();
        System.out.println(String.format("answer %s", sol.solution(begin1, target1, words1)));
        System.out.println(String.format("answer %s", sol.solution(begin2, target2, words2)));
    }
}