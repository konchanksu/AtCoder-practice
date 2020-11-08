#include <stdio.h>

int main(void){
    int a[3][3];
    int i, j, n;
    int flag = 0;
    int sum = 0, sum2 = 0;
    for(i = 0; i < 3; i++){
        for(j = 0; j < 3; j++){
            scanf("%d", &a[i][j]);
        }
    }

    scanf("%d", &n);
    int b[n];
    for(i = 0; i < n; i++){
        scanf("%d", &b[i]);
        for (j = 0; j < 3; j++){
            for(int k = 0; k < 3; k++){
                if(a[j][k] == b[i]){
                    a[j][k] = 0;
                }
            }
        }
    }

    for(i = 0; i < 3; i++){
        sum = 0, sum2 = 0;
        for(j = 0; j < 3; j++){
            sum += a[i][j];
            sum2 += a[j][i];
        }
        if(sum == 0 || sum2 == 0){
            flag = 1;
        }
    }

    if(a[0][0] + a[1][1] + a[2][2] == 0 || a[2][0] + a[1][1] + a[0][2] == 0) flag = 1;

    if(flag == 1){
        printf("Yes\n");
    }else{
        printf("No\n");
    }
    

    return 0;
}
