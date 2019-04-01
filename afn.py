from afd import AFD,AFDState
import threading
import copy
import traceback
class Epsilon:
	def __eq__(self,obj):
		return type(obj)==Epsilon
	def __hash__(self):
		return hash("Epsilon")
	def __str__(self):
		return "(Epsilon)"
	def __repr__(self):
		return self.__str__()
class AFNState(AFDState):
	def __init__(self,afdstate):
		if type(afdstate)!=AFDState:raise ValueError()
		self.name=afdstate.name
		self.t=afdstate.t
		self.flag=afdstate.flag
	def feed(self,l):
		ans=copy.copy(super().feed(l))
		return [] if ans==None else ans
	def __str__(self):
		return "AFNState(%s)"%self.name
	def addTransition(self,symbol,childlist):
		if type(childlist)!=list:raise RuntimeError("invalid childlist argument")
		for c in childlist:
			if type(c)!=AFNState:raise RuntimeError("invalid childlist argument")
		self.t[symbol]=childlist

class AFN(AFD):
	def __init__(self,q,sigma,delta,initial,finals):
		self.threads=[]
		if Epsilon()!= sigma[0]:raise RuntimeError("Epsilon must be the first in the alphabet")
		super().__init__(q,sigma,delta,initial,finals)
		for i in range(len(self.q)):
			self.q[i]=AFNState(self.q[i])
			if "i" in self.q[i].flag:
				self.initial=self.q[i]
		m=len(delta)
		n=len(delta[0])
		for i in range(m):
			for j in range(n):
				statename=delta[i][j]
				if statename==None:continue
				if type(statename)!=list:raise RuntimeError("invalid delta")
				child=[]
				for childname in statename:
					try:child.append(self.q[self.q.index(childname)])
					except ValueError:raise RuntimeError("Invalid delta")
				if child==[]:continue
				self.q[i].addTransition(self.sigma[j],child)
			pass
		self.reset()
	def reset(self):
		if type(self.initial)==AFDState:return
		self.currstate=self.initial
		for t in self.threads:t[1].join()
		self.threads=[]
	def isLanguage(self):
		ans=super().isLanguage()
		
		print("[isLanguage] %s"%(self.currstate))
		
		for t in self.threads:
			if ans: t[0].currstate=None
			t[1].join()
			ans|=t[0].isLanguage()
		return ans
	def __createThreads(self,stateList,word):
		if stateList==[]:return
		
		tn=threading.current_thread().getName()
		tn="1" if tn=="MainThread" else tn

		print("[%s branching ]%s"%(tn,stateList))

		tb=self.threads
		self.threads=[]
		for state in stateList:
			
			obj=copy.deepcopy(self)
			obj.currstate=state

			t=threading.Thread(name=tn+" "+str(len(tb)+1),target=AFN.feed, args=(obj,word,))
			t.start()
			tb.append([obj,t])
		self.threads=tb
	def feed(self,word):
		tn=threading.current_thread().getName()
		tn="1" if tn=="MainThread" else tn

		print("[%s starting] word:%s currstate:%s"%(tn,word,self.currstate))
		if self.currstate==None:
			print("[%s dead]%s"%(tn,self.currstate))
			return False
		for wi,l in enumerate(word):
			if l not in self.sigma:raise RuntimeError("word not in sigma")
			nextState=self.currstate.feed(l)
			if nextState == []:
				nextState=self.currstate.feed(Epsilon())
				if nextState==[]:
					print("[%s \"dead\"]%s"%(tn,self.currstate))
					return False 
					# continue
			else:
				self.__createThreads(self.currstate.feed(Epsilon()),word)
			print("[%s going to]  %s( %s )->%s"%(tn,self.currstate,l,nextState))
			self.currstate=nextState.pop()
			self.__createThreads(nextState,word[wi::])
		return self.isLanguage()


if __name__=="__main__":
	q=["q1","q2","q3","q4","q5","q6"]
	sigma=[Epsilon(),"0"]
	delta=[[] for _ in q]

	delta[0]=[["q2","q3"],None]
	delta[1]=[None,      ["q4"]]
	delta[2]=[None,      ["q5"]]
	delta[3]=[None,      ["q2"]]
	delta[4]=[None,      ["q6"]]
	delta[5]=[None,      ["q3"]]

	initial="q1"
	finals=["q2","q3"]
	
	aut=AFN(q,sigma,delta,initial,finals)
	msg=""
	print(msg,aut.feed(msg))
	aut.reset()
	msg="0"
	print(msg,aut.feed(msg))
	aut.reset()
	msg="00"
	print(msg,aut.feed(msg))
	aut.reset()
	msg="000"
	print(msg,aut.feed(msg))
	aut.reset()
	msg="0000"
	print(msg,aut.feed(msg))
	aut.reset()
	msg="00000"
	print(msg,aut.feed(msg))
	aut.reset()
	msg="000000"
	print(msg,aut.feed(msg))
	aut.reset()
