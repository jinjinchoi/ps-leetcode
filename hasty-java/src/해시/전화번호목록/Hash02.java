package 해시.전화번호목록;

import java.util.*;

public class Hash02 {

    public boolean solution(String[] phone_book) {
        HashMap<String, Boolean> phone_book_map = new HashMap<>();
        for(String phone_number: phone_book) phone_book_map.put(phone_number, true);

        for(String phone_number: phone_book_map.keySet()){
            if(checkIfPrefixExists(phone_number, phone_book_map.keySet())) return  false;
        }
        return true;
    }

    public boolean checkIfPrefixExists(String phone_number, Set<String> phone_list){
        for(int i=1; i<phone_number.length(); i++){
            if(phone_list.contains(phone_number.substring(0, phone_number.length()-i))) return true;
        }
        return false;
    }
}
