#include <stdio.h>
#include <stdlib.h>

int fibonacci(int n)
{
    int a = 0;
    int b = 1;
    int suma = 0;
    int i=0;

     for( i = 0; i < n ; i++)
     {
         suma = suma + b;
         b = a + b;
         a = b - a;
     }

     return suma;
}

int main()
{
    int n;
    printf("Podaj ile elementow ciagu Fibonacciego chcesz zsumowac:");
    scanf("%d",&n);
    printf("Suma %d liczb fibonacciego wynosi = %d \n",n,fibonacci(n));

    return 0;
}
