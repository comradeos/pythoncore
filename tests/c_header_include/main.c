#include <stdio.h>
#include "my_lib.h"

void HelloWorld()
{
   hello_world();
}

int Sum()
{
    return sum(1, 2);
}

int main()
{
    return 0;
}

/*
clang -dynamiclib -o ext_lib ./main.c
*/