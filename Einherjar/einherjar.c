+#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

char *author = NULL;
char **table = NULL;
int *sizes = NULL;

//need to figure out a leak to pass into 1337
int get_inp(char * buffer, int len) { //nulling out the 10th character?
    int retval = read(0, buffer, len);
    if ( retval == -1)
        exit(0);
    char *ptr = strchr(buffer, 10); //check this part specifically
    if (ptr != NULL)
        *ptr = '\0';
    return 0;
}
    

int getint() {
    char buffer[32];
    get_inp(buffer, 32);
    return atoi(buffer);
}


long long getll() {
    char buffer[32];
    get_inp(buffer, 32);
    return atoll(buffer);
}


int add() {
    int size = 0, idx = 0;
    char *ptr = NULL;
    puts("Enter size of input");
    size = getint();
    ptr = malloc(size);
    if ( ptr == NULL)
        exit(0);
    puts("Enter index");
    idx = getint();
    if ( idx < 0 || idx > 9) {
        puts("Invalid index");
        return 1;
    }
    table[idx] = ptr;
    sizes[idx] = size;
    return 0;
}


int delete() {
    int index = 0;
    puts("Enter index");
    index = getint();
    if ( index < 0 || index > 9 || table[index] == NULL) { //fail the OR condition...but asm code dusn seem so
        puts("Invalid index");
        return 1;
    }
    free(table[index]);
    table[index] = NULL;
    return 0;
}


int edit() {
    int size, idx, len;
    puts( "Enter index");
    idx = getint();
    if ( idx < 0 || idx > 9 || table[idx] == NULL) { //fail the OR condition 
        puts("Invalid index");
        return 1;
    }
    get_inp(table[idx], sizes[idx]); //pass it for taking regular input; overwrite the prev size?
    return 0;
}


int view() {
    int i = 0;
    for (i = 0; i < 10; i++) {
        if ( table[i] == NULL )
            continue;
        printf("%d => %s\n", i, table[i]);
    }
    return 0;
}


void flip() { //flip the prev_in_use bit at the leaked address
    long long addr = 0;
    int value;
    printf("Address : ");
    addr = getll();
    value = *(char *)addr; //changing the value at that  addr
    value ^= 1;
    *(char *)addr = value;
}


void change_author() {
    get_inp(author, 64);
}


void printmenu() {
    puts( "1) Add\n2) Delete\n3) Edit\n4) View\n5) Change author\n6) Exit");
    printf(">> ");
}


int main() {
    alarm(30);
    setvbuf(stdout, NULL, _IONBF, 0);//setting the buffer as null
    author = malloc(100); 
    table = (char **)malloc(10*sizeof(char *));
    sizes = (int *)malloc(10*sizeof(int));
    do { 
        printmenu();
        switch (getint()) {
            case 1: add(); break;
            case 2: delete(); break;
            case 3: edit(); break;
            case 4: view(); break;
            case 5: change_author(); break;
            case 6: exit(0);
            case 1337: flip(); break;
            default: puts("Invalid choice"); break;
        }
    } while(1);
    return 0;
}
