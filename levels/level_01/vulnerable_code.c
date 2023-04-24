#include <stdio.h>
#include <string.h>

void level_01_vulnerable_code(char *input) {
    char buffer[64];
    strcpy(buffer, input);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }
    level_01_vulnerable_code(argv[1]);
    return 0;
}

// Common secret function for all levels
void secret_function() {
    printf("Exploit successful!\n");
}