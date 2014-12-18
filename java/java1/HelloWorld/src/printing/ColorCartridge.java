package printing;

/**
 * Created by rwehner on 12/17/14.
 */
public class ColorCartridge implements ICartridge {
    @Override
    public String toString() {
        return "Color!";
    }

    public String getFillPercentage() {
        return "85%";
    }
}
