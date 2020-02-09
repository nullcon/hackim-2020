clean:
	rm -rf out
	rm b64

dirs:
	mkdir -p out/1 out/2 out/3 out/4

images:
	python2 dora-gen.py

b64:
	./genb64.sh

all: dirs images b64