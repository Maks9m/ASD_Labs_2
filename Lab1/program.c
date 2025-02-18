#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct{
    double F;
    double S;
} Result;

double r1(double x, int n, int i, double F, double S);
double r3(double x, int n, int i, double F);
Result r2(double x, int n, int i);
double loop(double x, int n, double S);

int main()
{
    double x = 5;
    int n = 20;
    int i = 1;
    double F = x;
    double S = x;

    printf("\n%*s\n", 25, "---First method---");
    r1(x, n, i, F, S);
    printf("\n%*s\n", 25, "---Second method---");
    r2(x, n, n);
    printf("\n%*s\n", 25, "---Third method---");
    r3(x, n, i, F);
    printf("\n%*s\n", 25, "---Loop method---");
    loop(x, n, S);
}

double r1(double x, int n, int i, double F, double S) // Виконує обчислення n членів ряду, і суми на рекурсивному спуску
{
    if (fabs(x) < 1000000)
    {
        printf("i = %d, F = %lf, S = %lf\n", i, F, S);
        if (n == 1)
        {
            return S;
        }
        else
        {
            F *= ((x*x) / (4*i*i + 2*i));
            S += F;
            return r1(x, n - 1, i + 1, F, S);
        }
    }
    else
    {
        printf("Error: x is out of range\n");
        return 0;
    }
}

Result r2(double x, int n, int i) // Виконує обчислення n членів ряду, і суми на рекурсивному поверненні
{
    if (fabs(x) < 1000000)
    {
        Result res;
        if (i == 1)
        {
            res.F = x;
            res.S = x;
            printf("i = %d, F = %lf, S = %lf\n", i, res.F, res.S);
            return res;
        }
        
        Result prev = r2(x, n, i - 1);
        res.F = prev.F * (x*x) / (4*(i-1)*(i-1) + 2*(i-1));
        res.S = prev.S + res.F;
        printf("i = %d, F = %lf, S = %lf\n", i, res.F, res.S);
        return res;
    }
    else
    {
        printf("Error: x is out of range\n");
        return (Result){0, 0};
    }
}

double r3(double x, int n, int i, double F) // Виконує обчислення членів ряду на рекурсивному спуску, а обчислення суми на рекурсивному поверненні
{
    if (fabs(x) < 1000000)
    {
        double S;
        if (i == n)
        {
            S = F;
            printf("i = %d, F = %lf, S = %lf\n", i, F, S);
            return S;
        }
        
        S = r3(x, n, i + 1, F*(x*x) / (4*i*i + 2*i));
        S += F;
        printf("i = %d, F = %lf, S = %lf\n", i, F, S);
        return S;
    }
    else
    {
        printf("Error: x is out of range\n");
        return 0;
    }
}

double loop (double x, int n, double S) // Виконує обчислення n членів ряду, і суми на циклі
{
    if (fabs(x) < 1000000)
    {
        double F = x;
        for (int i = 1; i <= n; i++)
        {
            printf("i = %d, F = %lf, S = %lf\n", i, F, S);
            F *= ((x*x) / (4*i*i + 2*i));
            S += F;
        }
        return S;
    }
    else
    {
        printf("Error: x is out of range\n");
        return 0;
    }
}
