#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void pop_rdi()
{
  asm("pop %rdi;ret");
}

void pop_rdx()
{
  asm("pop %rdx;ret");
}

void pop_rsi()
{
  asm("pop %rsi;ret");
}

void pop_rax()
{
  asm("pop %rax;ret");
}

void sys_call()
{
  asm("syscall");
}

int main(int argc, char const *argv[]) {
  char a[10];
  alarm(10);
  puts("Welcome Cadet. Your aim for this mission is to call execve syscall with second and third arguments as NULL and the first as a pointer to /bin/sh");
  puts("As usual here is your buffer-overflow. This program will terminate in 10 seconds.");
  gets(a);
  return 0;
}
