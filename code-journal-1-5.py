import numpy as np 

def main():
	x = np.linspace(0.0, 2*np.pi, num=1000)
	sinx = np.sin(x) 

	print(f"   x   | sin(x)")
	print("----------------")
	for i in range(10):
		print(f"{x[i]:.5f}|{sinx[i]:.5f}")

if __name__=="__main__":
	main()