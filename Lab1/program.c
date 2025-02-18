#include <stdio.h>;

int r1(int x, int n, int F);
int r2(int x, int n);
int r3(int x, int n);

#define RECURSION_SIZE 3

int main()
{
    int x, n;
    int (*recursion[3])(int,int) = {r1, r2, r3};

    printf("Enter x: ");
    scanf("%d", &x);
    printf("Enter n: ");
    scanf("%d", &n);
    for (int i = 0; i < RECURSION_SIZE; i++)
    {
        printf("Result: %d", recursion[i](x, n));
    }
}

int r1(int x, int n, int F)
{
    if (n == 0)
    {
        F = x;
    }
    else
    {
        F = (x*x)*r1(x, n-1, F)/(4*n*n+2*n);
    }
    return F;
}

int r2(int x, int n)
{
}

int r3(int x, int n)
{
}
