#include <stdio.h>

int main(){
  int n, d;
  int s;
  int ans;

  scanf("%d %d",&n, &d);

  for(int i=1;i<20;i++){
    s = (d * 2 + 1) * i;
    if(n <= s){
      ans = i;
      break;
    }
  }

  printf("%d\n",ans);
  return 0;
}
