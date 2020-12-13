#include <stdio.h>

int main(void){
    int n, i, j;
    int a;
    int ans;
    scanf("%d", &n);
    int x[n];
    for(i = 0; i < n; i++){
        scanf("%d", &x[i]);
    }

    for(i = 0; i <= 100; i++){
        a = 0;
        for(j = 0; j < n; j++){
            a += (i - x[j]) * (i - x[j]);
        }
        if(i == 0 || ans > a){
            ans = a;
        }
    }

    printf("%d\n", ans);

    return 0;
}
