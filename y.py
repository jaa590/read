
class calculation:

	
	def BMIcalculator(self, Height, Mass):
		
	
		BMI = (Mass)/(Height*Height)
		
	
		for t1, t2 in [(16, 'severely underweight'),
					(18.5, 'underweight'),
					(25, 'normal'), (30, 'overweight'),
					(35, 'moderately obese'),
					(float('inf'), 'severely obese')]:
		
			if BMI <= t1:
				put_text('Your BMI is', BMI, 'and the person is :', t2)
				break
