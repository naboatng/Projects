import numpy as np

dates = np.array([['2023-01-01','2023-01-02','2023-01-03','2023-01-04','2023-01-05','2023-01-30']])
bitcoin = np.array([[48000.00,49000.00,49500.00,51000.00,52000.00,58000.00]])
ethereum = np.array([[3800.00,3900.00,4000.00,4200.00,4300.00,4900.00]])
litecoin = np.array([[150.00,160.00,155.00,165.00,170.00,180.00]])

daily_return_bitcoin = (bitcoin[:,1:] - bitcoin[:,-1])/bitcoin[:,:-1]*100
daily_return_ethereum = (ethereum[:,1:] - ethereum[:,:-1])/ethereum[:,:-1]*100
daily_return_litecoin = (litecoin[:,1:] - litecoin[:,:-1])/litecoin[:,:-1]*100


maximum_return_bitcoin = np.max(daily_return_bitcoin)
maximum_return_ethereum = np.max(daily_return_ethereum)
maximum_return_litecoin = np.max(daily_return_litecoin)

mean_return_bitcoin = np.mean(daily_return_bitcoin)
mean_return_ethereum = np.mean(daily_return_ethereum)
mean_return_litecoin = np.mean(daily_return_litecoin)

minumum_returns_bitcoin = np.min(daily_return_bitcoin)
minumum_returns_ethereum = np.min(daily_return_ethereum)
minumum_returns_litecoin = np.min(daily_return_litecoin)

standard_dev_bitcoin = np.std(daily_return_bitcoin)
standard_dev_ethereum = np.std(daily_return_ethereum)
standard_dev_litecoin = np.std(daily_return_litecoin)


total_return_bitcoin = np.sum(daily_return_bitcoin)
total_return_ethereum = np.sum(daily_return_ethereum)
total_return_litecoin = np.sum(daily_return_litecoin)

column_sums_bitcoin = np.sum(bitcoin)
column_sums_ethereum = np.sum(ethereum)
column_sums_litecoin = np.sum(litecoin)

print("Dates:",dates)
print("\nBitcoin Prices:",bitcoin)
print("\nEthereum Prices:",ethereum)
print("\nLitecoin Prices:",litecoin)


print("\nDaily Returns for Bitcoin(%):",daily_return_bitcoin)
print("\nDaily Returns for Ethereum(%):",daily_return_ethereum)
print("\nDaily Returns for Litecoin(%):",daily_return_litecoin)

print("\nMax Returns for Bitcoin (%):",maximum_return_bitcoin)
print("\nMax Returns for Ethereum (%):",maximum_return_ethereum)
print("\nMax Returns for Litecoin (%):",maximum_return_litecoin)

print("\nMinimum Returns for Bitcoin(%):",minumum_returns_bitcoin)
print("\nMinimum Returns for Ethereum(%):",minumum_returns_ethereum)
print("\nMinimum Returns for Litecoin(%):",minumum_returns_litecoin)

print("\nStandard Deviation Return for Bitcoin (%):",standard_dev_bitcoin)
print("\nStandard Deviation Return for Ethereum(%):",standard_dev_ethereum)
print("\nStandard Deviation Return for Litecoin (%):",standard_dev_litecoin)

print("\nTotal Returns for Bitcoin (%):", total_return_bitcoin)
print("\nTotal Returns for Ethereum (%):", total_return_ethereum)
print("\nTotal Returns for Litecoin (%):", total_return_litecoin)



#Summary of the project
# I compute statics for each crypto price. Calculated the mean,max,minimum
# and standard deviation return and I find the sum of each crypto using the axis=0
# NumPy built in function  . I calculated the daily return for  todays price
# subtracted from yesterday price and divided by yesterday price multiply 100
#