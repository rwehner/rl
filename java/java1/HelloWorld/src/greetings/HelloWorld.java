package greetings;

import printing.IMachine;
import printing.Printer;

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
        IMachine machine = new Printer(true, "My Printer");

        machine.TurnOn();

    }

}
