#include <stdio.h>
#include <stdlib.h>

int zwieksz(int a)
{
    a = a + 10;
    return a;
}

int main()
{
    int a;
    printf("Podaj liczbe:");
    scanf("%d",&a);
    printf("\nWprowadziles: %d\nWynik po zwiekszeniu o 10 to: %d",a,zwieksz(a));
    return 0;
}
