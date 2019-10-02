
#		For Stand alone photovoltaic System
#
# Returns calculation of total needed energy for given power output in standalone photovoltic system
# variables :
# AvgPowerOutput : Average Power output required for System (for example : 1 kw = 1000 w)
#				   Important : w unit
# DurOfOp : Duration of operation Needed to operate solar system or solar system to be use(like 24h)
#				 	Important : hour unit
# AvgTimeOfSun : Average time of sunlight avaiable ( for exmaple : 8 hour)
#					Important : hour unit
# NumOfSunlessDay : Number of sunless day (for exmaple : 2 days in week)
#					Important : day per week unit
# BatVolt : Battery Bank Voltage (for example : 108V)
#					Important : Valt unit
#
#
# 					Important Thing 
#
#	Not calculated power dissipation of diode
#	Array tilt is fixed
#	electrical efficiency of the circuit of MPPT = 90%
#	charge/discharge cycle efficiency of the battery = 90%
#	wiring and cabling losees = 5%



def energy_calc_for_given_power_output(AvgPowerOutput,DurOfOp,AvgTimeOfSun,NumOfSunlessDay,BatVolt):
	calculation = {}
	calculation['energy_need_for_seven_days'] = AvgPowerOutput * DurOfOp * 7
	calculation['energy_given_directly_the_load'] = AvgPowerOutput * AvgTimeOfSun * (7 - NumOfSunlessDay)
	calculation['energy_need_for_storing_into_battery'] = calculation['energy_need_for_seven_days'] - calculation['energy_given_directly_the_load']
	calculation['energy_need_for_storing_into_battery_including_battery_efficeny'] = calculation['energy_need_for_storing_into_battery'] / 0.9
	calculation['Total_energy'] = calculation['energy_need_for_storing_into_battery_including_battery_efficeny'] + calculation['energy_given_directly_the_load']
	# including loss of MPPT and wiring cables by dividing
	calculation['Total_energy_including_losses_and_MPPT'] = calculation['Total_energy'] / (0.9*0.95)
	calculation['Battery_amp'] = calculation['energy_need_for_storing_into_battery_including_battery_efficeny'] / BatVolt
	return calculation


def num_of_pv_modules(total_energy,lat,module_walt,EHFS,sunless_day):
	calculation = {}
	calculation['Tilt_angle'] = 0.9 * lat
	calculation['power_of_array'] = total_energy / ( EHFS *(7- sunless_day ))
	calculation['power_of_array_after_derating'] = calculation['power_of_array'] + (0.2) * calculation['power_of_array']
	calculation['num_of_pv_modules'] = calculation['power_of_array_after_derating'] / module_walt
	return calculation


if __name__ == '__main__':
	# answer = energy_calc_for_given_power_output(AvgPowerOutput=1000,DurOfOp=24,AvgTimeOfSun=8,NumOfSunlessDay=2,BatVolt=108)
	# print (answer['energy_need_for_storing_into_battery_including_battery_efficeny'])
	# print (answer['Total_energy'])
	# print (answer['Battery_amp'])
	answer = num_of_pv_modules(215918,28.58,150,5.84,2)
	print (answer['num_of_pv_modules'])
