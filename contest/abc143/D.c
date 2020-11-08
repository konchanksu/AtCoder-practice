#include <stdio.h>

int main(){
    int a, b;
    int num[10000];

    scanf("%d %d", &a, &b);

    if(a < b){
        int m = a;
        a = b;
        b = m;
    }

    num[0] = a;
    num[1] = b;

    for(int i = 0; i < 100000; i++){
        num[i + 2] = num[i] % num[i + 1];
        if(num[i + 2] == 0){
            printf("%d\n", num[i + 1]);
            break;
        }
    } 

    return 0;
}