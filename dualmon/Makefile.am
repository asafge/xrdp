#Make FakeXinerama 

all: libXinerama.so.1.0.0

libXinerama.so.1.0.0:
	$(CC) $(LDFLAGS) -O2 -Wall Xinerama.c -fPIC -o libXinerama.so.1.0.0 -shared

clean:
	rm -f libXinerama.so.1.0.0

install:
	mkdir -p /usr/local/lib/fakeXinerama
	cp libXinerama.so.1.0.0 /usr/local/lib/fakeXinerama
	ln -f -s /usr/local/lib/fakeXinerama/libXinerama.so.1.0.0 /usr/local/lib/fakeXinerama/libXinerama.so
	ln -f -s /usr/local/lib/fakeXinerama/libXinerama.so.1.0.0 /usr/local/lib/fakeXinerama/libXinerama.so.1

#Add to dynamic linker
	echo "/usr/local/lib/fakeXinerama" >> /etc/ld.so.conf.d/fakeXinerama.conf
	ldconfig
		
uninstall:
	rm -rf /usr/local/lib/fakeXinerama 
	rm -rf /etc/ld.so.conf.d/fakeXinerama.conf
	ldconfig
