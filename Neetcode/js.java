
import java.util.HashMap;

public class js {

    public static void main(String[] args) {
        String s1 = "egg";
        String s2 = "add";

        HashMap<Character, Character> list_arr = new HashMap<>();

        for (int i = 0; i < s1.length(); i++) {
            list_arr.put(s1.charAt(i), s2.charAt(i));
        }

        for (int j = 0; j < list_arr.size(); j++) {
            for (int k = j + 1; k < list_arr.size(); k++) {

            }
        }
    }
}
