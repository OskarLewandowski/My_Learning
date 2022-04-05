#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>

bool sprawdzenie(char zdanie)
{
    if(zdanie>=48 && zdanie<=57)
    {
        return false;
    }
    return true;
}
bool sprawdzenie1(char zdanie)
{
    if((zdanie>=33 && zdanie<=47) ||(zdanie>=58 && zdanie<=64) || (zdanie>=91 && zdanie<=96)|| (zdanie>=123 && zdanie<=126))
    {
        return false;
    }
    return true;

}
bool spacja(char zdanie)
{
    if(isspace(zdanie))
    {
        return true;
    }
    return false;
}


bool duza(char zdanie)
{
    if(isupper(zdanie))
    {
        return true;
    }
    return false;
}

bool mala(char zdanie)
{
    if(islower(zdanie))
    {
        return true;
    }
    return false;
}

int main()
{
    char zdanie;
    printf("Kazda duza litera zostanie zamieniona na mala i na odwrot:\n");

  while(zdanie!='\n')
  {
      scanf("%c", &zdanie);

      if(sprawdzenie(zdanie) == false)
      {
            printf("ERROR_INVALID_DATA_13 (Wprowadzono niedozwolony znak: '%c')",zdanie);
            exit(0);
      }
      if(sprawdzenie1(zdanie) == false)
      {
            printf("ERROR_INVALID_DATA_13 (Wprowadzono niedozwolony znak: '%c')",zdanie);
            exit(0);
      }
      if(spacja(zdanie)==true)
      {
            printf("%c",zdanie);
      }
      if(duza(zdanie)==true)
      {
            printf("%c",zdanie+32);
      }
      if(mala(zdanie)==true)
      {
            printf("%c",zdanie-32);
      }
  }

    return 0;
}
