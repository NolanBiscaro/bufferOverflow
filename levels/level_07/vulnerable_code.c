// Vulnerable code for level 7
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <stdio.h>

void level_07_vulnerable_code(char *input) {
    printf(input);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }
    level_07_vulnerable_code(argv[1]);
    return 0;
}

// Common secret function for all levels
void secret_function() {
    printf("Exploit successful!\n");
}
