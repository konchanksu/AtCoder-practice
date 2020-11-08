#include <stdio.h>

int main(){
    int n;
    int a[1000000];
    int b[1000000];
    int i, j;

    scanf("%d", &n);

    for(i = 0; i < n; i++){
        scanf("%d", &a[i]);
        b[i] = i + 1;
    }

    for(i = 0; i < n; i++){
        for(j = 0; j < n; j++){
            if(a[j] ==  i + 1){
                printf("%d ", b[j]);
                break;
            }
        }
    }
    printf("\n");

    return 0;
}