/**
 * Created by rwehner on 12/17/14.
 */
public class FirstSample
{
    public static void main(String[] args)
    {
        String greeting = "We will not use 'Hello World!'";
        System.out.println(greeting);
        System.out.println(greeting.substring(16));
        double x = 2;
        double y = Math.pow(x, 2);
        System.out.println(y);

        String filename = "Monkey.txt";
        if(filename.endsWith(".txt"))
        {
            System.out.println(filename.replace(".txt", "").toUpperCase());
        }
    }
}
