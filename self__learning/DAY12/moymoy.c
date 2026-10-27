#include <stdio.h>

int main() {
    float num1;
    float num2;
    float total;
    char choice;

    printf("Please enter the first number: ");
    scanf("%f", &num1);

    printf("Please choose your operator (+ - * /): ");
    scanf(" %c", &choice);

    printf("Please enter the second number: ");
    scanf("%f", &num2);

    if (choice == '+') {
        total = num1 + num2;
        printf("Result: %f + %f = %.3f", num1,num2, total);
    } else if (choice == '-') {
        total = num1 - num2;
        printf("Result: %f - %f = %.3f", num1,num2, total);
    } else if (choice == '*') {
        total = num1 * num2;
        printf("Result: %f x %f = %.3f", num1,num2, total);
    } else if (choice == '/') {
        if (num2 == 0) {
            printf("Error BRUH: cannot divide by zero.");
        } else {
            total = num1 / num2;
            printf("Result: %f % %f = %.3f", num1,num2, total);
        }
    } else {
        printf("Your choice is invalid, please run the program again.\n");
    }

    return 0;
}