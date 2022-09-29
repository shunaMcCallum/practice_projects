import java.util.*;

public class Runner {

    public static void main(String[] args) {
//        List<Integer> list = Arrays.asList(10, 20, 20, 10, 30, 10, 20);
//        System.out.println(sockMerchant(list));
        String s = "www.abc.xy";
        System.out.println(caesarCipher(s, 87));

//        fff.jkl.gh

    }

    public static String caesarCipher(String s, int k) {
        char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        char[] string = s.toCharArray();
        // length = 26
        // k = 87
        // x = 24 ==> 0
        // x = 25 ==> 1
        // x = 25 ==> 2

        // length + k - 26

        boolean wasUpperCase = false;

        if (k > 26) {
            k = k % 26;
        }

        for (int i = 0; i < string.length; i++) {
            if (Character.isUpperCase(string[i])) {
                wasUpperCase = true;
                string[i] = Character.toLowerCase(string[i]);
            }
            for (int x = 0; x < alphabet.length; x++) {


                if (string[i] == alphabet[x]) {
                    if (x + k >= alphabet.length) {
                        int num = (x + k) - (alphabet.length);
                        string[i] = alphabet[num];
                        break;
                    } else if (x + k < alphabet.length) {
                        int num = x + k;
                        string[i] = alphabet[num];
                        break;
                    }
                }
            }
            if (wasUpperCase) {
                string[i] = Character.toUpperCase(string[i]);
                wasUpperCase = false;
            }
        }

        System.out.println(string);

        return string.toString();

    }
}
//
//    public static int sockMerchant(List<Integer> ar) {
//        double counter = 0.0;
//        int result = 0;
//        Set<Integer> set = new HashSet<>(ar);
//        List<Integer> list = new ArrayList<>(set);
//
//        for (int num1 = 0; num1 < list.size(); num1++) {
//            for (int num2 = 0; num2 < ar.size(); num2++) {
//                if (Objects.equals(list.get(num1), ar.get(num2))) {
//                    counter += 1.0;
//                }
//            }
//
//            if (counter > 1.0) {
//                result += (int) Math.floor(counter / 2);
//            }
//            counter = 0.0;
//        }
//        return result;
//    }


