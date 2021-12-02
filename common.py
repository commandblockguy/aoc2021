from aocd import data, submit
import aocd

def run(ex1, res1, p1, ex2, res2, p2, mode, do_submit):
	if not ex2: ex2 = ex1
	run_part(ex1, res1, p1, 'A', mode, do_submit)
	if p2:
		run_part(ex2, res2, p2, 'B', mode, do_submit)

def run_part(ex, ex_res, f, part, mode, do_submit):
	if mode == 'lines':
		ex = ex.splitlines()
	elif mode == 'nums':
		ex = [int(n) for n in ex.splitlines()]
	d = data
	if mode == 'lines':
		d = data.splitlines()
	elif mode == 'nums':
		d = [int(n) for n in data.splitlines()]
	actual = f(ex)
	if actual == ex_res:
		print('Part', part, 'passed example:', ex_res)
		result = f(d)
		print('Part', part, 'result:', result)
		if do_submit:
			submit(result, part=part)
			print('Submitted!')
		else:
			print('Not submitting - remember to enable safety toggle')
	else:
		print('Part', part, 'failed:')
		print('expected:', ex_res, 'actual:', actual)