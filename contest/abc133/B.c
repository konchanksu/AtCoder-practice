#include <stdio.h>

int main(){
  int n, d;
  int i,j,k;

  int num=0, ans =0;

  scanf("%d %d",&n, &d);
  int A[n][d];
  for(i=0;i<n;i++){
    for(j=0;j<d;j++){
      scanf("%d",&A[i][j]);
    }
  }
  int S[100] = {};

  for(i=0;i<n;i++){
    for(j=i+1;j<n;j++){
      for(k=0;k<d;k++){
        S[num] += (A[i][k] - A[j][k])*(A[i][k] - A[j][k]);
      }
      num++;
    }
  }

  for(j=0;j<num;j++){
    for(i=0;i<150;i++){
      if(i*i==S[j]){
        ans++;
        break;
      }
      if(i*i>S[j]){break;}
    }
  }

  printf("%d\n",ans);


  return 0;
}
