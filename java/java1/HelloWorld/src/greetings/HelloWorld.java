package greetings;

import printing.*;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class HelloWorld {
    public static void main(String[] args) throws NoSuchMethodException, InvocationTargetException, IllegalAccessException {
        Printer<ColorCartridge> printer = new Printer<ColorCartridge>(true, "My Printer", ColorCartridge.RED);
        printer.loadPaper(10);

        PrintingDevice annotation = printer.getClass().getAnnotation(PrintingDevice.class);
        Method printMethod = printer.getClass().getMethod(annotation.defaultPrintMethod(), int.class);
        printMethod.invoke(printer, annotation.defaultNumberOfCopies());

        printer.outputPage(4);

    }
}
