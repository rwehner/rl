package printing;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Created by rwehner on 12/16/14.
 */
public class Printer<T extends  ICartridge> implements IMachine
{
    private String modelNumber;
    private PaperTray paperTray = new PaperTray();
    private Machine machine;
    private T cartridge;
    //private List<Page> pages = new ArrayList<Page>();
    private Map<Integer, Page> pagesMap = new HashMap<Integer, Page>();


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
        String textToPrint = getTextFromfile();

        if(paperTray.isEmpty())
            System.out.println("Load more paper.");

        int pageNumber = 1;
        while (copies > 0 && !paperTray.isEmpty())
        {
            //System.out.println(textToPrint);
            //pages.add(new Page(textToPrint));
            pagesMap.put(pageNumber, new Page(textToPrint + ":" + pageNumber));
            copies--;
            paperTray.usePage();
            pageNumber++;
        }

    }

    private String getTextFromfile() {
        FileReader reader = null;
        BufferedReader bReader = null;

        CapitalizationReader capReader = null;



        String allText = "";
        try {
            reader = new FileReader("/var/tmp/test.txt");
            bReader = new BufferedReader(reader);
            capReader = new CapitalizationReader(bReader);

            String line;
            while((line = capReader.readLine() ) != null) {
                allText += line + "\n";
            }
            return allText;

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if(capReader != null) {
                try {
                    capReader.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
        return "";
    }

    public void getPage(int pageNumber) {
        System.out.println(pagesMap.get(pageNumber).getText());

    }

    public void getPages() {
        int pageCount = pagesMap.size();
        for(int i=1; i<=pageCount; i++) {
            getPage(i);
        }
    }
    public void outputPage(int pageNumber) {
        PrintWriter writer = null;
        try {
            writer = new PrintWriter(new FileWriter("/var/tmp/outputpage.txt"));
            writer.println(pagesMap.get(pageNumber).getText());
        } catch (IOException e) {
            e.printStackTrace();
        }
        finally {
            if(writer != null)
                writer.close();
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
