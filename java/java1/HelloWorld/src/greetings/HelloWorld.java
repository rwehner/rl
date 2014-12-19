package greetings;

import printing.*;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;

/**
 * Created by rwehner on 12/16/14.
 */
public class HelloWorld {
    public static void main(String[] args)
    {
        Printer<ColorCartridge> printer = new Printer<ColorCartridge>(true, "My Printer", ColorCartridge.RED);
        printer.loadPaper(5);
        printer.print(2);
        printer.outputPage(1);

        Path path = Paths.get("/var/tmp/newtest.txt");

        // Creating a empty file - like 'touch'
        try {
            Files.createFile(path);
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Deleting a file
//        try {
//            Files.deleteIfExists(path);
//        } catch (IOException e) {
//            e.printStackTrace();
//        }

        // Moving a file
        Path newPath = Paths.get("/var/tmp/newtest.txt-moved");
        try {
            Files.move(path, newPath);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
