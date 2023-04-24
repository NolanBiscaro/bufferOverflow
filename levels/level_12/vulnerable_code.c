// Vulnerability: A complex program with multiple buffer overflow vulnerabilities, including stack-based, heap-based, integer overflow, and format string vulnerabilities

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void level_12_vulnerable_code_1(char *input) {
    char buffer[64];
    strcpy(buffer, input);
}

void level_12_vulnerable_code_2(unsigned int size, char *input) {
    char *buffer = (char *) malloc(size);
    memcpy(buffer, input, size);
    free(buffer);
}

void level_12_vulnerable_code_3(char *input) {
    printf(input);
}

int main(int argc, char *argv[]) {
    if (argc != 4) {
        printf("Usage: %s <vuln_id> <size> <input>\n", argv[0]);
        return 1;
    }
    int vuln_id = atoi(argv[1]);
    unsigned int size = atoi(argv[2]);

    switch (vuln_id) {
        case 1:
            level_12_vulnerable_code_1(argv[3]);
            break;
        case 2:
            level_12_vulnerable_code_2(size, argv[3]);
            break;
        case 3:
            level_12_vulnerable_code_3(argv[3]);
            break;
        default:
            printf("Invalid vulnerability ID.\n");
            return 1;
    }
    return 0;
}

// Common secret function for all levels
void secret_function() {
    printf("Exploit successful!\n");
}
