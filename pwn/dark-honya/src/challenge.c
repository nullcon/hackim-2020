// House of Unsorted Einherjar
// Have null byte heap overflow
// there will be no "show" functionality to disable leaks
// no RELRO and no PIE to make users use unsorted bin into bss to get RCE

// momoku no honya
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 0xf8
#define MAX_BOOKS 16

char name[SIZE];

struct Book {
	char name[SIZE];
};

struct Book *books[MAX_BOOKS];

int readint()
{
        char buf[SIZE];
        if(fgets(buf, SIZE, stdin) == NULL)
                return -1;
        return atoi(buf);
}

void readstr(char* buf)
{
        int bytes_read;
        bytes_read = read(0, buf, SIZE);
        if (bytes_read == -1)
                puts("Err read string");

        buf[bytes_read] = '\0';
}


void buy()
{
	int idx;
	for (idx=0; books[idx]!=NULL; idx++){}

	if (idx >= MAX_BOOKS)
	{
		puts("Next time bring a bag with you!");
		return;
	}
	struct Book *book = (struct Book *)malloc(sizeof(struct Book));
	puts("Name of the book?");
	readstr(book->name);
	books[idx] = book;
}

void write_inside()
{
	unsigned int idx = readint();

        if (idx >= MAX_BOOKS)
        {
                puts("Writing in the air now?");
                return;
        }
        puts("Name of the book?");
        struct Book *book = books[idx];
	readstr(book->name);
}

void put_back()
{
	puts("Which book do you want to return?");
	unsigned int idx = readint();
	if(idx >= MAX_BOOKS)
	{
		puts("boy, you cannot return what you dont have!");
	}
	free(books[idx]);
	books[idx] = NULL;
}

void menu()
{
	puts("----- BookStore -----");
	puts("1) Buy a book");
	puts("2) Put it back");
	puts("3) Write inside a book");
	puts("4) Read the book");
	puts("5) Checkout!");
}

void init()
{
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
}

void get_name()
{
	puts("----- BookStore -----");
	puts("finally! a customer, what is your name?");
	readstr(name);
	puts(name);
	printf("Welcome %s\n", name);
}

int main(int argc, char **argv)
{
	int opt;
	init();
	get_name();
	while(1)
	{
		menu();
		opt = readint();
		switch(opt)
		{
			case 1:
				buy();
				break;
			case 2:
				put_back();
				break;
			case 3:
				write_inside();
				break;
			case 4:
				puts("Reading is not allowed before checkout");
				exit(0);
			case 5:
				puts("Come again :)");
				return 0;
			default:
				puts("Hey! what do you think you are doing?");
				exit(0);
		}
	}
}
