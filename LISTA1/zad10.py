from cmath import sin,cos
z = complex(0,1)
sin_z = sin(z)
cos_z = cos(z)

print('Część rzeczywista z sin(i):',sin_z.real)
print('Część urojona z sin(i):',sin_z.imag)
print('Część rzeczywista z cos(i):', cos_z.real)
print('Część urojona z cos(i):', cos_z.imag)
print('Zależność jest spełniona sin(i)^2+cos(i)^2 = 1: ')
print(sin(z)**2 + cos(z)**2)