package printing;

/**
 * Created by rwehner on 12/18/14.
 */
public class Page {
    private String printedText;

    public Page(String text) {

        printedText = text;
    }

    public String getText() {
        return printedText;
    }

}
