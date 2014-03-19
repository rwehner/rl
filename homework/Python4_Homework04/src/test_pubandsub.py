import unittest

from pubandsub import Publisher, SimpleSubscriber

class BasicSubscriber:
    'just captures how it was called'
    def __call__(self, arg):
        self.calledwith = arg
    
def afunction(arg):
    'captures its arg in a global'
    global afunction_calledwith
    afunction_calledwith = arg

class TestPublisher(unittest.TestCase):
    def test_duplicate_subscription(self):
        p = Publisher()
        p.subscribe(None)
        self.assertRaises(ValueError, p.subscribe, None)
        
    def test_unsubscribe_nonexistant_subscriber(self):
        p = Publisher()
        self.assertRaises(ValueError, p.unsubscribe, None)

    def test_subscribe_and_unsubscribe(self):    
        p = Publisher()
        s = (1,2)
        p.subscribe(s)
        self.assertTrue(s in p.subscribers)
        p.unsubscribe(s)
        self.assertFalse(s in p.subscribers)
        
    def test_publish(self):
        p = Publisher()
        s = BasicSubscriber()
        p.subscribe(s)
        p.subscribe(afunction)
        p.publish('hello')
        self.assertEqual(s.calledwith, 'hello')
        self.assertEqual(afunction_calledwith, 'hello')
        
class testSimpleSubscriber(unittest.TestCase):
    "Perhaps the publisher should be a mock in this test?"
    def test_simplesubscriber(self):
        p = Publisher()
        s = SimpleSubscriber('testname', p)
        # test items from __init__()
        self.assertEqual(s.name, 'testname')
        self.assertEqual(s.publisher, p)
        self.assertTrue(s.process in p.subscribers)
        # test __repr__()
        self.assertEqual(str(s), 'testname')
        # process() tests
        output = s.process('hello')
        self.assertEqual(output, "testname:HELLO")
        # should unsub after 3 calls
        for i in range(4):
            output = s.process('hello')
        self.assertFalse(s.process in p.subscribers)

    def test_process_unsubscribes_after_3(self):
        """
        Attempt to make sure that SimpleSubscriber.process()
        unsubscribes itself sanely after 3 calls.
        """
        p = Publisher()
        for i in range(6):
            newsub = SimpleSubscriber("Sub"+str(i), p)
            p.publish(str(i))
            if i == 0:
                self.assertEqual(len(p.subscribers), 1)
                self.assertTrue(str(p.subscribers[0]).endswith("Sub0>"))
            elif i == 1:
                self.assertEqual(len(p.subscribers), 2)
                self.assertTrue(str(p.subscribers[0]).endswith("Sub0>"))
                self.assertTrue(str(p.subscribers[-1]).endswith("Sub1>"))
            else:
                # should never have more than 3 in current settings
                self.assertEqual(len(p.subscribers), 3)
                self.assertTrue(str(p.subscribers[0]).endswith("Sub{0}>".format(i-2)))
                self.assertTrue(str(p.subscribers[1]).endswith("Sub{0}>".format(i-1)))
                self.assertTrue(str(p.subscribers[2]).endswith("Sub{0}>".format(i)))
                 
if __name__ == "__main__":
    unittest.main()