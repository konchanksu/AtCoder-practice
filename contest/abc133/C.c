#include<stdio.h>

int main(){
  int l, r;
  int min = 2018, tmp, tmp1;
  int i, j;

  scanf("%d %d",&l ,&r);

  for(i=l;i<r;i++){
    for(j=i+1;j<=r;j++){
      tmp = ((i%2019)*(j%2019))%2019;
      if(tmp < min){
        min = tmp;
        if(min == 0){
          printf("%d\n",min);
          return 0;
        }
      }
    }
  }

  printf("%d\n",min);
  return 0;
}
