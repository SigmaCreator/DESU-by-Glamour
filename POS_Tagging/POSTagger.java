import org.atilika.kuromoji.Token;
import org.atilika.kuromoji.Tokenizer;

public class POSTagger {
    public static void main(String[] args) {
        Tokenizer tokenizer = Tokenizer.builder().build();
        for (Token token : tokenizer.tokenize(args[0])) {
            System.out.println(token.getSurfaceForm() + "\t" + token.getAllFeatures());
        }
    }
}