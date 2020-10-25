from plotly.offline import plot
import plotly.graph_objs as go

'''
	- jobs_dict = {
					key = jobs_name
					value = index_number
					}
	- file_dict = {
					key = file_name
					value = [
							list of source jobs,
							list of destination jobs,
							]
					}
'''

jobs_dict = {}
files_dict_in = {}
files_dict_out = {}

def read_input():
	'''
	Read the job list file:
	'''
	in_file = 'JOBS_03.txt'

	job_name = ''
	program_name = ''
	file_name = ''
	file_type = ''
	is_STEPCTLG = False
	is_SIGNCFT = False

	file1 = open(in_file,'r')
	lines = file1.read().splitlines()
	
	for line in lines:
		if line[:4] != 'V//*':
			if line[1:12] == 'MEMBER NAME':
				if job_name != '':
					jobs_dict.update({job_name : job_dict})

				job_name = line[14:22]
				job_dict = dict(
								idx = len(jobs_dict),
								input = [],
								output = [],
								program = ''
								)

			if line.find(' EXEC ') > -1:
				program_name = line[line.find(' EXEC ')+6:]
				program_name = program_name.replace('PGM=','')
				program_name = program_name.replace('PROC=','')
				program_name = program_name.replace(',','').strip()

				if line[3:11] != 'STEPCTLG':
					job_dict['program'] = program_name
					is_STEPCTLG = False
				else:
					is_STEPCTLG = True

			if line.find('PROG (') > -1:
				program_name = line[line.find('PROG (')+6:line.find(')')].strip()
				job_dict['program'] = program_name

			if line.find('DSN=') > -1:
				file_name = line[line.find('DSN=')+4:]
				file_name = file_name[:file_name.find(',')]
				if 'PARMEXP' not in file_name and file_name.find('(') > -1:
					file_name = file_name[:file_name.find('(')]

			if line.find('DISP=') > -1:
				file_type = line[line.find('DISP=')+5:]
				file_type = file_type[:file_type.find(',')].replace('(','')
				if file_name[0] != '&' and not is_STEPCTLG:
					if file_type == 'NEW':
						if file_name not in job_dict['output']:
							#print(job_dict['output'])
							job_dict['output'].append(file_name)
						try:
							mylist = files_dict_out[file_name]
							if job_name not in mylist:
								mylist.append(job_name)
						except:
							mylist = [job_name]
						files_dict_out.update({file_name : mylist})
					else:
						if file_name not in job_dict['input']:
							job_dict['input'].append(file_name)
						try:
							mylist = files_dict_in[file_name]
							if job_name not in mylist:
								mylist.append(job_name)
						except:
							mylist = [job_name]
						files_dict_in.update({file_name : mylist})
			
			if program_name == 'SIGNCFT':	#SIGNCFX
				if line.find('DSNAME=') > -1:
					file_name = line[line.find('DSNAME=')+8:]
					file_name = file_name.replace("'","").replace(",","").strip()
					job_dict['input'] = [file_name]
				if line.find('SUNNAME=') > -1:
					file_name = line[line.find('SUNNAME=')+8:line.find(',')]
					job_dict['output'] = [file_name]

			if program_name == 'EXISPOOL':
				if line.find('APPLI=') > -1:
					file_name = line[line.find('APPLI=')+6:].strip()
					job_dict['input'] = [file_name]
				if line.find('DDN001') > -1:
					file_name = line[line.find('DSN=')+4:line.find(',')]
					job_dict['output'] = [file_name]

	file1.close()
	if job_name != '':
		jobs_dict.update({job_name : job_dict})

def set_sankey_lists():
	line_dict = dict(color = "green", width = 0.5)
	label_list = []
	source_list = []
	target_list = []
	value_list = []

	for input_file in files_dict_in:
		for input_jobs in files_dict_in[input_file]:
			label_list.append(input_jobs)
			#print(files_dict_out[input_file])
			print(files_dict_in[input_file])
			print(files_dict_out[output_file])
			try:
				for output_jobs in files_dict_out[input_file]:
					print(jobs_dict[input_file]["idx"])
					source_list.append(jobs_dict[input_file]["idx"])
					print(jobs_dict[output_file]["idx"])
					target_list.append(jobs_dict[output_file]["idx"])
					value_list.append(1)
			except:
				pass
				'''
				try:
					source_list.append(jobs_dict[input_file]["idx"])
					target_list.append(jobs_dict[output_file]["idx"])
					target_list.append(1)
				except:
					pass
				'''
	#print(label_list)
	#print(source_list)
	#print(target_list)
	#print(value_list)

	node_dict = dict(
					pad = 15,
					thickness = 20,
					line = line_dict,
					label = label_list,
					color = "blue"
					)
	link_dict = dict(
					source = source_list,
					target = target_list,
					value = value_list
					)

	fig = go.Figure(data=[go.Sankey(
									node = node_dict,
									link = link_dict
									)])

	xaxis_dict = dict(rangeslider=dict(visible=True),type="linear")
	fig.update_layout(
					xaxis=xaxis_dict,
					title_text="Complex Sankey Diagram",
					font_size=10
					)
	plot(fig, auto_open=True)

if __name__== "__main__":
	read_input()
	file1 = open("jobs_dict.txt",'w')
	for mydict in jobs_dict:
		#print("1 - {0}: {1}".format(mydict,jobs_dict[mydict]))
		file1.writelines("{0}: {1}\n".format(mydict,jobs_dict[mydict]))
	file1.close()
	file1 = open("files_dict_in.txt",'w')
	for mydict in files_dict_in:
		#print("2 - {0}: {1}".format(mydict,files_dict_in[mydict]))
		file1.writelines("{0}: {1}\n".format(mydict,files_dict_in[mydict]))
		#if 'RDEBY01H' in files_dict_in[mydict]:
			#print(files_dict_in[mydict])
	file1.close()
	file1 = open("files_dict_out.txt",'w')
	for mydict in files_dict_out:
		#print("3 - {0}: {1}".format(mydict,files_dict_out[mydict]))
		file1.writelines("{0}: {1}\n".format(mydict,files_dict_out[mydict]))
	file1.close()
	set_sankey_lists()