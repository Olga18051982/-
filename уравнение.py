import math
print("Введите коэффициенты для квадратного уравнения a^2+bx+c=0")
a=float(input('a= '))
b=float(input('b= '))
c=float(input('c= '))

discr=b**2-4*a*c
print('Дискриминант D=%.2f'% discr)
if discr>0:
    x1=(-b+math.sqrt(discr))/(2*a)
    x2=(-b-math.sqrt(disct))/(2*a)
    print('x1=%.2f \nx2=%.2f'%(x1, x2))
elif discr==0:
    x1=-b/(2*a)
    print("Корень= ", x1)
elif discr<0:
    print('Корней нет')


