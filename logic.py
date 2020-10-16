global GLOBAL_INPUT 
GLOBAL_INPUT =""

global GLOBAL_OUTPUT
GLOBAL_OUTPUT=""



def ReadLastNLines(f,n):
    global GLOBAL_INPUT
    with open(f) as infile:
        for x in (infile.readlines()[-n]):
            GLOBAL_INPUT += x
    infile.close()
   # print(GLOBAL_INPUT)
    
    
def WriteOutput():
     outfile = open("v_output.txt",'a')
     outfile.write(GLOBAL_OUTPUT)
     outfile.close()
 
    # MAIN LOGIC START
def prints():
    global GLOBAL_INPUT
    global GLOBAL_OUTPUT
    GLOBAL_INPUT=GLOBAL_INPUT.strip('\n')
    fun = 'print'
    result = GLOBAL_INPUT.find(fun)
    if (result != -1):
        GLOBAL_INPUT=GLOBAL_INPUT[GLOBAL_INPUT.index(fun) + len(fun):]
        GLOBAL_OUTPUT='cout<<"'+GLOBAL_INPUT+'";\n'
    else:
        print ("Sorry say again")
        
def loop():
       global Global_INPUT
       global GLOBAL_OUTPUT
       datatype="int"
       var_name="LOOP_ITR"
       condition="0"
       incrementer="NA"
       internal_loop_value="0"
       final_loop_value="0"
       ip=GLOBAL_INPUT.strip('\n')
       
       ip=ip.replace('run loop from ','')
       check=ip.split(' ')[0]
       if (check=='variable'):
            ip=ip.replace('variable ','')
            var_name=ip.split(' ')[0]
            ip=ip.replace(var_name +' value ','',1)
            internal_loop_value=ip.split(' ')[0]
            ip=ip.replace(internal_loop_value +' to ','')
            final_loop_value=ip.split(' ')[0]
            if(internal_loop_value.isnumeric()):
                internal_loop_value=int(internal_loop_value)
            if(final_loop_value.isnumeric()):
                final_loop_value=int(final_loop_value)
            ip=ip.replace(final_loop_value+' ','')
            print(ip)
            incrementer=ip.split(' ')[0]
            print(ip)
            ip=ip.replace(incrementer+' ','')
            
            con=ip.split(' ')[0]
            if(con=='where'):
                ip=ip.replace(con+' ','')
                condition=ip  
            else:
                print("where not found")
                print(internal_loop_value+"#######"+final_loop_value)
                if(internal_loop_value < final_loop_value):
                    condition=internal_loop_value +" < "+ final_loop_value
                    print(incrementer) 
                    if(incrementer==""):
                        incrementer=internal_loop_value +"++"
                else:
                    condition=internal_loop_value+" >= "+final_loop_value
                    if(incrementer==""):
                        incrementer=internal_loop_value +"--"
       else:
            print("variable not found logic")
           
           
#######################LOOP PARSE C++########################
       if(internal_loop_value.isnumeric() == False):
           datatype="string"
       print(incrementer)   
       temp_op="for( "+ datatype +" "+ var_name +" = "+ internal_loop_value +" ; "+ condition +" ; " + incrementer + " )\n{"
       print(temp_op)
        
        
    
    
    
    
    
    
    
    

    
 ####################################### MAIN PROGRAM FLOW START####################################
try: 
    ReadLastNLines("v_input.txt", 1)
   # prints()
    #route()
    #loop()
    WriteOutput()
    
except:
    print('ERROR x00000001 \nv_input.txt IS EMPTY.')            
