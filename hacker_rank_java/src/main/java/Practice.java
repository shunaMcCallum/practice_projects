import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Practice {
        // determine how many pairs of numbers are in the array
        // ignore any spares

        // loop - search array for matching numbers
        // count each matching number
        // take the final count and divide by 2 and round down
        // if no matching numbers, ignore
    public static int sockMerchant(List<Integer> ar) {
        double counter = 0.0;
        int result = 0;
        Set<Integer> set = new HashSet<>(ar);

        for (int num1 = 0; num1 < set.size(); num1++) {
            for (int num2 = 0; num2 < ar.size(); num2++) {
                if (num1 == num2) {
                    counter += 1.0;
                }
            }
            if (counter > 1.0) {
                double num = counter = 1.0;
                result += (int) Math.floor(num / 2);
            }
        }
        return result;
    }
}
