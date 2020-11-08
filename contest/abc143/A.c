#include <stdio.h>

int main(){
    int n;
    double ans;
    double num;

    scanf("%d", &n);

    if(n % 2 == 0){
        num = n / 2;
    }else{
        num = n / 2 + 1;
    }

    ans = num / n;

    printf("%lf", ans);
    return 0;
}