import json as j,os,urllib.request as u
U=os.environ["MAKEFUN_ENV_URL"]
P=lambda p,b:j.load(u.urlopen(U+p,data=j.dumps(b).encode()))
V=(0,100,320,330,500,900,0);N=(-33,-31,-18,-14,14,18,31,33);K=(-17,-16,-15,-1,1,15,16,17);I=(-17,-15,15,17);R=(-16,-1,1,16);A=(0,0,4,8,14,24,40,0);KK=(20,25,10,0,0,10,25,20);CR={0:2,7:1,112:8,119:4,4:3,116:12}
B=[0]*128;S=1;G=0;E=-1;KP=[0,0];ND=[0];LIM=60000;ST=[];SK=lambda m:-V[abs(B[m>>7&127])];BM=[0]
def F(f):
 global B,S,G,E,KP
 B=[0]*128;KP=[0,0];p=f.split();s=112
 for ch in p[0]:
  if ch=="/":s-=24
  elif ch.isdigit():s+=int(ch)
  else:
   v="PNBRQK".index(ch.upper())+1
   if ch.islower():v=-v
   B[s]=v
   if abs(v)==6:KP[0 if v>0 else 1]=s
   s+=1
 S=1 if p[1]=="w" else-1;G=0
 for ch in p[2]:G|={"K":1,"Q":2,"k":4,"q":8}.get(ch,0)
 E=-1 if p[3]=="-" else(int(p[3][1])-1)*16+ord(p[3][0])-97
def T(q,y):
 d=16*y
 for f in(-1,1):
  t=q-d+f
  if not t&136 and B[t]==y:return 1
 for o,pc in((N,2),(K,6)):
  for o2 in o:
   t=q+o2
   if not t&136 and B[t]==y*pc:return 1
 for o,ps in((I,(3,5)),(R,(4,5))):
  for o2 in o:
   t=q+o2
   while not t&136:
    v=B[t]
    if v:
     if abs(v) in ps and(v>0)==(y>0):return 1
     break
    t+=o2
 return 0
def M():
 m=[];a=m.append
 for q in range(128):
  if q&136:continue
  v=B[q]
  if not v or(v>0)!=(S>0):continue
  t=abs(v)
  if t==1:
   d=16*S;lr=7*(S>0);st=6-5*(S>0)
   for o in(d,d-1,d+1):
    to=q+o
    if to&136:continue
    c=B[to]
    if o==d:
     if c:continue
    elif c and(c>0)==(S>0) or not c and to!=E:continue
    if to>>4==lr:
     for p in(5,4,3,2):a(q|to<<7|p<<14)
    else:
     a(q|to<<7)
     if o==d and q>>4==st and not B[q+2*d]:a(q|(q+2*d)<<7)
  else:
   ds=N if t==2 else K if t==6 else I if t==3 else R if t==4 else I+R;sl=t>2 and t!=6
   for o in ds:
    to=q+o
    while not to&136:
     if B[to]:
      if(B[to]>0)!=(S>0):a(q|to<<7)
      break
     a(q|to<<7)
     if not sl:break
     to+=o
   if t==6:
    for x,b,g,r in((4,6,1,7),(4,2,2,0),(116,118,4,119),(116,114,8,112)):
     if q==x and G&g and B[r]==(4 if S>0 else-4):
      d=1 if b>x else-1;e=[x+d,x+2*d]+([x+3*d] if b<x else[])
      if all(not B[y] for y in e) and not any(T(x+i*d,-S) for i in(0,1,2)):a(x|b<<7)
 return m
def D(m):
 global S,G,E
 ST.append((B[:],S,G,E,KP[:]));f=m&127;t=m>>7&127;p=m>>14;v=B[f];c=B[t]
 B[t]=(p if v>0 else-p) if p else v;B[f]=0
 if abs(v)==6:KP[0 if v>0 else 1]=t
 if abs(v)==1 and t==E and not c:B[t-16*S]=0
 if abs(v)==6 and abs(t-f)==2:
  r=t+1 if t>f else t-2;B[t-1 if t>f else t+1]=B[r];B[r]=0
 E=(f+t)//2 if abs(v)==1 and abs(t-f)==32 else-1
 for s in(f,t):G&=~CR.get(s,0)
 S=-S
def W():
 global S,G,E
 B[:],S,G,E,KP[:]=ST.pop()
def Y():
 s=0
 for q in range(128):
  if q&136:continue
  v=B[q]
  if not v:continue
  t=abs(v);w=v>0;r=q>>4;f=q&7;c=min(f,7-f)+min(r,7-r);rr=r if w else 7-r
  if t==1:x=A[rr]
  elif t==2:x=6*c-20
  elif t==3:x=4*c-8
  elif t==4:x=15 if rr==6 else 0
  elif t==6:x=KK[f] if rr==0 else max(-50,-15*rr)
  else:x=2*c-6
  s+=(V[t]+x)*(w*2-1)
 return s*S
def Q(a,b):
 ND[0]+=1;st=Y()
 if st>=b:return b
 if st>a:a=st
 chk=T(KP[S<0],-S)
 ms=M() if chk else[x for x in M() if B[x>>7&127] or x>>14 or(x>>7&127)==E]
 ms.sort(key=SK)
 for m in ms:
  D(m)
  if T(KP[S>0],S):W();continue
  sc=-Q(-b,-a);W()
  if sc>=b:return b
  if sc>a:a=sc
 return a
def Z(a,b,d,pl):
 ND[0]+=1
 if ND[0]>LIM:raise StopIteration
 if d<=0:return Q(a,b)
 ms=M();ms.sort(key=SK);be=-10**9;bm=0
 for m in ms:
  D(m)
  if T(KP[S>0],S):W();continue
  sc=-Z(-b,-a,d-1,pl+1)
  W()
  if sc>be:be=sc;bm=m
  if sc>a:a=sc
  if a>=b:break
 if be==-10**9:return 0 if T(KP[S<0],-S) else-100000+pl
 if pl==0:BM[0]=bm
 return be
def H(lg):
 ND[0]=0;F(FN)
 for d in range(1,12):
  try:Z(-10**9,10**9,d,0)
  except StopIteration:break
  if ND[0]>LIM:break
 be=BM[0]
 if not be:return lg[0]
 f=be&127;t=be>>7&127
 return "%c%d%c%d"%(97+(f&7),(f>>4)+1,97+(t&7),(t>>4)+1)+("nbrq"[(be>>14)-2] if be>>14 else "")
FN=""
while 1:
 g=P("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":FN=g["fen"];g=P("/move",{"game":g["game"],"move":H(g["legal_moves"])})
