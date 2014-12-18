package greetings;

import printing.*;

/**
 * Created by rwehner on 12/16/14.
 */
public class HelloWorld {
    public static void main(String[] args)
    {
        //Printer myPrinter = new Printer(true, "My Printer");
        //myPrinter.loadPaper(1);
        //myPrinter.print(1);
        //myPrinter.TurnOff();
        //myPrinter.print(1);
        //myPrinter.printColors();
        //Printer<ColorCartridge> printer = new Printer<ColorCartridge>(true, "My Printer", new ColorCartridge());
        Printer<BWCartridge> printer = new Printer<BWCartridge>(true, "My Printer", new BWCartridge());
        Printer<ColorCartridge> printer2 = new Printer<ColorCartridge>(true, "My Printer", new ColorCartridge());

        printOne(printer);
        printOne(printer2);
    }

    public static void printOne(Printer<? extends ICartridge> printer) {
        String fillPercentage = printer.getCartridge().getFillPercentage();
        System.out.println(fillPercentage);
    }

}
