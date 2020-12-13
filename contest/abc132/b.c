#include<stdio.h>

int main(){
  int n;
  scanf("%d",&n);
  if(n<3 || n>20){return 0;}

  int p[n];
  int i,j;
  int a=0;
  for(i=0;i<n;i++){
    scanf("%d",&p[i]);
    if(p[i] > n || p[i] < 1){
      return 0;
    }
  }

  for(i=0;i<n;i++){
    for(j=i+1;j<n;j++){
      if(p[i] == p[j]){
        return 0;
      }
    }
  }

  for(i=1;i<n-1;i++){
    if(p[i]>p[i+1] && p[i]<p[i-1]){
      a++;
    }
    else if(p[i]<p[i+1] && p[i]>p[i-1]){
      a++;
    }
  }

  printf("%d\n",a);
  return 0;
}
