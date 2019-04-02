from afd import AFD,AFDState
from afn import AFN,AFNState,Epsilon
from itertools import chain,combinations
from sys import argv,exit
from ast import literal_eval as leval
def readAfnFromFile(filename):
	f=open(filename)
	states=list(leval(f.readline().strip()))
	sigma=[Epsilon()]+list(f.readline().strip())
	delta=[]
	for i in range(len(states)):
		temp=leval(f.readline().strip())
		if len(temp)!=len(sigma):raise RuntimeError("invalid delta on "+filename)
		for t in temp:
			if len(t)>len(sigma):raise RuntimeError("invalid delta on "+filename)
			for tt in t:
				if tt not in states:
					raise RuntimeError("invalid delta on "+filename)
		delta.append(list(temp))
	initial=leval(f.readline().strip())
	if initial not in states:raise RuntimeError("invalid initial on "+filename)
	final=leval(f.readline().strip())
	final=list(final)if type(final)==tuple else [final]
	for temp in final:
		if temp not in states:raise RuntimeError("invalid final on "+filename)
	f.close()
	return AFN(states,sigma,delta,initial,final)

def powerset(s):
    ans=list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    return [list(elem) for elem in ans]
def depthSearchEpsilon(fdn,state):
	ans=[]
	stack=[state]
	while(stack!=[]):
		aux=stack.pop()
		ans.append(aux.name)
		stack+=aux.feed(Epsilon())
	ans.sort()
	return ans
def fdn2fda( fdn ):
	states=[elem.name for elem in fdn.q]
	new_states_name=powerset(states)
	new_initial_name=depthSearchEpsilon(fdn,fdn.initial)
	new_initial_name=str(new_initial_name)

	new_final_names=[]
	final=[]
	for elem in fdn.q:
		if "f" in elem.flag:
			final.append(elem.name)
	for f in final:
		for n in new_states_name:
			if (f in n) and (n not in new_final_names):
				new_final_names.append(n)
	
	new_delta=[list() for _ in range(len(new_states_name))]
	s=len(fdn.sigma)-1

	new_delta[0]=[[]]*s
	#estados n==1
	for i,qs in enumerate(fdn.delta):
		for j in range(s):
			temp=fdn.delta[i][j+1]
			if temp!=None:
				ds=set()
				for t in temp:
					ds=ds.union(depthSearchEpsilon(fdn,fdn.q[fdn.q.index(t)]))
				temp=list(set(temp).union(ds))
				temp.sort()

			new_delta[i+1].append(temp)


	#estados n>1
	for i,sn in enumerate(new_states_name[1::]):
		if len(sn)==1:continue
		for j in range(s):
			u=set()
			for k in sn:
				temp=new_delta[new_states_name.index([k])][j]
				if temp==None:continue
				u=u.union(temp)
			u=list(u)
			u.sort()
			new_delta[i+1].append(u)
		pass
	#limpar, converter tudo para str
	for i in range(len(new_states_name)):
		new_states_name[i]=str(new_states_name[i])
	for i in range(len(new_final_names)):
		new_final_names[i]=str(new_final_names[i])
	for i in range(len(new_delta)):
		for j in range(len(new_delta[i])):
			elem=new_delta[i][j]
			if elem==None:
				new_delta[i][j]="[]"
			else:
				new_delta[i][j]=str(elem)

	# print("q:",new_states_name)
	# print("sigma:",fdn.sigma[1::])

	# print("delta:")
	# for r in new_delta:
	# 	print(r)
	# print("initial:\"%s\""%new_initial_name)
	# print("finals:",new_final_names)
	return AFD(new_states_name,fdn.sigma[1::],new_delta,new_initial_name,new_final_names)	

if len(argv)<1:
	print("[USO]fdn2fda.py [arquivo]")
	exit(-1)
fdn=readAfnFromFile(argv[1])

fda=fdn2fda(fdn)
print("\nEstados:")
print([q.name for q in fda.q])
print("\nSigma:")
print(fda.sigma)
print("\nDelta:")
for q in fda.q:
	print([qq.name for qq in q.t.values()])
print("\nEstado inicial:")
print(fda.initial.name)
print("\nEstados finais:")
finals=[]
for q in fda.q:
	if "f" in q.flag:
		finals.append(q.name)
print(finals)
	

# print(fda.feed("baa"))


# while(True):
# 	u=input()
# 	print("AFN:%s AFD:%s"%(fdn.feed(u),fda.feed(u)))
# 	fdn.reset()
# 	fda.reset()