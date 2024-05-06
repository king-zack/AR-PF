import math
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mean
import sys
import csv

def calcReal(ApparentPower, Factor):
	'''A simple function that calculates the real power kW given the apparent power (KVA) and the power factor'''
	return ApparentPower * Factor

def calcReactive(Apparent, Real):
	'''a function that calculates the reactive power kVAR from the apparent and real power'''
	return math.sqrt(Apparent**2 - Real**2)
	
def calcApparent(Real, powerFactor):
	'''A function that calculates the apparent power kVA from the apparent and real power'''
	return Real / powerFactor

def findCorrection(increment, Real, Reactive, Apparent, minPowFac=0, avgPowFac=0, correction=0):
	'''A function that increments KVA based on a corrective measure, with this new KVA value, the minimum power factor, the average power factor, and the correction value are returned'''
	correctionArray = []
	minPowFacArray = []
	avgPowFacArray = []
	while minPowFac < 0.93 or avgPowFac < 0.95:
		newReactive = []
		newApparent = []
		newPowerFactor = []
		correction = correction + increment
		for i in range(len(Real)):
			newReactive.append(Reactive[i] - correction)
		for j in range(len(Real)):
			newApparent.append(math.sqrt(newReactive[j]**2 + Real[j]**2))
		for k in range(len(Real)):
			newPowerFactor.append(Real[k] / newApparent[k])
		minPowFac = min(newPowerFactor)
		avgPowFac = mean(newPowerFactor)
		
		correctionArray.append(correction)
		minPowFacArray.append(minPowFac)
		avgPowFacArray.append(avgPowFac)
		
		data = {
			'Minimum Power Factor': minPowFacArray,
			'Average Power Factor': avgPowFacArray
		}
			
	return pd.DataFrame(data, index = correctionArray)
	
def findCost(data, rate):
	installationCost = 1600
	unitCost = 16214
	costperKVARCorrection = 71.33
	costperKVARBill = rate
	correction = list(data.index)
	payback = []
	savings = []
	payment = []
	for i in correction:
		cost = unitCost + installationCost + costperKVARCorrection*i
		saved = (mean(ApparentPower) - (mean(realPower) / data.loc[i, 'Average Power Factor'])) * costperKVARBill*12
		savings.append(saved)
		payment.append(cost)
		payback.append((cost / saved))
	data.insert(2, 'Cost of Correction', payment, True)
	data.insert(3, 'Savings', savings, True)
	data.insert(4, 'Payback Period', payback, True)
	return data

#import data as CSV	
powerData = pd.read_csv('PowerData.csv', index_col=0)

#Power Factor, Given by Bill
powerFactor = list(powerData.loc[:,'Power Factor'])
print(powerFactor)

#Real power, also given by bill
realPower = list(powerData.loc[:, 'Real Power'])
#plt.plot(powerFactor)
#plt.show()

#Using the power factor, find the real power and reactive power
ApparentPower = []
for i in range(len(powerFactor)):
	ApparentPower.append(calcApparent(realPower[i], powerFactor[i]))

reactivePower = []
for i in range(len(ApparentPower)):
	reactivePower.append(calcReactive(ApparentPower[i], realPower[i]))
	
print(powerData)
input("Press ENTER to confirm the data shown above")
powerFactorData = findCorrection(25, realPower, reactivePower, ApparentPower)
data = findCost(powerFactorData, float(input("Please enter the cost per KVA in USD: $")))
output_csv_data = data.to_csv('PFSavings.csv', index = True)
print('\nCSV String:\n', output_csv_data)

#plt.plot(data.index.values, data['Minimum Power Factor'].values, label = 'Minimum Power Factor')
#plt.plot(data.index.values, data['Average Power Factor'].values, label = 'Average Power Factor')
#plt.legend()
#plt.xlabel('Correction (kVAR)')
#plt.ylabel('Minimum Power Factor')
#plt.grid()
#plt.show()

#plt.plot(data.index.values, data['Payback Period'].values)
#plt.xlabel('Correction (kVAR)')
#plt.ylabel('Payback Period (Years)')
#plt.grid()
#plt.show()







