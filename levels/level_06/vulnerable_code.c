// Vulnerable code for level 6
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void level_06_vulnerable_code(unsigned int size, char *input) {
    char *buffer = (char *) malloc(size);
    memcpy(buffer, input, size);
    free(buffer);
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <size> <input>\n", argv[0]);
        return 1;
    }
    unsigned int size = atoi(argv[1]);
    level_06_vulnerable_code(size, argv[2]);
    return 0;
}

// Common secret function for all levels
void secret_function() {
    printf("Exploit successful!\n");
}