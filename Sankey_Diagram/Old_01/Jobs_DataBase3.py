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

files_to_ignore = []
files_to_ignore.append("PIN2PAP.PARMEXP(EQUALS)")
files_to_ignore.append("CDA9.EXPL.DIALOG.EXE")
files_to_ignore.append("PDEUEXP.PRIVATE.TCPIP.LOGON")
files_to_ignore.append("PDEUEXP.PRIVATE.CA7.LOGON")
files_to_ignore.append("CDA9.CA7.SY0C.COMMDS")
files_to_ignore.append("PIN2QSM.MAIL.ALERTE.BTI")
files_to_ignore.append("*.STEP0020.FILESEQS")
files_to_ignore.append("*.STEP0020.SYSPRINT")
files_to_ignore.append("CDA9.VFI.SY0C.BKUPTBL")
files_to_ignore.append("CDA9.VFI.SY0C.BKUPAUD")
files_to_ignore.append("PDEUVSM.MSGABS")
files_to_ignore.append("PDEUVSM.APBGUI")
files_to_ignore.append("PDEUVSM.GEO41OHF")
files_to_ignore.append("PDEUVSM.GEO41OSF")
files_to_ignore.append("PDEUVSM.GEO41SHF")
files_to_ignore.append("PDEUVSM.GEO41SSF")
files_to_ignore.append("CDS9.ISPOOL.LOADISPO.BA")
files_to_ignore.append("PDEUVSM.EPUCLC")
files_to_ignore.append("PDEUVSM.EPUDOC")
files_to_ignore.append("CDA9.CA7.SY0C.PARMLIB")
files_to_ignore.append("PDEUPAP.PDEGD515.ARCO")

jobs_dict = {}
in_files_dict = {}
out_files_dict = {}
in_file = 'JOBS_06.txt'
job_name = ''
program_name = ''
file_name = ''
file_type = ''
is_STEPCTLG = False
is_SIGNCFT = False
file2 = open("for testing.txt",'w')
file3 = open("for testing2.txt",'w')
progs = []

def read_input():
	'''
	Read the job list file:
	'''
	file1 = open(in_file,'r')
	job_name = ''
	program_name = ''
	
	while True:
		line = file1.readline()
		if not line:
			break
		if line[:3] != "//*":
			if " JOB " in line and line[:2] == "//":
				try:
					file3.writelines("{0} - {1}\n".format(job_name,jobs_dict[job_name]))
				except:
					pass
				job_name = line[line.find('//')+2:line.find('JOB')].strip()
				job_dict = dict(
								idx = len(jobs_dict),
								input = [],
								output = [],
								program = ''
								)
				jobs_dict.update({job_name : job_dict})
				is_STEPCTLG = False

			if " EXEC " in line and line[:2] == "//":
				if line[:10] == "//STEPCTLG":
					is_STEPCTLG = True
				else:
					is_STEPCTLG = False

				if "PGM=" in line:
					program_name = line[line.find("PGM=")+4:line.find(",")].strip()
				elif "PROC=" in line:
					program_name = line[line.find("PROC=")+5:line.find(",")].strip()
				else:
					program_name = line[line.find(" EXEC ")+6:line.find(",")].strip()
				if program_name != "DB2BATCH" and not is_STEPCTLG:
					jobs_dict[job_name]["program"] = program_name
					file2.writelines("{0} - {1}\n".format(job_name,program_name))

			if "RUN PROG" in line and not is_STEPCTLG:
				program_name = line[line.find("(")+1:line.find(")")].strip()
				jobs_dict[job_name]["program"] = program_name
				file2.writelines("{0} - {1}\n".format(job_name,program_name))

			if "DSN=" in line and not is_STEPCTLG:
				file_name = line[line.find("DSN=")+4:].strip()
				file_name = file_name[:file_name.find(",")].strip()
				if "PIN2PAP" not in file_name and file_name.find("(") >= 0:
					file_name = file_name[:file_name.find("(")]


			if "DSNAME=" in line and program_name == "SIGNCFT" and not is_STEPCTLG:
				file_type = "input"
				file_name = line[line.find("DSNAME=")+8:].strip()
				file_name = file_name[:file_name.find("'")]
				if file_name not in jobs_dict[job_name][file_type]:
					jobs_dict[job_name][file_type].append(file_name)
					update_file_dict(file_name,job_name,file_type)
				file2.writelines("{0}\t\t{1}\n".format(file_type,file_name))

			if "SUNNAME=" in line and program_name == "SIGNCFT" and not is_STEPCTLG:
				file_type = "output"
				file_name = line[line.find("SUNNAME=")+8:line.find(",")]
				if file_name not in jobs_dict[job_name][file_type]:
					jobs_dict[job_name][file_type].append(file_name)
					update_file_dict(file_name,job_name,file_type)
				file2.writelines("{0}\t\t{1}\n".format(file_type,file_name))

			if "APPLI=" in line and program_name == "EXISPOOL" and not is_STEPCTLG:
				file_type = "input"
				file_name = line[line.find("APPLI=")+6:].strip()
				if file_name not in jobs_dict[job_name][file_type]:
					jobs_dict[job_name][file_type].append(file_name)
					update_file_dict(file_name,job_name,file_type)
				file2.writelines("{0}\t\t{1}\n".format(file_type,file_name))

			if "APPLI=" in line and program_name == "RGISPOOL" and not is_STEPCTLG:
				file_type = "output"
				file_name = line[line.find("APPLI=")+6:].strip()
				if file_name not in jobs_dict[job_name][file_type]:
					jobs_dict[job_name][file_type].append(file_name)
					update_file_dict(file_name,job_name,file_type)
				file2.writelines("{0}\t\t{1}\n".format(file_type,file_name))

			if "DISP=" in line and not is_STEPCTLG:
				if "NEW" in line or (program_name == "FDXDOS" and "&DISPO" in line):
					file_type = "output"
				else:
					file_type = "input"
				if file_name not in files_to_ignore and file_name[:2] != "&&":
					if file_name not in jobs_dict[job_name][file_type] and file_name not in jobs_dict[job_name]["input"]:
						jobs_dict[job_name][file_type].append(file_name)
						update_file_dict(file_name,job_name,file_type)
					file2.writelines("{0}\t\t{1}\n".format(file_type,file_name))
			if program_name not in progs and program_name != '':
				progs.append(program_name)

	file1.close()
	file2.close()
	file3.close()
	file4 = open("for testing3.txt",'w')
	progs.sort()
	#for my_progs in progs:
	for my_progs in in_files_dict:
		file4.writelines("{0} --> {1}\n".format(my_progs, in_files_dict[my_progs]))
		if len(in_files_dict[my_progs]['output']) > 1:
			print("{0} --> {1}\n".format(my_progs, in_files_dict[my_progs]))

	file4.close()

def update_file_dict(my_file, my_job, my_type):
	if my_type == 'input':
		try:
			if my_job not in in_files_dict[my_file][my_type]:
				in_files_dict[my_file][my_type].append(my_job)
		except:
			file_dict = dict(
							input = [my_job],
							output = [],
							)
			in_files_dict.update({my_file : file_dict})
	else:
		try:
			if my_job not in in_files_dict[my_file][my_type]:
				in_files_dict[my_file][my_type].append(my_job)
		except:
			file_dict = dict(
							input = [],
							output = [my_job],
							)
			in_files_dict.update({my_file : file_dict})


if __name__== "__main__":
	read_input()
