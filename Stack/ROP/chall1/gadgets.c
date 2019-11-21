#include <stdlib.h>
#include <unistd.h>

void exec(char* cmd)
{
  system(cmd);
}

int main(int argc, char const *argv[]) {
  char a[10];
  alarm(10);
  puts("Welcome Cadet. Your aim for this mission is to call system() with /bin/sh");
  puts("As usual here is your buffer-overflow. This program will terminate in 10 seconds.");
  gets(a);
  return 0;
}

//