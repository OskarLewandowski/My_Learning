#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 50

void zapelnianie(int tablica[N])
{
    int i = 0;
    for(i = 0; i < N; i++)
    {
        tablica[i] = rand() % 99999;
    }
}


void wyswietl(int tablica[], int n)
{
	int i;
	for (i=0; i < n; i++)
    {
       printf("\t%d ", tablica[i]);
    }
	printf("\n");
}

void swap(int* a, int* b)
{
	int t = *a;
	*a = *b;
	*b = t;
}

void SortujSzybko(int tablica[],int first,int last)
{
   int i, j, pivot, temp;

   if(first<last){
      pivot=first;
      i=first;
      j=last;

      while(i<j){
         while(tablica[i]<=tablica[pivot]&&i<last)
            i++;
         while(tablica[j]>tablica[pivot])
            j--;
         if(i<j){
            temp=tablica[i];
            tablica[i]=tablica[j];
            tablica[j]=temp;
         }
      }

      temp=tablica[pivot];
      tablica[pivot]=tablica[j];
      tablica[j]=temp;
      SortujSzybko(tablica,first,j-1);
      SortujSzybko(tablica,j+1,last);

   }
}

int main()
{
    srand(time(NULL));
	int tablica[N];
	zapelnianie(tablica);

    //int tablica[] = {997,0,124,756,1337,34656,21,69,70,2137,112,235436,6878,23,132,4235,56768,3};
    int n = sizeof(tablica)/sizeof(tablica[0]);
    //printf("(1) %d (2) %d (Ilosc) %d \n",sizeof(tablica), sizeof(tablica[0]), sizeof(tablica)/sizeof(tablica[0]));
    printf("\n");
	printf("Przed sortowaniem:");
	wyswietl(tablica, n);
	SortujSzybko(tablica, 0, n-1);
    printf("\n");
	printf("Po sortowaniu:");
	wyswietl(tablica, n);
    printf("\n");
	return 0;
}
