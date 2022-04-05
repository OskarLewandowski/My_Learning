#include <stdio.h>
#include <stdlib.h>

void MinMax(int arr[],int licz)
{
    int n, min, max, trzym1, trzym2;
    //system("cls");
    min=arr[0];
    max=arr[0];

    for(int i=1;i<licz;i++)
    {
        trzym1=arr[i];
        trzym2=arr[i];
        if(min>trzym1)
        {
            min = trzym1;
        }
        else if(max<trzym2)
        {
            max=trzym2;
        }
    }

    printf("\nNajmniejsza liczba jest: %d\n",min);
    printf("\nNajwieksza liczba jest: %d\n",max);
}

void swap(int* a, int* b)
{
	int t = *a;
	*a = *b;
	*b = t;
}

void SortujSzybko(int arr[],int first,int last){
   int i, j, pivot, temp;

   if(first<last){
      pivot=first;
      i=first;
      j=last;

      while(i<j){
         while(arr[i]<=arr[pivot]&&i<last)
            i++;
         while(arr[j]>arr[pivot])
            j--;
         if(i<j){
            temp=arr[i];
            arr[i]=arr[j];
            arr[j]=temp;
         }
      }

      temp=arr[pivot];
      arr[pivot]=arr[j];
      arr[j]=temp;
      SortujSzybko(arr,first,j-1);
      SortujSzybko(arr,j+1,last);
   }
}

int main()
{
    size_t size = 16;
    int tmp, *tab;
    int licz=0;
    int n;
// Przydzielenie poczatkowego bloku pamieci
    tab = malloc(sizeof *tab * (size + 1));
    if (!tab)
    {
        perror("malloc");
        return 0;
    }
// odwolanie do elementu poza tablicy
    tab[size + 1] = 0;

    puts("Podaj liczby calkowite dodatnie: ");
    printf("%d) ",licz+1);
// Odczyt liczb
    while (scanf("%d", &tmp) == 1)
    {
// Jezeli zapelniono cala tablice, trzeba ja zwiekszyc
// bledny warunek - prawdziwy tylko gdy size jest rowne 0
        if (tab == tab + size)
        {
            size *= 4;

            int *ptr = realloc(tab, (size + 1) * sizeof *ptr);
            if (!ptr)
            {
                free(tab);
                perror("realloc");
                return 0;
            }
// znowu odwolanie sie do elementu poza tablicy
            ptr[size + 1] = 0;
            tab = ptr;
        }
        *tab = tmp;
        ++tab;
        licz++;
        printf("%d) ",licz+1);
    }

// printf("ILE %d",licz);
    n=licz;
    int x;
    int trzym[licz];
    int trzymOdwrotnie[licz];
    x=licz-1;

    for(int j=0; j<licz; j++)
    {
        --tab;
        trzym[j]=*tab;
        trzymOdwrotnie[x]=trzym[j];
        x=x-1;
    }

//MIN I MAX
    MinMax(trzym,licz);
    printf("\n");

//SORTOWANIE PRZED
    printf("Przed sortowaniem: ");
    for(int i = 0; i < licz; i++)
    {
        printf(" %d ",trzymOdwrotnie[i]);
    }

    SortujSzybko(trzym, 0, n-1);
    printf("\n\n");

    printf("Po sortowaniu: ");
    for(int i = 0; i < licz; i++)
    {
        printf(" %d ",trzym[i]);
    }
    printf("\n");

// Zwolnienie pamieci i zakonczenie programu
    free(tab);
    return 0;
}
