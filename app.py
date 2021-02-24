from flask import Flask,render_template
import requests
import datetime
import json
import pygal
from pygal.style import Style
app = Flask(__name__)

@app.route('/')
def main():
	now = datetime.datetime.now()
	year = now.year
	myUrl = 'https://api.covid19api.com/summary'
	response = requests.get(myUrl)
	r = json.loads(response.text)
	updateDate = r['Countries'][164]['Date']
	dataDate = str(updateDate).split('T')[0]
	totalGlobal = r['Global']['TotalConfirmed']
	Swaziland = r['Countries'][164]['TotalConfirmed']

	deathsGlobal = r['Global']['TotalDeaths']
	deathsSwaziland = r['Countries'][164]['TotalDeaths']

	recoveriesGlobal = r['Global']['TotalRecovered']
	recoveriesSwaziland = r['Countries'][164]['TotalRecovered']


	return render_template('index.html',
	 deathsGlobal = deathsGlobal,
	 dataDate = dataDate,
	 deathsSwaziland = deathsSwaziland,  
	 recoveriesSwaziland = recoveriesSwaziland,
	 recoveriesGlobal = recoveriesGlobal, 
	 totalGlobal = totalGlobal, 
	 Swaziland = Swaziland ,
	 year = year)

@app.route('/globalGraph.svg')
def makeGlobalGraph():
	myUrl = 'https://api.covid19api.com/summary'
	response = requests.get(myUrl)
	r = json.loads(response.text)
	totalGlobal = r['Global']['TotalConfirmed']
	Swaziland = r['Countries'][164]['TotalConfirmed']

	deathsGlobal = r['Global']['TotalDeaths']
	deathsSwaziland = r['Countries'][164]['TotalDeaths']

	recoveriesGlobal = r['Global']['TotalRecovered']
	recoveriesSwaziland = r['Countries'][164]['TotalRecovered']
	blue = Style(colors=('blue'))
	line_chart = pygal.Bar(style=blue)
	line_chart.title = 'Global Covid 19 stats'
	line_chart.x_labels = ['Cases','Recoveries','Deaths']
	line_chart.add('Global',[totalGlobal,recoveriesGlobal,deathsGlobal])
	
	return line_chart.render_response()

@app.route('/eswatiniGraph.svg')
def makeeSwatiniGraph():
	myUrl = 'https://api.covid19api.com/summary'
	response = requests.get(myUrl)
	r = json.loads(response.text)
	totalGlobal = r['Global']['TotalConfirmed']
	Swaziland = r['Countries'][164]['TotalConfirmed']

	deathsGlobal = r['Global']['TotalDeaths']
	deathsSwaziland = r['Countries'][164]['TotalDeaths']

	recoveriesGlobal = r['Global']['TotalRecovered']
	recoveriesSwaziland = r['Countries'][164]['TotalRecovered']
	blue = Style(colors=('blue'))
	line_chart = pygal.Bar(style=blue)
	line_chart.title = 'eSwatini Covid 19 stats'
	line_chart.x_labels = ['Cases','Recoveries','Deaths']
	line_chart.add('eSwatini',[Swaziland,recoveriesSwaziland,deathsSwaziland],color='blue')
	
	return line_chart.render_response()


if __name__ == '__main__':
	app.run()