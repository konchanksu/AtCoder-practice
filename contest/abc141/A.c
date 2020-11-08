#include <stdio.h>
#include <string.h>

int main(){
    char hoge[10];
    scanf("%s", hoge);

    if(strcmp(hoge, "Sunny") == 0){
        printf("Cloudy");
    }else if(strcmp(hoge, "Cloudy") == 0){
        printf("Rainy");
    }else{
        printf("Sunny");
    }
    return 0;
}