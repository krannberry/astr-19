import sys

class Frog: 

		def print(self):
			print (f"length of arms = {self.arm_length}")
			print (f"length of legs= {self.leg_length}")
			print (f"number of eyes= {self.num_eyes}")
		
			if self.tail: 
				print("tail")
			else: 
				print("no tail")

			if self.furry:
				print("furry")
			else: 
				print("not furry")

		def __init__(self, arm_length=4, leg_length=6, num_eyes=2, tail=False, furry=False):
			self.arm_length = float(arm_length)
			self.leg_length = float(leg_length)			
			self.num_eyes = int(num_eyes)
			self.tail = bool(tail)
			self.furry = bool(furry)

			print(f"My favorite animal is a Frog!")	

def main():
	arm_length = 3 
	leg_length = 10. 

	if(len(sys.argv)>=2):
		arm_length = int(sys.argv[1])

	if(len(sys.argv)>=3):
		leg_length = float(sys.argv[2])

	frog = characteristics(arm_length=arm_length, leg_length=leg_length)

	frog.print()

def main():
    arm_length = 4
    leg_length = 6
    num_eyes = 2

    if len(sys.argv) >= 2:
        arm_length = int(sys.argv[1])

    if len(sys.argv) >= 3:
        leg_length = float(sys.argv[2])

    if len(sys.argv) >= 4:
        num_eyes = int(sys.argv[3])

    frog = Frog(arm_length=arm_length, leg_length=leg_length, num_eyes=2)
    frog.print()

if __name__ == "__main__":
    main()