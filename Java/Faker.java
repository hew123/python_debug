import java.util.Random;

public class Faker {

    public String letterify(String letterString) {
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        Random random = new Random();
        String result = "";
        for (int i = 0; i < letterString.length(); i++) {
            char current = letterString.charAt(i);
            if (current == '?') {
                char temp = alphabet.charAt(random.nextInt(alphabet.length()));
                result += temp;
            } else {
                result += current;
            }
        }
        return result;
    }

    public String numerify(String numberString) {
        String numbers = "0123456789";
        Random random = new Random();
        String result = "";
        for (int i = 0; i < numberString.length(); i++) {
            char current = numberString.charAt(i);
            if (current == '#') {
                char temp = numbers.charAt(random.nextInt(numbers.length()));
                result += temp;
            } else {
                result += current;
            }
        }
        return result;
    }

    public String bothify(String string) {
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String numbers = "0123456789";
        Random random = new Random();
        String result = "";
        for (int i = 0; i < string.length(); i++) {
            char current = string.charAt(i);
            if (current == '?') {
                char temp = alphabet.charAt(random.nextInt(alphabet.length()));
                result += temp;
            } else if (current == '#') {
                char temp = numbers.charAt(random.nextInt(numbers.length()));
                result += temp;
            } else {
                result += current;
            }
        }
        return result;
    }

}
