import math
elevator_L=1.58
elevator_D=1.48
elevator_H=2.58

elevator_door_w=0.9
elevator_door_h=2.1

target_door_l=2.45#2.45
target_door_d=1.15#1.15

def consider_elevator_height(L,D,H,w,h,l):
    project_l=math.sqrt(((L - w) / 2 + w) ** 2 + D ** 2)
    if project_l>l:
        return H #此时电梯门的高度就是极限，相当于门的底部是完全放进里面，就看上门
    else:
        x=math.acos(project_l/l)
        d1_fenzi=H-l*math.sin(x)
        d1_fenmu=math.cos(math.acos(math.sqrt(((L-w)/2+w)**2+D**2)/l))
        d1=d1_fenzi/d1_fenmu
        print('d1:', d1)
        return d1

def consider_elevator_door_height(L,D,H,w,h,l):
    project_l=math.sqrt(((L - w) / 2 + w) ** 2 + D ** 2)
    if project_l>l:
        return h #此时电梯门的高度就是极限，相当于门的底部是完全放进里面，就看电梯门高度
    else:
        x = math.acos(project_l / l)
        d2=h*math.cos(x)
        print('d2:',d2)
        return d2

target_door_d,target_door_l=min(target_door_d,target_door_l),max(target_door_d,target_door_l)#确保长边用于大于宽度，数学模型上是以长边做l，短边做d
if target_door_d**2+target_door_l**2 < ((elevator_L-elevator_door_w)/2+elevator_door_w)**2+elevator_D**2+elevator_H**2:
    d1 = consider_elevator_height(elevator_L,elevator_D,elevator_H,elevator_door_w,elevator_door_h,target_door_l)
    d2 = consider_elevator_door_height(elevator_L, elevator_D, elevator_H, elevator_door_w, elevator_door_h, target_door_l)

    if target_door_d<=min(d1,d2):
        print('门可以进电梯')
    else:
        print('门无法进电梯')
else:
    print('门斜线超出电梯的斜线，肯定进不去电梯')
