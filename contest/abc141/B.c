#include <stdio.h>
#include <string.h>

int main(){
    char hoge[101];
    int a;

    scanf("%s", hoge);
    a = strlen(hoge);

    for(int i = 0; i < a; i++){
        if(i % 2 == 0){
            if(hoge[i] == 'L'){
                printf("No\n");
                return 0;
            }
        }else{
            if(hoge[i] == 'R'){
                printf("No\n");
                return 0;
            }
        }
    }
    printf("Yes\n");
    return 0;
}