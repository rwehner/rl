class Publisher:
    def __init__(self):
        self.subscribers = []
        
    def subscribe(self, subscriber):
        if subscriber in self.subscribers:
            raise ValueError("Multiple subscriptions are not allowed")
        self.subscribers.append(subscriber)
        
    def unsubscribe(self, subscriber):
        if subscriber not in self.subscribers:
            raise ValueError("Can only unsubscribe subscribers")
        self.subscribers.remove(subscriber)
        
    def publish(self, s):
        # create a separate list for iteration so
        # unsubscribe events don't break this.
        for subscriber in self.subscribers[:]:
            subscriber(s)
            
class SimpleSubscriber:
    def __init__(self, name, publisher):
        self.name = name
        self.publisher = publisher
        publisher.subscribe(self.process)
        self.process_called_count = 0
    
    def process(self, s):
        if self.process_called_count >= 3:
            try:
                self.publisher.unsubscribe(self.process)
            except ValueError:
                pass
        else:
            self.process_called_count += 1
            output = "{0}:{1}".format(self.name, s.upper())
            # a little hack to make this function more testable
            if __name__ == "__main__":
                print(output)
            else:
                return output  
        
    def __repr__(self):
        return self.name

if __name__ == "__main__":
    def multiplier(s):
        print(2*s)
        
    publisher = Publisher()
    publisher.subscribe(multiplier)
    for i in range(6):
        newsub = SimpleSubscriber("Sub"+str(i), publisher)
        line = input("Input {}: ".format(i))
        publisher.publish(line)