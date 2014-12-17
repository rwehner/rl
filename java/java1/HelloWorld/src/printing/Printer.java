package printing;

/**
 * Created by rwehner on 12/16/14.
 */
public class Printer extends Machine
{
    private String modelNumber;
    private PaperTray paperTray = new PaperTray();

    public Printer(boolean isOn, String modelNumber)
    {
        super(isOn);
        this.modelNumber = modelNumber;
    }

    @Override
    public void TurnOn()
    {
        System.out.println("Warming up printer.");
        super.TurnOn();
    }

    public void print(int copies)
    {

        String onStatus = "";
        if(isOn)
        {
            onStatus = " is on.";
        }
        else
        {
            onStatus = " is off.";
        }
        String textToPrint = modelNumber + onStatus;


        if(paperTray.isEmpty())
            System.out.println("Load more paper.");

        while (copies > 0 && !paperTray.isEmpty())
        {
            System.out.println(textToPrint);
            copies--;
            paperTray.usePage();
        }

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

    public boolean getIsOn() {
        return isOn;
    }

    public void loadPaper(int sheets) {
        paperTray.addPaper(sheets);
    }
}
