package 해시.완주하지못한선수;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class Hash01 {
    public String solution(String[] participants, String[] completions) {
        HashMap<String,Integer> participantMap = generatePariticipantMap(participants);
        participantMap = compareWithCompletions(completions, participantMap);
        return getDropout(participantMap);
    }

    public HashMap<String,Integer> generatePariticipantMap(String[] participants){
        HashMap<String,Integer> participantMap = new HashMap<>();
        for(String participant : participants) participantMap.put(participant, participantMap.getOrDefault(participant, 0) + 1);
        return participantMap;
    }

    public HashMap<String,Integer> compareWithCompletions(String[] completions, HashMap<String,Integer> participantMap){
        for(String completion : completions) participantMap.put(completion, participantMap.get(completion) - 1);
        return participantMap;
    }

    public String getDropout(HashMap<String,Integer> participantMap){
        Iterator<Map.Entry<String, Integer>> entries = participantMap.entrySet().iterator();
        while(entries.hasNext()){
            Map.Entry<String, Integer> entry = entries.next();
            if(entry.getValue() == 1) return entry.getKey();
        }
        return "";
    }
}
