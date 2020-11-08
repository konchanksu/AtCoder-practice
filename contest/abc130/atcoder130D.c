#include<stdio.h>

int main(){
  int n;
  int x = 0;
  long k;
  int i,j;
  int t;
  long ans = 0;

  scanf("%d %d",&n,&k);
  int a[n];
  int s[n+1];
  s[0]=0;
  for(i=0;i<n;i++){
    scanf("%d",a[i]);
    s[i+1] = s[i] + a[i];
  }

  for(i=0;i<n;i++){
    while () {
      
    }
  }

  printf("%ld\n",ans);
  return 0;
}
