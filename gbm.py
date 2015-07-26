#Setup parameters
mu=0.1;
sigma=0.26;
S0=39;
n_path=1000;
n=n_partitions=1000;
period=3;

#theorectical expectation and variance
T_E = S0 * p.exp(mu*period)
T_Var = (S0**2)*(np.exp(2*mu*period))*(np.exp(sigma*sigma*period)-1)
print('Theorectical Expectation = ' + str(T_E) )
print('Theorectical Variance = ' + str(T_Var))

#Create Brownian paths
t=p.linspace(0,period,n+1);
dB=p.randn(n_path,n+1)/p.sqrt(n/period);
dB[:,0]=0;
B=dB.cumsum(axis=1);

#Calculate stock prices
nu=mu-sigma*sigma/2.0
S=p.zeros_like(B);
S[:,0]=S0
S[:,1:]=S0*p.exp(nu*t[1:]+sigma*B[:,1:])

#Plotting only 5 realizations of the GBM
S_plot=S[0:5]
label = 'Time , $t$' ; p.xlabel(label)
label = 'Stock prices, $S$' ; p.ylabel(label)
para1 = '\n with $\mu$ = ' + str(mu)
para2 = 'and $\sigma$ = ' + str(sigma) + '\n'
p.title('5 simulated run of Stock Prices' + para1 + para2)
p.plot(t,S_plot.transpose());
p.show();

#Calculate the expectation value of S(3) based on the simulation
S3=np.array(S[:,-1])
E_S3=np.mean(S3)
print('E(S3) = ' + str(E_S3))

#Calculate the variance of S(3)
Var_S3=np.var(S3)
print('Var(S3) = ' + str(Var_S3))

#Calculate P[S(3)> 39]
mask = S3 > 39
non_zero=mask*S3
num1=np.count_nonzero(non_zero)
den1=len(mask)
P_S3_more_than_39 = num1/den1
print('P(S3 > 39) = ' + str(P_S3_more_than_39))

#Calculate E[S(3) | S(3) > 39]
mask2 = S3 > 39                  #number of values more than 39 
S3_more_than_39 = S3 * mask    #extracting values more than 39
num2 = sum(S3_more_than_39)
den2 = sum(mask2)+0.0
E_S3_more_than_39 = num2/den2
print('E(S3 | S3 > 39) = ' + str(E_S3_more_than_39))
