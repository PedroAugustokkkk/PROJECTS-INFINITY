#include <stdio.h>

int main() {
    char nome[100];
    int idade;

    printf("Digite seu nome: ");
    fgets(nome, sizeof(nome), stdin);  // Lê uma string com espaços

    printf("Digite sua idade: ");
    scanf("%d", &idade);

    printf("\nNome: %s", nome);
    printf("Idade: %d\n", idade);

return 0;
}
