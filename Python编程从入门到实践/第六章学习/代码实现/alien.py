#aliens.py

alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned "+str(new_points)+" points!")

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_1 = {}

alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

alien_0 = {'color':'green'}
print('The alien is '+alien_0['color']+".")

alien_0['color'] = 'red'
print("The alien is "+alien_0['color']+".")


alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print('Original x-position: '+str(alien_0['x_position']))

#向右移动外星人
#据外星人当前速度决定将其移动多远

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else :
    x_increment = 3

#新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position']+x_increment

print('New x-position:'+str(alien_0['x_position']))


alien_0 = {'color':'green','points':5}
print(alien_0)

del alien_0['points']
print(alien_0)


#p93
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)





#p94
#创建一个用于存储外星人的空列表
aliens = []

#创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

#显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print('...')

#显示创造了多少个外星人
print("Total number of aliens:"+str(len(aliens)))






#p94

#创建一个用于存储外星人空列表
alien = []

#创建30个；绿色的外星人
for alien_number in range(0,30):
    new_alien = {'color1':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10

#显示前五个外星人
for alien in aliens[0:5]:
    print(alien)
print('...')














