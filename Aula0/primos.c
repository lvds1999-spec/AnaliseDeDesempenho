#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
int is_prime(int x) {
    if (x <= 1) return 0;
    if (x == 2 || x == 3 || x == 5) return 1;
    if (x % 2 == 0 || x % 3 == 0 || x % 5 == 0) return 0;
    int sqrt_n = (int)floor(sqrt((double)x));
    for (int d = 7; d <= sqrt_n; d += 2) {
        if (x % d == 0) return 0;
    }
    return 1;
}
int main(void) {
    char line[256];
    long n;
    char *endptr;
    printf("Digite um inteiro N > 0: ");
    if (fgets(line, sizeof(line), stdin) == NULL) {
        fprintf(stderr, "Erro de leitura.\n");
        return 1;
    }
    line[strcspn(line, "\r\n")] = '\0';
    if (line[0] == '\0') {
        fprintf(stderr, "Entrada vazia. Informe um número inteiro > 0.\n");
        return 1;
    }
    n = strtol(line, &endptr, 10);
    while (*endptr != '\0' && isspace((unsigned char)*endptr)) {
        endptr++;
    }
    if (*endptr != '\0') {
        fprintf(stderr, "Entrada inválida: '%s'. Informe um número inteiro > 0.\n", line);
        return 1;
    }
    if (n < 1) {
        fprintf(stderr, "Valor inválido: %ld. Informe N maior que 0.\n", n);
        return 1;
    }
    if (n > 100000000) {
        fprintf(stderr, "N muito grande para este programa (max 100000000).\n");
        return 1;
    }
    int N = (int)n;
    printf("Valor de N: %d\n", N);
    int count = 0;
    int first = 1;
    printf("Numeros primos: ");
    for (int i = 2; i <= N; i++) {
        if (is_prime(i)) {
            if (!first) {
                printf("-");
            }
            printf("%d", i);
            first = 0;
            count++;
        }
    }
    if (count == 0) {
        printf("(nenhum)");
    }
    printf("\n");
    printf("Quantidade de numeros primos: %d\n", count);
    return 0;
}