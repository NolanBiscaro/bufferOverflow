// Vulnerable code for level 11
#include <stdio.h>
#include <string.h>
#include <pthread.h>

void *level_11_vulnerable_code(void *input) {
    char buffer[64];
    strcpy(buffer, (char *)input);
    return NULL;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }
    pthread_t thread_id;
    pthread_create(&thread_id, NULL, level_11_vulnerable_code, argv[1]);
    pthread_join(thread_id, NULL);
    return 0;
}

// Common secret function for all levels
void secret_function() {
    printf("Exploit successful!\n");
}
