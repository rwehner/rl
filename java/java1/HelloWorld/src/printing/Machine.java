package printing;

/**
 * Created by rwehner on 12/17/14.
 */
public class Machine
{
    protected boolean isOn;

    public Machine(boolean isOn)
    {
        this.isOn = isOn;
    }

    public void TurnOn()
    {
        isOn = true;
        System.out.println("Machine is on!");
    }

    public void TurnOff()
    {
        isOn = false;
    }
}
