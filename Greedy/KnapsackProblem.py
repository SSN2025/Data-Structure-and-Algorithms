import numpy as np
def greedyKnapsack(value,weight,capacity):
            temp = np.column_stack((value,weight))
            temp = temp.tolist()
            temp.sort(key = lambda x: (x[0]/x[1]),reverse = True)
            pr =0
            i=0
            for i in range(len(value)):
                    if(capacity > 0 and temp[i][1]<capacity):
                            print(f"{temp[i][1]} of {temp[i][0]}")
                            capacity -= temp[i][1]
                            pr += temp[i][0]
                    else: break
            if(capacity>0):
                     pr += temp[i][0] * (capacity/temp[i][1])
                     print(f"{capacity/temp[i][1]} of {temp[i][0]}")
            return pr



a = np.array([25,24,15],dtype = float)
b = np.array([18,15,10],dtype = float)

print(f"Maximised value: {greedyKnapsack(a,b,20.0)}")

    