#include<stdio.h>

int main(){
  int n,x;
  int i;
  int a = 0;
  int d = 0;

  scanf("%d %d",&n,&x);

  if(1>n || n>100)return 0;
  if(1>x || x>10000)return 0;

  int L[n];

  for(i=0;i<n;i++){
    scanf("%d",&L[i]);
  }

  for(i=0;i<=n;i++){
    if(i!=0)d = d + L[i-1];
    if(i==0)d=0;

    if(d>x)break;
    else a++;
  }

  printf("%d\n",a);

  return 0;
}
