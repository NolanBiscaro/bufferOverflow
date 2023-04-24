#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void secret_function() {
    printf("Congratulations! You have successfully exploited the buffer overflow vulnerability and executed the secret function!\n");
    exit(0);
}

void vulnerable_function() {
    char buffer[64];
    printf("Enter your input: ");
    gets(buffer);
    printf("You entered: %s\n", buffer);
}

int main() {
    printf("Welcome to Level 1: Basic stack-based buffer overflow\n");
    vulnerable_function();
    printf("Exiting the program...\n");
    return 0;
}