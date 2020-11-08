#include<stdio.h>

int main(){
  int n, a, b;
  int ans;

  scanf("%d %d %d",&n, &a, &b);

  if(n<1 || n>20)return 0;
  if(a<1 || a>50)return 0;
  if(b<1 || b>50)return 0;

  if(a*n>b)ans = b;
  else ans = a*n;

  printf("%d\n",ans);

  return 0;
}
