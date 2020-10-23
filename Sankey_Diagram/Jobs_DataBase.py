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
	Read the settings file and fill the dictionary with global settings
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
							job_dict['output'].append(file_name)
						try:
							mylist = files_dict_in[file_name]
							if job_name not in mylist:
								mylist.append(job_name)
						except:
							mylist = [job_name]
						files_dict_in.update({file_name : mylist})
					else:
						if file_name not in job_dict['input']:
							job_dict['input'].append(file_name)
						try:
							mylist = files_dict_out[file_name]
							if job_name not in mylist:
								mylist.append(job_name)
						except:
							mylist = [job_name]
						files_dict_out.update({file_name : mylist})
			
			if program_name == 'SIGNCFT':
				if line.find('DSNAME=') > -1:
					file_name = line[line.find('DSNAME=')+8:]
					file_name = file_name.replace("'","").replace(",","").strip()
					job_dict['input'] = file_name
				if line.find('SUNNAME=') > -1:
					file_name = line[line.find('SUNNAME=')+8:line.find(',')]
					job_dict['output'] = file_name

			if program_name == 'RGISPOOL':
				if line.find('DDN001') > -1:
					file_name = line[line.find('DSN=')+4:]
					file_name = file_name.replace(",","").strip()
					job_dict['output'] = file_name
				if line.find('SUNNAME=') > -1:
					file_name = line[line.find('SUNNAME=')+8:line.find(',')]
					job_dict['input'] = file_name

	file1.close()
	if job_name != '':
		jobs_dict.update({job_name : job_dict})

if __name__== "__main__":
	read_input()
	for mydict in jobs_dict:
		print("1 - {0}: {1}".format(mydict,jobs_dict[mydict]))
	for mydict in files_dict_in:
		print("2 - {0}: {1}".format(mydict,files_dict_in[mydict]))
	for mydict in files_dict_out:
		print("3 - {0}: {1}".format(mydict,files_dict_out[mydict]))