package printing;

/**
 * Created by rwehner on 12/16/14.
 */
public class Printer implements IMachine
{
    private String modelNumber;
    private PaperTray paperTray = new PaperTray();
    private Machine machine;


    public Printer(boolean isOn, String modelNumber)
    {
        machine = new Machine(isOn);
        this.modelNumber = modelNumber;
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

    public void print(int copies)
    {

        String onStatus = "";
        if(machine.isOn())
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

    public void loadPaper(int sheets) {
        paperTray.addPaper(sheets);
    }
}
