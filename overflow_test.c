#include <string.h>
#include <stdio.h>

void overflowed() {
	printf("%s\n", "Execution Hijacked");
}

void function (char *stc) {
	char buffer[5];
	strcpy(buffer, str);
}

void main (int argc, char *argv[]) {
	function(argv[1]);
	printf("%s\n", "Executed normally");
}
	
