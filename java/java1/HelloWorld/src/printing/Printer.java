package printing;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by rwehner on 12/16/14.
 */
public class Printer<T> implements IMachine
{
    private String modelNumber;
    private PaperTray paperTray = new PaperTray();
    private Machine machine;
    private T cartridge;
    private List<Page> pages = new ArrayList<Page>();


    public Printer(boolean isOn, String modelNumber, T cartridge)
    {
        machine = new Machine(isOn);
        this.modelNumber = modelNumber;
        this.cartridge = cartridge;
    }

    public T getCartridge() {
        return cartridge;
    }

    @Override
    public void TurnOn()
    {
        System.out.println("Warm up printer.");
        machine.TurnOn();
    }

    @Override
    public void TurnOff()
    {
        machine.TurnOff();
    }

    @Override
    public boolean isOn() {
        return machine.isOn();
    }

    public <U extends ICartridge> void printUsingCartridge(U cartridge, String message) {
        System.out.println(cartridge.getFillPercentage());
        System.out.println(message);
        System.out.println(cartridge.toString());
    }

    public void print(int copies)
    {
        checkCopies(copies);

        String onStatus = getStatusString();
        String textToPrint = modelNumber + " is " + onStatus.toLowerCase() + ".";

        if(paperTray.isEmpty())
            System.out.println("Load more paper.");

        while (copies > 0 && !paperTray.isEmpty())
        {
            //System.out.println(textToPrint);
            pages.add(new Page(textToPrint));
            copies--;
            paperTray.usePage();
        }

    }

    public void outputPages() {
        for(Page currentPage : pages) {
            System.out.println(currentPage.getText());
        }
    }

    public String getStatusString() {
        String onStatus = "";
        if(machine.isOn())
        {
            onStatus = "ON";
        }
        else
        {
            onStatus = "OFF";
        }
        return onStatus;
    }

    private void checkCopies(int copies) {
        if(copies < 0)
            throw new IllegalArgumentException("Can't print fewer than 0 copies.");
    }

    public void printColors()
    {
        String[] colors = new String[]{"Red", "Blue", "Green", "Yellow", "Orange"};

        for (String currentColor : colors)
        {
            if ("Green".equals(currentColor)) {
                continue;
            }
            System.out.println(currentColor);
        }
    }

    private void print(String text)
    {
        System.out.println(text);
    }

    public String getModelNumber() {
        return modelNumber;
    }

    public void loadPaper(int sheets) {
        paperTray.addPaper(sheets);
    }
}
