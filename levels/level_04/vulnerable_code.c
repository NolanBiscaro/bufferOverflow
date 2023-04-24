// Vulnerable code for level 4
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void level_04_vulnerable_code(char *input) {
    char *buffer = (char *) malloc(64);
    strcpy(buffer, input);
    free(buffer);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }
    level_04_vulnerable_code(argv[1]);
    return 0;
}

// Common secret function for all levels
void secret_function() {
    printf("Exploit successful!\n");
}