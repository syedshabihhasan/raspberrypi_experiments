'''
@author: syed shabih hasan

the code explores the function of each pin on the RPi2
'''
import RPi.GPIO as GPIO

def main():
	code_dict = {0: "OUT", 1: "IN", 40: "SERIAL", 41: "SPI", 42: "I2C", 43: "HARD_PWM", -1: "UNKNOWN"}
	GPIO.setmode(GPIO.BOARD)
	pins = range(1, 41)
	for pin in pins:
		try:
			f = GPIO.gpio_function(pin)
			if f in code_dict:
				print("Pin: {}, Function: {}".format(pin, code_dict[f]))
			else:
				print("Pin: {}, Function: UNDEFINED".format(pin))
		except:
			print("Pin: {}, Function: EXCEPTION".format(pin))

if __name__ == "__main__":
	main()