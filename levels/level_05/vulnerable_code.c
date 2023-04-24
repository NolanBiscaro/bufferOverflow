// Vulnerable code for level 5
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
    void (*func_ptr)();
    char buffer[64];
} data;

void level_05_vulnerable_code(char *input) {
    data *d = (data *) malloc(sizeof(data));
    d->func_ptr = NULL;
    strcpy(d->buffer, input);
    if (d->func_ptr) {
        d->func_ptr();
    }
    free(d);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }
    level_05_vulnerable_code(argv[1]);
    return 0;
}

// Common secret function for all levels
void secret_function() {
    printf("Exploit successful!\n");
}