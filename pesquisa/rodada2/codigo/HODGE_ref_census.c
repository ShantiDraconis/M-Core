/* HODGE_ref_census.c -- independent referee implementation of Shioda's (P_m^4).
 *
 * Definitions (Shioda 1979, as restated in da Silva arXiv 2101.04739 Def. 2.4/2.5):
 *   M_m = semigroup of multisets x of elements of {1..m-1} (counts x_i) with
 *         sum_i <t i> x_i = m*y for ALL t in (Z/m)^*, some integer y>0.  M_m(y) = degree y.
 *   (Elements of M_m(y) have exactly 2y entries: add the t and -t equations.)
 *   decomposable: a = c + d with c,d in M_m (both nonzero).
 *   quasi-decomposable: a + b = c + d with b in M_m(1), c,d in M_m, {c,d} != {a,b}.
 *   (P_m^4): every indecomposable a in M_m(3) is quasi-decomposable.
 * Everything below is checked LITERALLY (subset enumeration), and the 3+3 shortcut is
 * computed separately as a cross-check.
 *
 * Extra annotations for residual orbits (not part of (P_m^4)):
 *   std5 : a = s_{5,i} = {i, i+k, i+2k, i+3k, i+4k, -5i}, k=m/5 (Aoki 5-standard)
 *   tsplit: a = T1 u T2 with two zero-sum triples (Jumagulov crit. 1, X^1 x X^1)
 *   clos1/clos2: a u p1 (u p2) partitions into "known-algebraic blocks":
 *        pairs, Hodge quadruples (grade 2, Lefschetz), std5 sextuples, tsplit sextuples,
 *        std7 octuples s_{7,i}; at least one block not one of the added pairs.
 *
 * usage: HODGE_ref_census mlo mhi [verbose]
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int m, U[512], nU, Uh[512], nUh;
static int gcd(int a,int b){while(b){int t=a%b;a=b;b=t;}return a;}

/* is multiset v[0..L-1] (entries in 1..m-1) an element of M_m ? returns degree y or 0 */
static int inM(const int *v,int L){
  long s=0; for(int i=0;i<L;i++) s+=v[i];
  if(s%m) return 0;
  int y=(int)(s/m); if(y<=0) return 0;
  for(int j=0;j<nU;j++){int t=U[j]; long st=0; for(int i=0;i<L;i++) st+=(long)(t*v[i])%m; if(st!=(long)y*m) return 0;}
  return y;
}
static void sortv(int *v,int L){for(int i=1;i<L;i++){int x=v[i],j=i-1;while(j>=0&&v[j]>x){v[j+1]=v[j];j--;}v[j+1]=x;}}
static int cmpv(const int *a,const int *b,int L){for(int i=0;i<L;i++){if(a[i]!=b[i])return a[i]<b[i]?-1:1;}return 0;}

/* literal decomposability of a (length 6): a=c+d, c,d in M nonzero */
static int dec_literal(const int *a){
  for(int S=1;S<63;S++){int c[6],d[6],lc=0,ld=0;
    for(int i=0;i<6;i++){if(S>>i&1)c[lc++]=a[i];else d[ld++]=a[i];}
    if(inM(c,lc)&&inM(d,ld)) return 1;}
  return 0;
}
static int dec_fast(const int *a){for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)if((a[i]+a[j])%m==0)return 1;return 0;}

/* literal quasi-decomposability: exists beta, a+{beta,-beta} = c+d, c,d in M, {c,d}!={a,b} */
static int qdec_literal(const int *a,int *wb,int *wc,int *lwc){
  int as[6]; memcpy(as,a,sizeof as); sortv(as,6);
  for(int beta=1;beta<m;beta++){
    int e[8]; for(int i=0;i<6;i++)e[i]=a[i]; e[6]=beta; e[7]=m-beta;
    int bs[2]={beta<m-beta?beta:m-beta, beta<m-beta?m-beta:beta};
    for(int S=1;S<255;S++){ if(!(S&1)) continue; /* fix element 0 in c to halve work */
      int c[8],d[8],lc=0,ld=0;
      for(int i=0;i<8;i++){if(S>>i&1)c[lc++]=e[i];else d[ld++]=e[i];}
      if(!inM(c,lc)||!inM(d,ld)) continue;
      /* exclude trivial {c,d}={a,b} */
      int cs[8],ds[8]; memcpy(cs,c,lc*sizeof(int)); memcpy(ds,d,ld*sizeof(int)); sortv(cs,lc); sortv(ds,ld);
      int triv=0;
      if(lc==6&&ld==2&&!cmpv(cs,as,6)&&!cmpv(ds,bs,2)) triv=1;
      if(lc==2&&ld==6&&!cmpv(ds,as,6)&&!cmpv(cs,bs,2)) triv=1;
      if(triv) continue;
      if(wb){*wb=beta; memcpy(wc,cs,lc*sizeof(int)); *lwc=lc;}
      return 1;
    }
  }
  return 0;
}
/* 3+3 shortcut: triple T with s=sum T !=0 mod m and T u {-s} of degree 2 */
static int qdec_fast(const int *a){
  for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)for(int k=j+1;k<6;k++){
    int s=(a[i]+a[j]+a[k])%m; if(!s) continue;
    int c[4]={a[i],a[j],a[k],m-s}; if(inM(c,4)==2) return 1;}
  return 0;
}
static int is_std(const int *a,int L,int p){ /* a (sorted, length L=p+1) equals s_{p,i}? */
  if(L!=p+1||m%p) return 0; int k=m/p;
  for(int i=1;i<k;i++){ /* i mod k suffices up to the set {i+jk}; but -p*i depends on i mod k only too */
    int v[16]; for(int j=0;j<p;j++) v[j]=i+j*k; v[p]=((m-(p*i)%m)%m); if(v[p]==0) continue;
    sortv(v,L); if(!cmpv(v,a,L)) return i; }
  return 0;
}
static int tsplit(const int *a){
  for(int j=1;j<6;j++)for(int k=j+1;k<6;k++) if((a[0]+a[j]+a[k])%m==0) return 1; /* complement then also zero-sum */
  return 0;
}
/* is block v (length L, unsorted) a known-algebraic Hodge block? */
static int good_block(const int *v,int L){
  int w[16]; memcpy(w,v,L*sizeof(int)); sortv(w,L);
  if(L==2) return (w[0]+w[1])%m==0;
  if(inM(w,L)!=L/2) return 0;
  if(L==4) return 1;
  if(L==6) return dec_fast(w)||is_std(w,6,5)||tsplit(w);
  if(L==8) return is_std(w,8,7)>0;
  return 0;
}
/* partition multiset e[0..n-1] into good blocks; used mask */
static int part(const int *e,int n,int used,int *nontriv,int npair_added){
  int f=-1; for(int i=0;i<n;i++) if(!(used>>i&1)){f=i;break;}
  if(f<0) return 1;
  int rest[16],nr=0; for(int i=f+1;i<n;i++) if(!(used>>i&1)) rest[nr++]=i;
  for(int S=0;S<(1<<nr);S++){
    int L=1+__builtin_popcount(S); if(L&1) continue; if(L>8) continue;
    int v[16],lv=0,mask=1<<f; v[lv++]=e[f];
    for(int i=0;i<nr;i++) if(S>>i&1){v[lv++]=e[rest[i]];mask|=1<<rest[i];}
    if(!good_block(v,lv)) continue;
    /* block entirely inside the added pairs region and of length 2 counts as trivial */
    if(part(e,n,used|mask,nontriv,npair_added)) return 1;
  }
  return 0;
}
static int closure(const int *a,int k,int *wit){
  int e[10]; for(int i=0;i<6;i++) e[i]=a[i];
  if(k==1){ for(int b=1;b<=m/2;b++){ e[6]=b;e[7]=m-b; int nt; if(part(e,8,0,&nt,1)){wit[0]=b;return 1;} } }
  if(k==2){ for(int b=1;b<=m/2;b++)for(int c=b;c<=m/2;c++){ e[6]=b;e[7]=m-b;e[8]=c;e[9]=m-c; int nt;
      if(part(e,10,0,&nt,2)){wit[0]=b;wit[1]=c;return 1;} } }
  return 0;
}
/* note: a itself is indecomposable, so any partition of a u pairs into good blocks that just
   returns the added pairs and a as one block requires a itself to be good (std5/tsplit) --
   those are reported separately (level 0). For k>=1 the trivial partition {a}+pairs is only
   possible if a is good, which we test first, so closure(k) is meaningful only for non-good a. */

int main(int argc,char**argv){
  int mlo=atoi(argv[1]),mhi=atoi(argv[2]),verbose=argc>3?atoi(argv[3]):0;
  for(m=mlo;m<=mhi;m++){
    nU=nUh=0; for(int t=1;t<m;t++) if(gcd(t,m)==1){U[nU++]=t; if(t>1&&2*t<=m) Uh[nUh++]=t;}
    long nmult=0,dimB=0,norb=0,ndec=0,nqd=0,nres=0,dimres=0,mismatch=0,nstd=0,ntsp=0,nc1=0,nc2=0,nopen=0,nfull=0;
    static int reps[200000][6]; int nreps=0;
    int a[6];
    for(a[0]=1;a[0]<m;a[0]++){ int s0=3*m-a[0]; if(s0<5*a[0]) break;
     for(a[1]=a[0];a[1]<m;a[1]++){ int s1=s0-a[1]; if(s1<4*a[1]) break; if(s1>4*(m-1)) continue;
      for(a[2]=a[1];a[2]<m;a[2]++){ int s2=s1-a[2]; if(s2<3*a[2]) break; if(s2>3*(m-1)) continue;
       for(a[3]=a[2];a[3]<m;a[3]++){ int s3=s2-a[3]; if(s3<2*a[3]) break; if(s3>2*(m-1)) continue;
        for(a[4]=a[3];a[4]<m;a[4]++){ int s4=s3-a[4]; if(s4<a[4]) break; if(s4>m-1) continue;
          a[5]=s4; nmult++;
          int ok=1; for(int j=0;j<nUh&&ok;j++){int t=Uh[j],st=0; for(int i=0;i<6;i++) st+=(t*a[i])%m; if(st!=3*m) ok=0;}
          if(!ok) continue;
          /* ordered count */
          long perm=720; {int i=0; while(i<6){int j=i; while(j<6&&a[j]==a[i]) j++; int r=j-i; long f=1; for(int q=2;q<=r;q++) f*=q; perm/=f; i=j;}}
          dimB+=perm;
          /* canonical? */
          int canon=1; for(int j=1;j<nU&&canon;j++){int b[6]; for(int i=0;i<6;i++) b[i]=(U[j]*a[i])%m; sortv(b,6); if(cmpv(b,a,6)<0) canon=0;}
          if(!canon) continue;
          norb++; memcpy(reps[nreps++],a,sizeof a);
        }}}}}
    for(int r=0;r<nreps;r++){ int *x=reps[r];
      { /* full pairing (MMRV Def 3.6, linear-cycle characters D_m^4) */
        int fp=0; int pr[15][3][2]={{{0,1},{2,3},{4,5}},{{0,1},{2,4},{3,5}},{{0,1},{2,5},{3,4}},{{0,2},{1,3},{4,5}},{{0,2},{1,4},{3,5}},{{0,2},{1,5},{3,4}},{{0,3},{1,2},{4,5}},{{0,3},{1,4},{2,5}},{{0,3},{1,5},{2,4}},{{0,4},{1,2},{3,5}},{{0,4},{1,3},{2,5}},{{0,4},{1,5},{2,3}},{{0,5},{1,2},{3,4}},{{0,5},{1,3},{2,4}},{{0,5},{1,4},{2,3}}};
        for(int q=0;q<15&&!fp;q++){int ok=1; for(int u=0;u<3;u++) if((x[pr[q][u][0]]+x[pr[q][u][1]])%m) ok=0; if(ok) fp=1;}
        nfull+=fp; }
      int dl=dec_literal(x), df=dec_fast(x); if(dl!=df) mismatch++;
      if(dl){ndec++; continue;}
      int wb,wc[8],lwc; int ql=qdec_literal(x,&wb,wc,&lwc), qf=qdec_fast(x); if(ql!=qf) mismatch++;
      if(ql){nqd++; continue;}
      nres++;
      /* orbit dimension */
      { int seen[256][6],ns=0; long d=0; for(int j=0;j<nU;j++){int b[6]; for(int i=0;i<6;i++) b[i]=(U[j]*x[i])%m; sortv(b,6);
          int nw=1; for(int q=0;q<ns;q++) if(!cmpv(seen[q],b,6)){nw=0;break;}
          if(nw){ if(ns<256) memcpy(seen[ns++],b,sizeof b); long perm=720; int i=0; while(i<6){int jj=i; while(jj<6&&b[jj]==b[i]) jj++; int rr=jj-i; long f=1; for(int q=2;q<=rr;q++) f*=q; perm/=f; i=jj;} d+=perm; } }
        dimres+=d; }
      int st=is_std(x,6,5), ts=tsplit(x), c1=0,c2=0,w[2]={0,0};
      if(st) nstd++; else if(ts) ntsp++; else { c1=closure(x,1,w); if(c1) nc1++; else { c2=closure(x,2,w); if(c2) nc2++; else nopen++; } }
      if(verbose) printf("  m=%d R: (%d,%d,%d,%d,%d,%d) %s%s%s%s%s",m,x[0],x[1],x[2],x[3],x[4],x[5],
          st?"std5 ":"",ts?"tsplit ":"",c1?"clos1 ":"",c2?"clos2 ":"",(!st&&!ts&&!c1&&!c2)?"OPEN ":"");
      if(verbose&&(c1||c2)) printf(" pairs={%d,%d}%s",w[0],m-w[0],c2?"":""), c2?printf(",{%d,%d}",w[1],m-w[1]):0;
      if(verbose) printf("\n");
    }
    printf("m=%d phi=%d multisets(sum3m)=%ld dimB=%ld orbits=%ld dec=%ld qdec=%ld R=%ld dimR=%ld | std5=%ld tsplit=%ld clos1=%ld clos2=%ld open=%ld | fullpair=%ld mismatch=%ld\n",
      m,nU,nmult,dimB,norb,ndec,nqd,nres,dimres,nstd,ntsp,nc1,nc2,nopen,nfull,mismatch);
    fflush(stdout);
  }
  return 0;
}
