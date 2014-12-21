package printing;

public class ContinuousPrinter extends Thread {

    private Printer<ICartridge> printer = new Printer<ICartridge>(false, "Threaded Printer", ColorCartridge.BLUE);

    @Override
    public void run() {
        for(int i = 0; i < 100; i++)
            printer.printUsingCartridge(ColorCartridge.BLUE, "In Thread " + i);

        super.run();
    }
}
