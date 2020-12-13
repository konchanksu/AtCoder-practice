#include <stdio.h>

int main(void){
    int n, k;
    scanf("%d %d", &n, &k);
    int a = 1;
    int count = 0;

    while(a <= n){
        a *= k;
        count++;
    }

    printf("%d\n", count);
    return 0;
}
