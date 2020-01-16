from event import MyBroadcaster, EventHook

myFunction = lambda: print("listener")

theBroadcaster = MyBroadcaster()

# add a listener to the event
theBroadcaster.onChange += myFunction

# remove listener from the event
theBroadcaster.onChange -= myFunction

# fire event
theBroadcaster.onChange.fire()
