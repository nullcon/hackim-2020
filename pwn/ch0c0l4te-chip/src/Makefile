all:
	gcc -O0 -fno-stack-protector -no-pie main.c rng.c -o main \
		-Wno-shift-count-overflow \
		-Wno-integer-overflow
