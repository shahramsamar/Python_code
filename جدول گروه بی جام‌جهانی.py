Spain =  {'name':'Spain','wins':0 , 'loses':0 , 'draws':0 ,'gol_za':0,'gol_kh':0, 'goal difference':0 , 'points':0}
Iran = {'name':'Iran','wins':0 , 'loses':0 , 'draws':0 ,'gol_za':0,'gol_kh':0, 'goal difference':0 , 'points':0} 
Portugal = {'name':'Portugal','wins':0 , 'loses':0 , 'draws':0 ,'gol_za':0,'gol_kh':0, 'goal difference':0 , 'points':0}
Morocco  = {'name':'Morocco','wins':0 , 'loses':0 , 'draws':0 , 'gol_za':0,'gol_kh':0,'goal difference':0 , 'points':0}
list2 = []
for i in range(6):
 var =input().split('-')
 list2.append((var))
# list2 =[['2', '2'], ['2', '1'], ['1', '2'], ['2', '2'], ['3', '1'], ['2', '1']]
#1#Spain (2) - Iran (2) [2,2]
###############################################
Iran['gol_za'] += int(list2[0][0]) 
Iran['gol_kh'] += int(list2[0][1]) 
Iran['goal difference'] = (Iran['gol_za']-Iran['gol_kh'])
Spain['gol_za'] += int(list2[0][1])
Spain['gol_kh'] += int(list2[0][0]) 
Spain['goal difference'] = (Spain['gol_za'] -Spain['gol_kh'] )
if  int(list2[0][0]) == int(list2[0][1])  :
 Iran['draws'] ,Spain['draws'] = 1,1
 if Iran['draws'] != 0 and Spain['draws'] != 0 :
   Iran['points'] , Spain['points'] = 1,1
elif int(list2[0][0]) > int(list2[0][1]) :
  Iran['wins'] ,Spain['loses'] = 1,1
  if Iran['wins'] != 0 or Spain['loses'] != 0 :
     Iran['points'] , Spain['points'] = 3,0
elif int(list2[0][0]) < int(list2[0][1]) :
 Iran['loses'] ,Spain['wins'] = 1,1
 if Iran['loses'] != 0 and Spain['wins'] != 0 :
   Iran['points'] , Spain['points'] = 0,3
#2#Portugal (1) - Iran (2) [2,1]
###############################################
Iran['gol_za'] += int(list2[1][0])
Iran['gol_kh'] += int(list2[1][1])
Iran['goal difference'] = (Iran['gol_za']-Iran['gol_kh']) 
Portugal['gol_za'] += int(list2[1][1])
Portugal['gol_kh'] += int(list2[1][0])
Portugal['goal difference'] = (Portugal['gol_za']-Portugal['gol_kh'])
if  int(list2[1][0]) == int(list2[1][1]) :
 Iran['draws'] +=1
 Portugal['draws'] +=1
 if Iran['draws']!= 0 and Portugal['draws']!= 0 :
    Iran['points'] += 1 
    Portugal['points'] += 1
elif int(list2[1][0]) > int(list2[1][1]) :
  Iran['wins'] += 1
  Portugal['loses'] += 1
  if Iran['wins'] != 0 and Portugal['loses'] != 0 :
    Iran['points'] += 3 
    Portugal['points'] += 0
elif int(list2[1][0]) < int(list2[1][1]) :
 Iran['loses'] += 1
 Portugal['wins'] += 1
 if Iran['loses'] != 0 and Portugal['wins'] != 0 :
    Iran['points'] += 0
    Portugal['points'] += 3
#3#Morocco (2) - Iran (1) [1,2]
###############################################
Iran['gol_za'] += int(list2[2][0])
Iran['gol_kh'] += int(list2[2][1])
Iran['goal difference'] = (Iran['gol_za']-Iran['gol_kh'])
Morocco['gol_za'] += int(list2[2][1])
Morocco['gol_kh'] += int(list2[2][0])
Morocco['goal difference'] = (Morocco['gol_za'] -Morocco['gol_kh'] )
if  int(list2[2][0]) == int(list2[2][1]) :
 Iran['draws'] += 1
 Morocco['draws'] += 1
 if Iran['draws'] != 0 and Morocco['draws'] != 0:
    Iran['points'] += 1
    Morocco['points'] += 1
elif int(list2[2][0]) > int(list2[2][1]) :
  Iran['wins'] += 1
  Morocco['loses'] += 1
  if Iran['wins'] != 0 and Morocco['loses'] != 0:
    Iran['points'] += 3
    Morocco['points'] += 0
elif int(list2[2][0]) < int(list2[2][1]) :
 Iran['loses'] += 1
 Morocco['wins'] += 1
 if Iran['loses'] != 0 and Morocco['wins'] != 0:
    Iran['points'] += 0
    Morocco['points'] += 3
#4#Portugal (2) - Spain (2) [2,2]
###############################################
Spain['gol_za'] += int(list2[3][0])
Spain['gol_kh'] += int(list2[3][1])
Spain['goal difference']  = (Spain['gol_za'] -Spain['gol_kh'] )
Portugal['gol_za'] += int(list2[3][1])
Portugal['gol_kh'] += int(list2[3][0])
Portugal['goal difference'] = (Portugal['gol_za'] -Portugal['gol_kh'])
if  int(list2[3][0]) == int(list2[3][1]) :
 Spain['draws'] += 1
 Portugal['draws'] += 1
 if Spain['draws'] != 0 and Portugal['draws'] != 0:
    Spain['points'] += 1
    Portugal['points'] += 1
elif int(list2[3][0]) > int(list2[3][1]) :
  Spain['wins'] += 1
  Portugal['loses'] += 1
  if Spain['wins'] != 0 and Portugal['loses'] != 0:
    Spain['points'] += 3
    Portugal['points'] += 0
elif int(list2[3][0]) < int(list2[3][1]) :
  Spain['loses']  += 1
  Portugal['wins'] += 1
  if Spain['loses'] != 0 and Portugal['wins'] != 0:
    Spain['points'] += 0
    Portugal['points'] += 3
#5#Morocco (1) - Spain (3) [3,1]
###############################################
Spain['gol_za'] += int(list2[4][0])
Spain['gol_kh'] += int(list2[4][1])
Spain['goal difference'] = (Spain['gol_za']-Spain['gol_kh'] )
Morocco['gol_za'] += int(list2[4][1])
Morocco['gol_kh'] += int(list2[4][0])
Morocco['goal difference'] = (Morocco['gol_za']-Morocco['gol_kh'])
if  int(list2[4][0]) == int(list2[4][1]) :
 Spain['draws'] += 1 
 Morocco['draws'] += 1
 if Spain['draws'] != 0 and  Morocco['draws'] != 0:
    Spain['points'] += 1
    Morocco['points'] += 1
elif int(list2[4][0]) > int(list2[4][1]) :
  Spain['wins'] += 1
  Morocco['loses'] += 1
  if Spain['wins'] != 0 and  Morocco['loses'] != 0:
    Spain['points'] += 3
    Morocco['points'] += 0 
elif int(list2[4][0]) < int(list2[4][1]) :
 Spain['loses'] += 1
 Morocco['wins'] += 1
 if Spain['loses'] != 0 and  Morocco['wins'] != 0:
    Spain['points'] += 0
    Morocco['points'] += 3
#6#Morocco (2) - Portugal (1) [2,1]
###############################################
Portugal['gol_za'] += int(list2[5][0])
Portugal['gol_kh'] += int(list2[5][1])
Portugal['goal difference'] = (Portugal['gol_za']-Portugal['gol_kh'])
Morocco['gol_za'] += int(list2[5][1])
Morocco['gol_kh'] += int(list2[5][0])
Morocco['goal difference'] = (Morocco['gol_za']-Morocco['gol_kh'])
if  int(list2[5][0]) == int(list2[5][1]) :
 Portugal['draws'] += 1
 Morocco['draws'] += 1
 if Portugal['draws'] != 0 and  Morocco['draws'] != 0:
    Portugal['points'] += 1
    Morocco['points'] += 1
elif int(list2[5][0]) > int(list2[5][1]) :
  Portugal['wins'] += 1
  Morocco['loses'] += 1
  if Portugal['wins'] != 0 and  Morocco['loses'] != 0:
    Portugal['points'] += 3
    Morocco['points'] += 0
elif int(list2[5][0]) < int(list2[5][1]) :
 Portugal['loses'] += 1
 Morocco['wins'] += 1
 if Portugal['loses'] != 0 and  Morocco['wins'] != 0:
    Portugal['points'] += 0
    Morocco['points'] += 3
# print(Iran,'\n')
# print(Spain,'\n')
# print(Portugal,'\n')
# print(Morocco,'\n')
finall = {"Iran": Iran, "Morocco":Morocco , "Portugal": Portugal, "Spain":Spain}
# print(finall)
sorted_teams = sorted(finall.items(), key=lambda x: (-x[1].get('points'), -x[1].get('wins'),x[1].get('name'))) 
# print(sorted_teams)
for index in sorted_teams:
  # print(index[1]["name"],"",'wins:',index[1]["wins"],",",'loses:',index[1]["loses"],",",'draws:',index[1]["draws"],",",'goal difference:',index[1]["goal difference"],",",'points:',index[1]["points"])
    print("%s  wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i" %(index[1]["name"],index[1]["wins"],index[1]["loses"],index[1]["draws"],index[1]["goal difference"],index[1]["points"]))