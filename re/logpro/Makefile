all :
	swipl -o dist/exe --stand_alone=true -g main -c chall.pl
	patchelf --set-rpath ./ dist/exe

clean :
	rm dist/exe