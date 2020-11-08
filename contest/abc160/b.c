#include <stdio.h>

int main(){
    int n, c500, c5;
    scanf("%d", &n);
    c500 = n / 500 * 1000;
    n %= 500;
    c5 = n / 5 * 5;
    printf("%d\n", c500 + c5);
    
    return 0;
}
