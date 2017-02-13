def format(f, p):
	f = open(f)
	p = open(p)

	var = []
	inputs = []
	outputs = []
	inidle = 0
	outidle = 0
	for line in p.readlines():
		if "input" in line:
			line = line.strip().split(" ")
			for item in line:
				if((item != ".inputs") & (item != "idle")):
					var.append(item)
					inputs.append(item)
			if "idle" in line:
				inidle = 1
		if "output" in line:
			line = line.strip().split(" ")
			for item in line:
				if((item != ".outputs") & (item != "idle")):
					var.append(item)
					outputs.append(item)
			if "idle" in line:
				outidle = 1
	# print inputs
	# print outputs

	f.readline()
	con = []
	res = []
	idle = 0
	for line in f.readlines():
		if ";" in line:
			if "idle" in line:
				var.append("idle")
				idle = 1
			for v in var:
				line = line.strip().replace(v+"=0", "!"+v)
				line = line.replace(v+"=1", v)
				line = line.replace("*", "&")
				line = line.replace("+", "|")
			line = line.replace(";", " ")
			if "assume" in line:
				line = line.replace("assume", " ")
				con.append(line)
				con.append("&")
			else:
				res.append(line)
				res.append("&")

	con.append("true")
	res.append("true")

	formula = []
	formula.append("((")
	for item in con:
		formula.append(item)
	formula.append(")->(")
	for item in res:
		formula.append(item)
	formula.append("))")

	return formula, inputs, outputs, idle, inidle, outidle

if __name__=="__main__":
	i = 0
	while i <= 79:
		fname = "Acacia/load_"+str(i)+".ltl"
		pname = "Acacia/load_"+str(i)+".part"
		(formula, inv, outv, idle, inidle, outidle) = format(fname, pname)
		f = open("acacia/"+str(i)+".ltlf", "w")
		for it in formula:
			print >> f, it,
		f.close();
		p = open("acacia/"+str(i)+".part", "w")
		print >> p, ".inputs: ",
		for it in inv:
			print >> p, it.upper(),
		if (idle == 1) & (inidle == 1):
			print >> p, "IDLE",
		print >> p, "\n",
		print >> p, ".outputs: ",
		if (idle == 1) & (outidle == 1):
			print >> p, "IDLE",
		for it in outv:
			print >> p, it.upper(),
		i = i + 1



