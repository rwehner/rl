package printing;

/**
 * Created by rwehner on 12/17/14.
 */
public class BWCartridge implements ICartridge {
    @Override
    public String toString() {
        return "Black and White!";
    }

    public String getFillPercentage() {
        return "50%";
    }
}
