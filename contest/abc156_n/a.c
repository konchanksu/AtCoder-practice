#include <stdio.h>

int main(void){
    int n, r;
    scanf("%d %d", &n, &r);

    if(n >= 10){
        printf("%d\n", r);
    }else{
        printf("%d\n", r + (10 - n) * 100);
    }
    
    return 0;
}
