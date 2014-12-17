package printing;

/**
 * Created by rwehner on 12/17/14.
 */
public class PaperTray
{
    int pages = 0;

    public void addPaper(int count)
    {
        pages += count;
    }

    public void usePage()
    {
        pages--;
    }

    public boolean isEmpty()
    {
        return pages < 1;
    }
}
