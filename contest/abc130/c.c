#include<stdio.h>

int main(){
  int x,y;
  double w,h;
  int m;
  double ans;
  scanf("%lf %lf %d %d",&w,&h,&x,&y);
  if(w<1 || h>1000000000)return 0;
  if(0>x || x>w)return 0;
  if(0>y || y>h)return 0;

  if(w/2==x && h/2==y)m = 1;
  else m=0;

  ans = w*h/2;
  printf("%lf %d\n",ans ,m);

  return 0;
}
