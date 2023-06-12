import math  # needed for pi
pi = math.pi # pi
g  = 9.81    # gravitational constant on Earth

def get_distance(velocity:float, angle:float)-> float:
    d = ((velocity**2)*math.sin(2*angle))/g
    return d 
    
## print(get_distance(10, 0.25*pi)) test case 

def degrees_to_radians(d:float)-> float:
    return d*(pi/180) #formula for converting degree to radians is multiplying the angle in degree by pi/180

## print(degrees_to_radians(180))  test case 

def get_radian_of(angle_string: str)-> float:
    angle = float(angle_string[:-1])
    if angle_string.endswith('r'):
        return angle      
    else:
        return degrees_to_radians(angle)
        
## print(get_radian_of("45d"))  test case 

def is_a_number(s:str)-> bool:
    try :
        number = float(s) #the try statement tries to convert the string to float and the except statement provides code for when the string cannot be converted
        if s[0] == "-":
            return False 
        elif number>0:
            return True
        else:
            return False
    except ValueError:
        return False
    
## print(is_a_number("3.1.2"))  test case 

def is_valid_angle(s:str)-> bool:
    try:
        angle = float(s[:-1])
        if (s[-1] == "d" or s[-1] == "D") and 0<angle<90:
            return True 
        elif (s[-1] == "r" or s[-1] == "R") and 0<angle<pi/2:
            return True 
        else:
            return False 
    except ValueError:
        return False
        
## print(is_valid_angle("0.001r"))  test case 

def approx_equal(x, y, tol):
    if abs(x-y) <= tol:
        return True 
    else:
        return False 
    
## print(approx_equal(4,3,0.99))  test case 

## Testing the game.
if __name__ == "__main__":
    while True:
        target = float(input("Enter a target distance: "))
        tol = float(input("Enter how close you need to be to your target: "))
        target_hit = False
        while not target_hit:
            valid_velocity = False
            while not valid_velocity:
                v = input("Enter a valid velocity: ")
                valid_velocity = is_a_number(v)   
            valid_angle = False
            v = float(v)
            while not valid_angle:
                theta = input("Enter a valid angle: ")
                valid_angle = is_valid_angle(theta)
            theta = get_radian_of(theta)
            d = get_distance(float(v), theta)
            target_hit = approx_equal(target, d, tol)
            if target_hit:
                print("Congratulations! You hit the target.")
            elif target > d:
                print("The shot hit short of the target, try again.")
            else: 
                print("The shot hit past the target, try again.")