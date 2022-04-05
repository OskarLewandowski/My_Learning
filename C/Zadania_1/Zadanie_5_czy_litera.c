#include <stdio.h>
#include <stdlib.h>

int main()
{
    char znak;
    while(znak != '/')
    {
        printf("Podaj znak w celu sprawdzenia (aby zakonczyc wcisnij '/'): ");
        scanf(" %s", &znak);
        if(znak>=49 && znak<=57)
        {
            printf("Wprowadzono liczbe: ' %c '\n", znak);
        }
        else if((znak>=33 && znak<=47) ||(znak>=58 && znak<=64) || (znak>=91 && znak<=96)|| (znak>=123 && znak<=126))
        {
            printf("Wprowadzono znak: ' %c '\n", znak);
        }
        else
        {
            printf("Wprowadzono litere: ' %c '\n", znak);
        }
    }

    return 0;
}
