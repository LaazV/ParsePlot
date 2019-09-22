import sys, re, os, importlib
import julian

beginDate = []
endDate = []
seeing = []
julianDate = []
y_vertice = []


def main():
	os.system('cls')
	print("\nScript initializated")
	try:
		file = sys.argv[1]
	except (IndexError) as e:
		print("Error Opening File. Aborting")
		#file = 'data.txt'
		abort()

	if(filterData(file)):
		print("Converting JulianDate to Standard DateTime", end="", flush=True)
		if (convertJulian(beginDate,endDate)):
			print(" ..................... [SUCCESS]")
		else:
			print(" ..................... [FAIL]")

		print("Savind to file", end="", flush=True)

		if(1):
			output = open("custom.js", "w")
			output.write("var data=[{\nx:[")
			one = 1
			for item in y_vertice:
				if (one == 1):
					output.write("\"%s\"" % item)
					one = 0
				else:
  					output.write(",\"%s\"" % item)
			output.write("], \ny: [")
			one = 1
			for item in seeing:
				if (one == 1):
					output.write("\"%s\", "% item)
					one = 0
				else:
					output.write(",\"%s\""% item)
			output.write("],")
			output.write("""
				type: 'scatter',
				mode: 'lines+markers',
				marker: {
				color: 'rgb(55,128,191)',
				width: 6
				},
				connectgaps: true
				}];
				var layout = {
				title: 'Seeing (Arcsec)',
				xaxis: {
					title: 'Time'
				},
				yaxis: {
					title: 'Arcsec'
				}
				};
				Plotly.newPlot('graph', data, layout);
  				""")

			output.close()


			print(" ................................................. [SUCCESS]")
		else:
			print(" ................................................. [FAIL]")
		abort()

	else:
		print("ERROR: X and Y vertices are different sizes")
	a=input()

def filterData(file):
	print("Opening file", end="", flush=True)
	pattern = "(\d{1,10}\.\d{1,10}) ; (\d{1,10}\.\d{1,10}).+;.+.+ (\d{1}\.\d{2}) ; "
	file = open(file)

	with file as f:
		for line in f:
			regex = re.match(pattern, line)
			if regex:
				beginDate.append(regex.group(1))
				endDate.append(regex.group(2))
				seeing.append(regex.group(3))
			else:
				continue

	print(".................................................... [SUCCESS]")
	sizeBeginDate = len(beginDate)
	sizeEndDate   = len(endDate)
	sizeSeeing    = len(seeing)

	dateArraysComp    = sizeBeginDate == sizeEndDate
	dateAndSeeingComp = sizeEndDate == sizeSeeing
	dateAndSeeingNotNull = sizeSeeing > 1

	if dateArraysComp and dateAndSeeingComp and dateAndSeeingNotNull:
		print("Data points captured: [" + str(sizeSeeing) + "]")
		return True
	else:
		return False

def convertJulian(beginDateJDD, endDateJDD):

	if len(beginDateJDD) == len(endDateJDD):
		for i in range(len(endDateJDD)):
			julianDate.append(float(beginDateJDD[i])+(float(endDateJDD[i])-float(beginDateJDD[i]))/2.0)
			y_vertice.append(julian.jd_to_datetime(julianDate[i]))
		return True
	else:
		return False

def abort():
	print("\nNothing to do.")
	a = input('Press enter to exit....')
	exit()
if __name__ == "__main__":
    main()
