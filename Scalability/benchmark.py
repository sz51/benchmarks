import os
import commands
import sys
import random
# files = os.listdir(".")
# for file in files:
# 	tmp = file.split(".")
# 	if(tmp[1] == "ltlf"):
# 		newname = tmp[0]+".mona"
# 	os.rename(file, newname)

# benchmark = open("ltlf.txt")
# i = 1
# for line in benchmark.readlines():
# 	if "(" in line:
# 		f = open(str(i)+'.ltlf', 'w')
# 		f.write(line)
# 		f.close()
# 		i = i + 1

# length = int(raw_input("input the length:\n"))  
# nvars = int(raw_input("input the number of variables:\n"))
# num = int(raw_input("input the number of cases:\n"))
# print 'length is %d\n' % length
# print 'the number of variables is %d\n' % num
num = 50
length = 1
while length <= 10:
	nvars = 100
	while nvars <= 500:
		n = 1
		while n <= num:
			Vars = []
			in_l = set()
			out_l = set()
			formulas = []
			j = 1
			while j <= nvars:
				Vars.append(j)
				j = j + 1
			a = 1
			while a <= length:
				in_items = [] 
				out_items = []  
				tmp = random.randint(1,20)
				# tmp = 17
				# print tmp
				f = open('cases/'+str(tmp)+'.ltlf')
				formula = f.readline().strip('\n')
				p = open('cases/'+str(tmp)+'.part')
				for line in p.readlines():
					if 'inputs' in line:
						line = line.split(":")[1].strip('\n')
						line = line.split(" ")
						i = 1
						while i < len(line):
							in_items.append(line[i])
							i = i + 1
					if 'outputs' in line:
						line = line.split(":")[1].strip('\n')
						line = line.split(" ")
						i = 1
						while i < len(line):
							out_items.append(line[i])
							i = i + 1
				
				for ins in in_items:
					ran = random.choice(Vars)
					Vars.remove(ran)
					formula = formula.replace(ins, 'P'+str(ran))
					in_l.add('P'+str(ran))
				
				for outs in out_items:
					ran = random.choice(Vars)
					Vars.remove(ran)
					formula = formula.replace(outs, 'P'+str(ran))
					out_l.add('P'+str(ran))
				formulas.append('(')
				formulas.append(formula)
				formulas.append(')')
				formulas.append(' & ')
				a = a + 1
			formulas.pop()
			newformula = ""
			for fl in formulas:
				fl = fl.strip('\r')
				newformula = newformula + fl

			newpart = ".inputs: "
			for item in in_l:
				newpart = newpart + item + ' '
			newpart = newpart.rstrip() + "\n.outputs: "
			for item in out_l:
				newpart = newpart + item  + ' '
			newpart = newpart.rstrip()

			path = 'case_'+str(length)+'_'+str(nvars)+'_'+str(num)
			isExists=os.path.exists(path)
			if not isExists:
				os.mkdir(path)
			ff = open(path+'/'+str(n)+'.ltlf', 'w')
			ff.write(newformula)
			ff.close()
			fp = open(path+'/'+str(n)+'.part', 'w')
			fp.write(newpart)
			fp.close()
			n = n + 1
		nvars = nvars + 50
	length = length + 1

