#include <stdio.h>

int main(){
  int i,j;
  int a=-1,b=-1;
  int c=0;
  char s[5];

  for(i=0;i<4;i++){
    scanf("%c",&s[i]);
  }
  s[4] = '\n';

  for(i=0;i<4;i++){
    for(j=0;j<4;j++){
      if(i!=j && s[i] == s[j]){

        c++;
      }
    }
  }
  if(c==4){printf("Yes\n");}
  else{printf("No\n");}
  return 0;
}
