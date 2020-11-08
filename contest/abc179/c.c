#include <stdio.h>

int main(void){
    int n;
    scanf("%d", &n);
    int ans = n * 2 - 3;

    for(int j = 2; j * j <= n; j++) {
        for(int i = j * j; i < n; i += j) {
            if(i == j * j) ans += 1;
            else if(i % j == 0) ans += 2;
        }
    }

    printf("%d\n", ans);
}