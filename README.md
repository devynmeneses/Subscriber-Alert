# Subscriber-Alert
Plays a sound if a chosen YouTube channel has gained a subscriber or not

Packages to install (if not installed):
  urllib
  json
  random
  pygame
  threading
  
NOTES:
1) I don't know how to us GitHub. Sorry
2) Inside the if statement, there is a second if-else statement. In that statement, the if is to check if the channel is over 100 subs, and the second is if the channel is not at 100 subs
3) API key is placed inside key variable
4) Channel username is placed inside username variable
5) Place song file names inside the songs list. One is chosen at random to play everytime a new sub is gained if the channel is over 100 subs
6) Place basic alert sound into the else statement in the second if statement. This will play the sound if the channel has less than a 100 subs
