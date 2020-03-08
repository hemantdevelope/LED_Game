import RPi.GPIO as GPIO
import time

Score1 = 0
Score2 = 0

Player1Name = input("Enter player1Name: ")
Player2Name = input("Enter player2Name: ")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(12,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(15,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(16,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(18,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(22,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(32,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(33,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(35,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(36,GPIO.OUT,initial=GPIO.LOW)


def workButton1(channel):
    if (GPIO.input(11) == True):
        global Score1
        Score1 = Score1 + 1

def workButton2(channel):
    if (GPIO.input(36) == True):
        global Score2
        Score2 = Score2 + 1
        
GPIO.setup(29,GPIO.IN,pull_up_down = GPIO.PUD_UP) #setting pin 29 as input and pull up resistor as up
GPIO.setup(31,GPIO.IN,pull_up_down = GPIO.PUD_UP) #setting pin 31 as input and pull up resistor as up

GPIO.add_event_detect(29,GPIO.FALLING,callback= workButton1, bouncetime =150) #setting interrupt for pin 29 
GPIO.add_event_detect(31,GPIO.FALLING,callback= workButton2, bouncetime =150) #setting interruot for pin 31




def impact():
    GPIO.output(11,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(15,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(22,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(11,GPIO.LOW)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(16,GPIO.LOW)
    GPIO.output(18,GPIO.LOW)
    GPIO.output(22,GPIO.LOW)

    
def listenRestart():
    if (GPIO.input(29) == True and GPIO.input(31) == True):
        impact()
        Score1 =0
        Score2 =0
         





def results():
    print("Player1 %s score is >> %d "%(Player1Name,Score1))
    print("player2 %s score is >> %d "%(Player2Name,Score2))
    time.sleep(1)
    for i in range(Score1):
        GPIO.output(36,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(36,GPIO.LOW)
        time.sleep(1)

    time.sleep(3)
    for J in range(Score2):
        GPIO.output(11,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(11,GPIO.LOW)
        time.sleep(1)

        
count =0

time.sleep(1)
while count < 10:

    GPIO.output(11,GPIO.HIGH)
    time.sleep(.08)
    GPIO.output(11,GPIO.LOW)
    time.sleep(.08)

    GPIO.output(12,GPIO.HIGH)    
    time.sleep(.08)
    GPIO.output(12,GPIO.LOW)
    time.sleep(.08)
    

    GPIO.output(15,GPIO.HIGH)
    time.sleep(.08)
    GPIO.output(15,GPIO.LOW)
    time.sleep(.08)
    

    GPIO.output(16,GPIO.HIGH)
    time.sleep(.08)
    GPIO.output(16,GPIO.LOW)
    time.sleep(.08)
    

    GPIO.output(18,GPIO.HIGH)
    time.sleep(.08)
    GPIO.output(18,GPIO.LOW)
    time.sleep(.08)
    

    GPIO.output(22,GPIO.HIGH)
    time.sleep(.08)
    GPIO.output(22,GPIO.LOW)
    time.sleep(.08)

    GPIO.output(32,GPIO.HIGH)
    time.sleep(.08)
    GPIO.output(32,GPIO.LOW)
    time.sleep(.08)

    GPIO.output(33,GPIO.HIGH)
    time.sleep(.08)
    GPIO.output(33,GPIO.LOW)
    time.sleep(.08)

    GPIO.output(35,GPIO.HIGH)
    time.sleep(.08)
    GPIO.output(35,GPIO.LOW)
    time.sleep(.08)

    GPIO.output(36,GPIO.HIGH)
    time.sleep(.08)
    GPIO.output(36,GPIO.LOW)
    time.sleep(.08)

    #reversing pattern

    GPIO.output(35,GPIO.HIGH)
    time.sleep(.08)
    GPIO.output(35,GPIO.LOW)
    time.sleep(.08)

    GPIO.output(33,GPIO.HIGH)
    time.sleep(.08)
    GPIO.output(33,GPIO.LOW)
    time.sleep(.08)

    GPIO.output(32,GPIO.HIGH)
    time.sleep(.08)
    GPIO.output(32,GPIO.LOW)
    time.sleep(.08)

    GPIO.output(22,GPIO.HIGH)
    time.sleep(.08)
    GPIO.output(22,GPIO.LOW)
    time.sleep(.08)
    
    GPIO.output(18,GPIO.HIGH)
    time.sleep(.08)
    GPIO.output(18,GPIO.LOW)
    time.sleep(.08)
    

    GPIO.output(16,GPIO.HIGH)
    time.sleep(.08)
    GPIO.output(16,GPIO.LOW)
    time.sleep(.08)
    

    GPIO.output(15,GPIO.HIGH)
    time.sleep(.08)
    GPIO.output(15,GPIO.LOW)
    time.sleep(.08)
    

    GPIO.output(12,GPIO.HIGH)
    time.sleep(.08)
    GPIO.output(12,GPIO.LOW)
    time.sleep(.08)
    

    
    if count == 10 :
        GPIO.output(11,GPIO.HIGH)
        time.sleep(.08)
        GPIO.output(11,GPIO.LOW)
        time.sleep(.08)
    count += 1

print("The count is: ",count)   
results()
GPIO.cleanup()

