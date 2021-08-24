
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char ** argv)
{
	printf("hello world\n");
	printf("%d argument(s)\n", argc);
	for (int i = 0; i < argc; i++)
	{
		printf("argument %d: %s\n", i, argv[i]);
	}
	
	return EXIT_SUCCESS;
}
