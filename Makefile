CFLAGS += -Wall -I../include -I ./include -L../lib -os

all: playback.exe

data.h:
	python3 convert.py
	xxd -i data > data.h

playback: playback.c data.h
	gcc $(CFLAGS) -o playback playback.c

playback.exe: playback.c data.h
	i686-w64-mingw32-gcc $(CFLAGS) -o playback.exe playback.c

clean:
	rm -f data
	rm -f data.h
	rm -f playback
	rm -f playback.exe