#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <unistd.h>

const char *niceguy = NULL;
char *table[10] = {0};

int get_inp(char * buffer, int len) {
    int retval = read(0, buffer, len);
    if ( retval == -1)
        exit(0);
    buffer[retval] = '\0';
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
    unsigned long long size = 0;
    char *ptr = NULL;
    puts("Enter size of input");
    size = getll();
    if( size < 128 ){
        puts("Size is too small !");
        return 1;
    }
    ptr = malloc(size);
    if ( ptr == NULL)
        exit(0);
    puts("Enter index");
    int idx = getint();
    if ( idx < 0 || idx > 9) {
        puts("Invalid index");
        return 1;
    }
    table[idx] = ptr;
    return 0;
}



int delete() {
    int index = 0;
    puts("Enter index");
    index = getint();
    if ( index < 0 || index > 9 || table[index] == NULL) {
        puts("Invalid index");
        return 1;
    }
    free(table[index]);
    table[index] = NULL;
    return 0;
}


int edit() {
    int size, idx;
    puts( "Enter index");
    idx = getint();
    if ( idx < 0 || idx > 9 || table[idx] == NULL) {
        puts("Invalid index");
        return 1;
    }
    puts("Enter size");
    size = getint();
    get_inp(table[idx], size);
    return 0;
}


void printmenu() {
    puts( "1) Add\n2) Delete\n3) Edit\n4) Exit\n");
    printf(">> ");
}


int goodguy() {
    printf("%p\n", niceguy);
    return 0;
}


int main() {
    alarm(30);
    setvbuf(stdout, NULL, _IONBF, 0);
    niceguy = malloc(256);
    do {
        printmenu();
        switch (getint()) {
            case 1: add(); break;
            case 2: delete(); break;
            case 3: edit(); break;
            case 4: exit(0);
            case 1337: goodguy(); break;
            default: puts("Invalid choice"); break;
        }
    } while(1);
    return 0;
}
