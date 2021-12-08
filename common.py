from aocd import data, submit
import aocd

def run(ex1, res1, p1, ex2, res2, p2, inp_transf, do_submit):
	if inp_transf == None:
		inp_transf = lambda x: x
	_run_part(ex1, res1, p1, 'A', inp_transf, do_submit)
	if p2:
		_run_part(ex2, res2, p2, 'B', inp_transf, do_submit)

def _run_part(ex, ex_res, f, part, inp_transf, do_submit):
	actual = f(inp_transf(ex))
	if actual == ex_res:
		print('Part', part, 'passed example:', ex_res)
		result = f(inp_transf(data))
		print('Part', part, 'result:', result)
		if do_submit:
			submit(result, part=part)
			print('Submitted!')
		else:
			print('Not submitting')
	else:
		print('Part', part, 'failed:')
		print('expected:', ex_res, 'actual:', actual)

def lines(x):
	return x.splitlines()

def nums(x):
	return [int(n) for n in x.splitlines()]

def dbl_lines(x):
	return x.split('\n\n')

def csv(x):
	return [int(n) for n in x.split(',')]
