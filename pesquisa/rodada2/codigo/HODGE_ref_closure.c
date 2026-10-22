/* HODGE_ref_closure.c -- search for "pair certificates" for a residual Hodge character a of X_m^4.
 * Certificate: a u p_1 u ... u p_k  (p_j = {b_j, -b_j}) = disjoint union of blocks, each block a
 * Hodge character (sum <t v> = |v|/2 * M for all units t mod M) of one of the known-algebraic types:
 *   L=2 pair; L=4 any grade-2 quadruple (Fermat surface, Lefschetz (1,1));
 *   L=6 tsplit (two zero-sum triples, X^1 x X^1), std5 (Aoki s_{5,i}), qdec sextuple (Shioda);
 *   L=8 std7 (Aoki s_{7,i}).
 * Optional level lift: work with a' = lam*a at level M = lam*m (descent along X_{lam m} -> X_m).
 * usage: HODGE_ref_closure m lam K a0 a1 a2 a3 a4 a5
 * prints the first certificate found (blocks) or NONE.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int M,U[1024],nU;
static int gcd(int a,int b){while(b){int t=a%b;a=b;b=t;}return a;}
static void sortv(int *v,int L){for(int i=1;i<L;i++){int x=v[i],j=i-1;while(j>=0&&v[j]>x){v[j+1]=v[j];j--;}v[j+1]=x;}}
static int cmpv(const int *a,const int *b,int L){for(int i=0;i<L;i++){if(a[i]!=b[i])return a[i]<b[i]?-1:1;}return 0;}
static int grade(const int *v,int L){ long s=0; for(int i=0;i<L;i++){ if(v[i]%M==0) return 0; s+=v[i]; }
  if(s%M) return 0; long y=s/M;
  for(int j=0;j<nU;j++){int t=U[j]; long st=0; for(int i=0;i<L;i++) st+=(long)t*v[i]%M; if(st!=y*M) return 0;}
  return (int)y; }
static int is_std(const int *w,int L,int p){ if(L!=p+1||M%p) return 0; int k=M/p;
  for(int i=1;i<k;i++){int v[16]; for(int j=0;j<p;j++) v[j]=i+j*k; v[p]=(M-(p*i)%M)%M; if(!v[p]) continue; sortv(v,L); if(!cmpv(v,w,L)) return 1;}
  return 0; }
static int dec6(const int *a){for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)if((a[i]+a[j])%M==0)return 1;return 0;}
static int tspl(const int *a){for(int j=1;j<6;j++)for(int k=j+1;k<6;k++) if((a[0]+a[j]+a[k])%M==0) return 1; return 0;}
static int qdec6(const int *a){for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)for(int k=j+1;k<6;k++){int s=(a[i]+a[j]+a[k])%M; if(!s) continue; int c[4]={a[i],a[j],a[k],M-s}; if(grade(c,4)==2) return 1;} return 0;}
static const char* btype(const int *v,int L){ int w[16]; memcpy(w,v,L*sizeof(int)); sortv(w,L);
  if(L==2) return (w[0]+w[1])%M==0?"pair":0;
  if(grade(w,L)!=L/2) return 0;
  if(L==4) return "quad";
  if(L==6){ if(dec6(w)) return "dec6"; if(is_std(w,6,5)) return "std5"; if(tspl(w)) return "tsplit"; if(qdec6(w)) return "qdec6"; return 0; }
  if(L==8) return is_std(w,8,7)?"std7":0;
  return 0; }
static int blk[16][16],blen[16],nb;
static int part(const int *e,int n,int used){
  int f=-1; for(int i=0;i<n;i++) if(!(used>>i&1)){f=i;break;}
  if(f<0) return 1;
  int rest[16],nr=0; for(int i=f+1;i<n;i++) if(!(used>>i&1)) rest[nr++]=i;
  for(int S=0;S<(1<<nr);S++){ int L=1+__builtin_popcount(S); if((L&1)||L>8) continue;
    int v[16],lv=0,mask=1<<f; v[lv++]=e[f];
    for(int i=0;i<nr;i++) if(S>>i&1){v[lv++]=e[rest[i]];mask|=1<<rest[i];}
    if(!btype(v,lv)) continue;
    memcpy(blk[nb],v,lv*sizeof(int)); blen[nb]=lv; nb++;
    if(part(e,n,used|mask)) return 1;
    nb--; }
  return 0; }
int main(int argc,char**argv){
  int m=atoi(argv[1]),lam=atoi(argv[2]),K=atoi(argv[3]); int a[6]; for(int i=0;i<6;i++) a[i]=atoi(argv[4+i]);
  M=lam*m; nU=0; for(int t=1;t<M;t++) if(gcd(t,M)==1) U[nU++]=t;
  int e[16]; for(int i=0;i<6;i++) e[i]=lam*a[i];
  if(grade(e,6)!=3){printf("not Hodge at level %d\n",M);return 1;}
  { const char*t=btype(e,6); if(t){printf("m=%d lam=%d level0: a itself is %s\n",m,lam,t);return 0;} }
  int b[8]={0};
  for(int k=1;k<=K;k++){
    int lim=M/2; for(int j=0;j<k;j++) b[j]=1;
    while(1){
      int n=6; for(int j=0;j<k;j++){e[n++]=b[j]; e[n++]=M-b[j];}
      nb=0;
      if(part(e,n,0)){
        printf("m=%d lam=%d (level %d) k=%d a'=(%d,%d,%d,%d,%d,%d) pairs:",m,lam,M,k,e[0],e[1],e[2],e[3],e[4],e[5]);
        for(int j=0;j<k;j++) printf(" {%d,%d}",b[j],M-b[j]);
        printf(" blocks:");
        for(int q=0;q<nb;q++){int w[16]; memcpy(w,blk[q],blen[q]*sizeof(int)); sortv(w,blen[q]); printf(" %s(",btype(w,blen[q])); for(int i=0;i<blen[q];i++) printf("%d%s",w[i],i+1<blen[q]?",":""); printf(")");}
        printf("\n"); return 0; }
      /* next nondecreasing k-tuple in [1,lim] */
      int j=k-1; while(j>=0&&b[j]==lim) j--; if(j<0) break; b[j]++; for(int q=j+1;q<k;q++) b[q]=b[j];
    }
  }
  printf("m=%d lam=%d K=%d a=(%d,%d,%d,%d,%d,%d): NONE\n",m,lam,K,a[0],a[1],a[2],a[3],a[4],a[5]);
  return 0;
}
