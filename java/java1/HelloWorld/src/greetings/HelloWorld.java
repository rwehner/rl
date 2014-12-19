package greetings;

import printing.*;

import java.io.File;
import java.io.IOException;
import java.util.*;

/**
 * Created by rwehner on 12/16/14.
 */
public class HelloWorld {
    public static void main(String[] args)
    {
        Printer<ColorCartridge> printer = new Printer<ColorCartridge>(true, "My Printer", ColorCartridge.RED);
//        printer.loadPaper(5);
//        printer.print(2);
//        printer.getPages();

        for(ColorCartridge cartridge : ColorCartridge.values()) {
            System.out.println(cartridge.printColor());
        }

    }
}
