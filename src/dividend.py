from random import uniform

def reinvest(shares, cost, dividend, yld):
	amount = shares * yld
	dividend += amount

	new_shares = (amount+30) / cost

	shares += round(new_shares,6)

	return shares, dividend

def main():
	cost 	 = 7.70 + uniform(-1,1)
	shares 	 = 38.108918
	print("initial value: ", shares * cost)
	
	yld 	 = .085
	dividend = 0

	for mnth in range(0,50):
		shares, dividend = reinvest(shares, cost, dividend, yld)
		cost += uniform(-.5,.5)

	print("shares: ", shares)
	print("dividend", dividend)
	print("value", shares*cost)


main()