from random import choice


def zar1():
        return choice(range(1, 7))

def zar2():
        return choice(range(1, 7))

try_list=[100,1000,10000]
sumumation_dictionary={2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
for numbers in try_list:
        
        for times_for_roll in range(numbers):
            sum=0
            sum=zar1()+zar2()
            
            value=sumumation_dictionary[sum]
            new_value=value+1
            sumumation_dictionary[sum]=new_value
        print(sumumation_dictionary)   
        print(f"for {numbers} time")         
        r_min=1
        r_max=13
        t_max=0
        t_min=1000000000
        for keys in sumumation_dictionary:
               if sumumation_dictionary[keys]>t_max:
                t_max=sumumation_dictionary[keys]
        
        for keys in sumumation_dictionary:
              if sumumation_dictionary[keys]<t_min:
                t_min=sumumation_dictionary[keys]
        
        for keys in sumumation_dictionary:
              m=sumumation_dictionary[keys]
              star=1+((m-t_min)*(13))/(t_max-t_min)
              print(keys," *" * int(star),"\n")