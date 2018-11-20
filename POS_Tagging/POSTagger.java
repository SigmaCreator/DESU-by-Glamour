import org.atilika.kuromoji.Token;
import org.atilika.kuromoji.Tokenizer;
import java.io.*;

public class POSTagger {
    public static void main(String[] args) {
        Tokenizer tokenizer = Tokenizer.builder().build();

        try {

            BufferedReader br = new BufferedReader(new FileReader("input.txt")); 

        for (Token token : tokenizer.tokenize(br.readLine())) {
            System.out.println(token.getSurfaceForm() + "\t" + token.getAllFeatures());
        }

        } catch (Exception e) {}
    }
}