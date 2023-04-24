#include <stdio.h>
#include <string.h>

void level_02_vulnerable_code(char *input) {
    char buffer1[64];
    char buffer2[64];
    strcpy(buffer1, input);
    strcpy(buffer2, "This is an additional variable on the stack.");
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }
    level_02_vulnerable_code(argv[1]);
    return 0;
}

// Common secret function for all levels
void secret_function() {
    printf("Exploit successful!\n");
}