from plotly.offline import plot
import plotly.graph_objs as go


file_name = "input_file.txt"

file1 = open(file_name,'r')
lines = file1.read().splitlines()
input_list = []
jobs_dict = {}
files_dict = {}
i = 0
for line in lines:
  input_list = line.split(",")
  #print(input_list)
  if input_list[0] not in jobs_dict:
    jobs_dict.update({input_list[0] : i})
    i += 1

  if input_list[4] not in files_dict:
    if input_list[5] == "NEW":
      file_usage = [input_list[0]]
    else:
      file_usage = [0, input_list[0]]
  else:
    file_usage = files_dict[input_list[4]]
    if input_list[5] == "NEW":
      file_usage[0] = [input_list[0]]
    else:
      file_usage.append(input_list[0])

  files_dict.update({input_list[4] : file_usage})
file1.close()

#print(jobs_dict)
#print(files_dict)

jobs_list = list(jobs_dict.keys())

label_list = list(jobs_dict.keys())
source_list = []
target_list = []
for myfiles in files_dict:
  for myjobs in files_dict[myfiles][1:]:
    source_list.append(jobs_dict[files_dict[myfiles][0]])
    target_list.append(jobs_dict[myjobs])
value_list = []
for i in range(len(source_list)):
  value_list.append(1)

line_dict = dict(color = "green", width = 0.5)

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
