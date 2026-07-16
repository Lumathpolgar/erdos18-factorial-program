#include <algorithm>
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/rational.hpp>
#include <cstdint>
#include <iostream>
#include <limits>
#include <queue>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>
using boost::multiprecision::cpp_int; using Rational=boost::rational<cpp_int>; using u128=unsigned __int128; using u64=uint64_t;
struct Err:std::runtime_error{using std::runtime_error::runtime_error;};
std::string dec(u128 x){if(!x)return"0";std::string s;while(x){s.push_back(char('0'+unsigned(x%10)));x/=10;}std::reverse(s.begin(),s.end());return s;}
u128 p128(const std::string&s){u128 x=0;for(char c:s){u128 o=x;x=x*10+(c-'0');if(x<o)throw Err("overflow");}return x;}
int cr(const Rational&x){cpp_int q=x.numerator()/x.denominator();if(x.numerator()%x.denominator()!=0&&x.numerator()>0)++q;return q.convert_to<int>();}
std::pair<Rational,Rational> lp(int a,int b,int N){Rational z(cpp_int(a-b),cpp_int(a+b)),z2=z*z,p=z,s(0);for(int j=0;j<N;j++){s+=p/Rational(2*j+1);p*=z2;}Rational lo=2*s;return{lo,lo+2*p/(Rational(2*N+1)*(Rational(1)-z2))};}
std::pair<int,int> pars(int n){int e=0;while((1LL<<(e+1))<=n)e++;int sc=1<<e;for(int N:{8,12,16,24,32,48,64,96}){auto a=lp(2,1,N),b=lp(n,sc,N);Rational lo=Rational(e)*a.first+b.first,hi=Rational(e)*a.second+b.second;int r1=cr(4*lo),r2=cr(4*hi),m1=cr(16*lo*lo),m2=cr(16*hi*hi);if(r1==r2&&m1==m2)return{r1,m1};}throw Err("params");}
std::vector<int> ps(int n){std::vector<bool>a(n+1,true);a[0]=a[1]=false;std::vector<int>p;for(int i=2;i<=n;i++)if(a[i]){p.push_back(i);if(1LL*i*i<=n)for(int j=i*i;j<=n;j+=i)a[j]=false;}return p;}
int vp(int n,int p){int s=0;while(n){n/=p;s+=n;}return s;} cpp_int fac(int n){cpp_int x=1;for(int i=2;i<=n;i++)x*=i;return x;} cpp_int isq(const cpp_int&v){cpp_int l=0,h=cpp_int(1)<<((boost::multiprecision::msb(v)+2)/2+1);while(l+1<h){cpp_int m=(l+h)/2;if(m*m<=v)l=m;else h=m;}return l;}
struct PE{int p,e;u64 c;};
void gen(const std::vector<PE>&f,int i,u128 x,std::vector<u128>&out){if(i==(int)f.size()){out.push_back(x);return;}u128 cur=x;for(int k=0;k<=f[i].e;k++){gen(f,i+1,cur,out);if(k<f[i].e)cur*=unsigned(f[i].p);}}
struct H{u128 v;uint32_t r,c;}; struct G{bool operator()(const H&a,const H&b)const{return a.v>b.v;}};
int main(int argc,char**argv){try{int n=52;bool have_mask=false;uint64_t requested_mask=0;if(argc>1)n=std::stoi(argv[1]);if(argc>2){requested_mask=std::stoull(argv[2]);have_mask=true;}if(argc>3)throw Err("usage: marker_three_mitm_prefix_u128 [n] [partition_mask]");auto[r,M]=pars(n);int v2=vp(n,2);std::vector<PE>f;u64 total=1;for(int p:ps(n)){if(p==2)continue;int e=vp(n,p)-(p==3);if(e>0){f.push_back({p,e,u64(e+1)});total*=u64(e+1);}}
cpp_int Yb=isq(fac(n))/3;std::string ys=Yb.convert_to<std::string>();if(ys.size()>38)throw Err("Y too large");u128 Y=p128(ys),W=((u128(1)<<r)-3)/3;
size_t m=f.size();u64 besta=0,bestb=0;uint64_t bestmask=0;cpp_int bestdiff=-1;for(uint64_t mask=0;mask<(1ULL<<m);mask++){u64 a=1;for(size_t i=0;i<m;i++)if(mask>>i&1)a*=f[i].c;u64 b=total/a;cpp_int d=a>b?a-b:b-a;if(bestdiff<0||d<bestdiff){bestdiff=d;besta=a;bestb=b;bestmask=mask;}}
if(have_mask){if(m>=64||requested_mask>=(1ULL<<m))throw Err("partition mask out of range");bestmask=requested_mask;besta=1;for(size_t i=0;i<m;i++)if((bestmask>>i)&1)besta*=f[i].c;bestb=total/besta;}std::vector<PE>fa,fb;for(size_t i=0;i<m;i++)((bestmask>>i)&1?fa:fb).push_back(f[i]);std::vector<u128>A,B;A.reserve(besta);B.reserve(bestb);gen(fa,0,1,A);gen(fb,0,1,B);std::sort(A.begin(),A.end());std::sort(B.begin(),B.end());if(A.size()*B.size()!=total)throw Err("MITM count mismatch");if(std::adjacent_find(A.begin(),A.end())!=A.end()||std::adjacent_find(B.begin(),B.end())!=B.end())throw Err("duplicate half divisor");if(A.size()>B.size()){std::swap(A,B);}std::cerr<<"split="<<A.size()<<"x"<<B.size()<<" total="<<total<<"\n";
std::priority_queue<H,std::vector<H>,G>q;for(uint32_t i=0;i<A.size();i++){u128 v=A[i]*B[0];if(v<=Y)q.push({v,i,0});}
u128 E=0,prev=0;u64 count=0;int t=1,used=0;u128 scale=1,D=(E+W+1),bound=Y;cpp_int prod=1;std::vector<std::string>rows;auto resolve=[&](bool blocked,u128 left,u64 K,u128 right,u128 gap){u128 umax=left;E+=scale*umax;used++;prod*=cpp_int(K)+1;std::string row="layer="+std::to_string(t)+",scale="+dec(scale)+",core_bound="+dec(bound)+",gap_threshold="+dec(D)+",connected_max_core="+dec(umax)+",connected_count="+std::to_string(K)+",carrier_endpoint="+dec(E);if(blocked)row+=",first_blocking_left="+dec(left)+",first_blocking_right="+dec(right)+",first_blocking_gap="+dec(gap);else row+=",first_blocking_gap=NONE";rows.push_back(row);};
while(true){if(q.empty()){resolve(false,prev,count,0,0);break;}H h=q.top();q.pop();u128 d=h.v;if(d>bound){resolve(false,prev,count,0,0);if(E+W<Y)throw Err("no-block layer did not finish certificate; continuation requires replay");break;}if(d<=prev)throw Err("non-increasing or duplicate divisor stream");u128 gap=d-prev;bool reeval=true;while(reeval&&gap>D){resolve(true,prev,count,d,gap);if(E+W>=Y){reeval=false;break;}t++;scale=u128(1)<<(t-1);bound=Y/scale;D=(E+W+1)/scale;if(d>bound)throw Err("next bound already passed after blocked layer");}
if(E+W>=Y)break;prev=d;count++;uint32_t nc=h.c+1;if(nc<B.size()){u128 nv=A[h.r]*B[nc];if(nv<=Y)q.push({nv,h.r,nc});}
if(count%10000000ULL==0)std::cerr<<"progress="<<count<<",heap="<<q.size()<<",layer="<<t<<"\n";
}
u128 occ=E+W;cpp_int req=(Yb+cpp_int(W)+1)/(cpp_int(W)+1),ratio=prod/req;std::cout<<"schema=nova1.marker-three-mitm-prefix-u128.v1\nresult_class=finite certificate\nn="<<n<<"\nr="<<r<<"\nM="<<M<<"\nv2_factorial="<<v2<<"\nY="<<dec(Y)<<"\nW="<<dec(W)<<"\ntotal_odd_core_divisor_count="<<total<<"\nmitm_partition_mask="<<bestmask<<"\nmitm_rows="<<A.size()<<"\nmitm_columns="<<B.size()<<"\nemitted_until_certificate="<<count<<"\nmaximum_heap="<<A.size()<<"\n";for(auto&s:rows)std::cout<<s<<"\n";std::cout<<"layers_used="<<used<<"\ncarrier_endpoint="<<dec(E)<<"\noccupied_through="<<dec(occ)<<"\nmargin="<<(occ>=Y?dec(occ-Y):std::string("-")+dec(Y-occ))<<"\nreaches_full_endpoint="<<(occ>=Y?"true":"false")<<"\nterm_bound="<<r+used<<"\nconnected_prefix_product="<<prod<<"\nfinite_requirement_ceiling="<<req<<"\nproduct_floor_ratio="<<ratio<<"\n";return occ>=Y?0:2;}catch(std::exception&e){std::cerr<<"FAIL: "<<e.what()<<"\n";return 1;}}
