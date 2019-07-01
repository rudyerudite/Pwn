#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char name[64];
char* table[10];

int get_inp(char * buffer, int len) {
    int retval = read(0, buffer, len);
    if ( retval == -1)
        exit(0);
    char *ptr = strchr(buffer, 10);
    if (ptr != NULL)
        *ptr = '\0';
    return 0;
}

int getint() {
    char buffer[32];
    get_inp(buffer, 32);
    return atoi(buffer);
}

void add()
{
  printf("Enter index :");
  int idx=getint();
  if(idx<0 || idx>9)
    exit(0);
  table[idx]=malloc(0x30);
  get_inp(table[idx],0x30);
}

void delete()
{
  printf("Enter index :");
  int idx=getint();
  if(idx<0 || idx>9 || !table[idx])
    exit(0);
  free(table[idx]);
  table[idx]=NULL;
}

void edit()
{
  printf("Enter index :");
  int idx=getint();
  if(idx<0 || idx>9 || !table[idx])
    exit(0);
  get_inp(table[idx],0x50);
}

void view()
{
  printf("Enter index :");
  int idx=getint();
  if(idx<0 || idx>9 || !table[idx])
    exit(0);
  printf("Data: %s\n",table[idx]);
}

int printmenu()
{
    puts("-----------------------");
    puts("#### Fast-bin Menu ####");
    puts("-----------------------");
    puts("| 1. Add              |");
    puts("| 2. Edit             |");
    puts("| 3. View             |");
    puts("| 4. Free             |");
    puts("| 5. View name        |");
    puts("| 6. Exit             |");
    puts("-----------------------");
    printf("Enter choice >> ");
    return getint();
}


int main()
{
    setvbuf(stdout,NULL,_IONBF,0);
    printf("Enter name: ");
    get_inp(name,64);
    while(1){
      switch(printmenu()){
        case 1: add();
                break;
        case 2: edit();
                break;
        case 3: view();
                break;
        case 4: delete();
                break;
        case 5: printf("Name: %s\n",name);
                break;
        case 6: exit(0);
        default: puts("Nice! You don't even know how to read.");
      }
    }
}
