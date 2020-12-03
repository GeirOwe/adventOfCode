# advent of code by geir owe
# day1 

#variables needed
firstExpense = 0
secondExpense = 0
thirdExpense = 0

expense_total = 2020 #the sum that the expenses are to sum up to
expenses_found = False

#the puzzle input, the expense report - test
expense_report = [1721, 979, 366, 299, 675, 1456]

expense_report = [1688, 1463, 1461, 1842, 1441, 1838, 1583, 1891, 1876, 1551, 1506, 2005, 1989, 1417, 1784, 
1975, 1428, 1485, 1597, 1871, 105, 788, 1971, 1892, 1854, 1466, 1584, 1565, 1400, 1640, 1780, 1774, 360, 1421, 
1368, 1771, 1666, 1707, 1627, 1449, 1677, 1504, 1721, 1994, 1959, 1862, 1768, 1986, 1904, 1382, 1969, 1852, 1917, 
1966, 1742, 1371, 1405, 1995, 1906, 1694, 1735, 1422, 1719, 1978, 1641, 1761, 1567, 1974, 1495, 1973, 1958, 1599, 
1770, 1600, 1465, 1865, 1479, 1687, 1390, 1802, 2008, 645, 1435, 1589, 1949, 1909, 1526, 1667, 1831, 1864, 1713, 1718, 
1232, 1868, 1884, 1825, 1999, 1590, 1759, 1391, 1757, 323, 1612, 1637, 1727, 1783, 1643, 1442, 1452, 675, 1812, 1604, 
1518, 1894, 1933, 1801, 1914, 912, 1576, 1961, 1970, 1446, 1985, 1988, 1563, 1826, 1409, 1503, 1539, 1832, 1698, 1990, 
1689, 1532, 765, 1546, 1384, 1519, 1615, 1556, 1754, 1983, 1394, 1763, 1823, 1788, 1407, 1946, 1751, 1837, 1680, 1929, 
1814, 1948, 1919, 1953, 55, 1731, 1516, 1895, 1795, 1890, 1881, 1799, 1536, 1396, 1942, 1798, 1767, 1745, 1883, 2004, 
1550, 1916, 1650, 1749, 1991, 1789, 1740, 1490, 1873, 1003, 1699, 1669, 1781, 2000, 1728, 1877, 1733, 1588, 1168, 1828, 1848, 
1963, 1928, 1920, 1493, 1968, 1564, 1572]

#some variables to be used while looping
#firstExpenseitem contains the position in the expense report for my first number
#secondExpenseitem starts one position after the firstExpenseItem and loops to the end
#thirdExpenseitem starts one position after the secondExpenseItem and loops to the end
noOfexpenses = len(expense_report)
firstExpenseItem = 0 
secondExpenseItem = 0
thirdExpenseItem = 0

#loop over all remaining items in the expense reports
for exp1 in expense_report:
    if expenses_found == False:
        secondExpenseItem = firstExpenseItem
    
    #loop thru all the remaining expenses, that is listed after this expense
    while secondExpenseItem < (noOfexpenses-1):
        #go to the next item in the list looking for second item
        secondExpenseItem = secondExpenseItem + 1
        thirdExpenseItem = secondExpenseItem + 1
        exp2 = expense_report[secondExpenseItem]
        
        while thirdExpenseItem < (noOfexpenses):
            #I'm just expecting one match, if the match is fund we stop
            if expenses_found == False:
                exp3 = expense_report[thirdExpenseItem]
                if exp1 + exp2 + exp3 == expense_total:
                    expenses_found = True
                    firstExpense = exp1 #store the first expense
                    secondExpense = exp2 # store the second expense
                    thirdExpense = exp3 # store the third expense
                    secondExpenseItem = noOfexpenses #stop looking if the match is found
                    thirdExpenseItem = noOfexpenses #stop looking if the match is found
                else:
                    #go to the next item in the list looking for third item
                    thirdExpenseItem = thirdExpenseItem + 1
    
    #move to the next expense item in the list
    firstExpenseItem = firstExpenseItem + 1
        
#print results
print('----------------------------------------------------')
print('')
if expenses_found:
    print('first expense: ', firstExpense)
    print('second expense:', secondExpense)
    print('third expense:', thirdExpense)
    print('expenses summarized: ', firstExpense + secondExpense + thirdExpense)
    print('expenses multiplied:', firstExpense * secondExpense * thirdExpense)
else:
    print('check your expenses - some items are missing')

print('number of expenses processed: ', noOfexpenses)
print('')
print('------------------End of print ---------------------')
