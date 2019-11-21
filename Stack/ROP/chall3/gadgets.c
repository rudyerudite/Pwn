#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char FLAG[100]="5up3r_53cr3t_$tr1ng_n0_0n3_c4n_s33!";

void pop_rdi()
{
  asm("pop %rdi;ret");
}

int main(int argc, char const *argv[]) {
  char a[10];
  alarm(10);
  puts("Welcome Cadet. Your aim for this mission is to print out the contents of the 'FLAG' global variable");
  puts("As usual here is your buffer-overflow. This program will terminate in 10 seconds.");
  gets(a);
  return 0;
}
