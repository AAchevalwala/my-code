from tkinter import *
from tkinter import messagebox
import math

root=Tk()
root.title('Simple Calculator')
root.iconbitmap(r'C:\Users\Ahsan.AHSAN-PC\AppData\Local\Programs\Python\Python38-32\calc.ico')
textFieldWidth = 50
bWidth=10
bHeight=2
result=None
operand1=None
operand2=None
operator=None
memory=None

#helper function performs calculations
def perform_calc():
    global operand1,operand2,operator, result

    if operator =='+':
        result=operand1+operand2
    elif operator =='-':
        result =operand1 - operand2
    elif operator ==r'/':
        result =operand1 / operand2
    elif operator =='*':
        result =operand1 * operand2
    elif operator == '**':
        result= math.pow(operand1, operand2)

# helper function generates error 
def gen_error(e):
    global operand1,operand2,operator, result
    textField.delete(0,END)
    savedValue.delete(0,END)
    messagebox.showerror('Error', e)
    operand1=None
    operand2=None
    operator='='

#executes on  del click
def del_click():
    textField.delete(0,END)

#executes on backspaeclick
def backspace_click():
    current=textField.get()
    textField.delete(0,END)
    textField.insert(0,current[0:-1])
    

#executes when a number key is pressed(0-9 and .)
def number_click(value):
    global operand1,operand2,operator, result
    num=tuple(('0','1','2','3','4','5','6','7','8','9','.'))

    if value in num: 
        current=str(textField.get())
        textField.delete(0,END)

        if(operator == '='): 
            operator=None
            operand1=None
            operand2=None
            savedValue.delete(0,END)

            if(value =='.'):
                textField.insert(0, '0' + value)
            else:
                textField.insert(0, value)
        else:

            if(value =='.' and current ==''):
                textField.insert(0, '0' + value)
            else:
                textField.insert(0,current+ value)

# executes when an operator key is pressed (+,-,pow,*,/)
def operator_click(value):
    global operand1,operand2,operator, result
    op=tuple(('+','-','*',r'/','**'))

    if operand1 == None and operator ==None and len(textField.get())> 0:

        try:
            savedValue.delete(0,END)
            savedValue.insert(0,str(textField.get())+ value)
            operand1=float(textField.get())
            operator=value
            textField.delete(0,END)
        except ValueError as v:
            gen_error(v)
            return
            
    elif(operand2 ==None and operator =='=' and operand1 == None):
        operator = None
        savedValue.delete(0,END)
                
    elif operand2 ==None and operator =='=':
        operator = value
        savedValue.delete(0,END)
        savedValue.insert(0,str(operand1)+ value)
        textField.delete(0,END)
            
    elif (operator in op and operand1 is not None and len(textField.get())> 0 ):

        try:
            operand2= float(textField.get())
            textField.delete(0,END)
            perform_calc()
            savedValue.delete(0,END)
            savedValue.insert(0,str(result)+value)
            operator = value
            operand1=result
            operand2=None
        except ValueError as v:
            gen_error(v)
            return

    elif(operand1 !=None and operand2 ==None and operator !='='):
        operator=value
        savedValue.delete(0,END)
        savedValue.insert(0,str(operand1)+value)

#executes when = is pressed    
def eq_click():
    global operand1,operand2,operator, result
    try:
        if operand1!=None and operator != None and  operator!= '=' and len(textField.get()) > 0:
            operand2=float(textField.get())
            textField.delete(0,END)
            perform_calc()
            savedValue.delete(0,END)
            savedValue.insert(0,str(result))
            operand1=result
            operand2=None
            result=None
            operator='='

        elif(operand1==None and operand2==None and len(textField.get())> 0):
            operand1=float(textField.get())
            operator='='
            textField.delete(0,END)
            savedValue.delete(0,END)
            savedValue.insert(0,str(operand1))

    except ValueError as v:
        gen_error(v)
        return
    except ZeroDivisionError as z:
        gen_error(z)
        return
            
#executes when c is pressed
def c_click():
    global operand1,operand2,operator, result
    textField.delete(0,END)
    savedValue.delete(0,END)
    operand1=None
    operand2=None
    operator=None
    
#Helper for single Operand Calculations
def perform_single_operation(operation,current):
    singleOperators=('Per','Sign','Sqrt','Fact','Log','Ln','Rec','Exp')
    global operand1,operand2,operator, result

    if(operation == singleOperators[0]):
        current = current/100
    elif(operation== singleOperators[1]):
        current = -current
    elif(operation== singleOperators[2]):
        current = math.sqrt(current)
    elif(operation== singleOperators[3]):
        current = math.factorial(current)
    elif(operation== singleOperators[4]):
        current = math.log10(current)
    elif(operation== singleOperators[5]):
        current = math.log(current)
    elif(operation== singleOperators[6]):
        current = 1/current
    elif(operation== singleOperators[7]):
        current = math.exp(current)

    return current
    
#executes for all the single operand operations
def single_operand_calc_click(operation):
    global operand1,operand2,operator, result
    try:
        if (len(textField.get()) !=0 and len(savedValue.get())==0):
            current=float(textField.get())
            current=perform_single_operation(operation,current)
            textField.delete(0,END)
            savedValue.insert(0,str(current))
            operand1 =current   
    
        elif(len(textField.get()) !=0 and len(savedValue.get())!=0 ):
            current=float(textField.get())
            current=perform_single_operation(operation,current)   
            textField.delete(0,END)
            textField.insert(0,str(current))   
     
        elif(len(savedValue.get()) > 0 and len(textField.get()) ==0):
            op=tuple(('+','-','*',r'/','**'))

            if(operator in op):
                strdata=savedValue.get()[0:-len(operator)]
                current=float(strdata)
                strdata=operator
            else:
                current=float(savedValue.get())
                strdata=''

            current=perform_single_operation(operation,current)
            savedValue.delete(0,END)
            savedValue.insert(0,str(current)+ strdata)
            operand1=current

    except ValueError as v:
        gen_error(v)
    except OverflowError as o:
        gen_error(o)

#defines memory function
def mem_control_click(option):
    global memory,operator,operand1,operand2,result
    mem_options=['Mshow','Madd','Msub','Mrem']
    try:
        op=tuple(('+','-','*',r'/','**'))

        if(operator in op):
            strdata=savedValue.get()[0:-len(operator)]
            current=float(strdata)
        elif(operator not in op and len(savedValue.get())> 0):
            current=float(savedValue.get())


        if (option== mem_options[0]):

            if(memory !=None and operator in op):
                textField.delete(0,END)
                textField.insert(0,str(memory))
            elif(operator not in op and memory!= None):
                textField.delete(0,END)
                savedValue.delete(0,END)
                textField.insert(0,str(memory))
                operand1=None
                operand2=None
                operator=None   
            else:
                raise ValueError('Memory does not exist')

        elif(option == mem_options[1]):

            if(memory ==None and len(savedValue.get())>0):
                memory= current
            elif (len(savedValue.get())>0):
                memory=memory + current

        elif(option == mem_options[2]):

            if(memory ==None and len(savedValue.get())>0):
                memory=- current
            elif (len(savedValue.get())>0):
                memory=memory - current

        elif(option == mem_options[3]):
            memory=None

    except ValueError as v:
        gen_error(v)
            
#creating  gui elements
textField = Entry(root,width=textFieldWidth,borderwidth=10)
savedValue=Entry(root,width=50,borderwidth=2,bg='grey')
button0=Button(root,text='0',width= bWidth,height= bHeight,command=lambda:number_click('0'))
button1=Button(root,text='1',width=bWidth,height= bHeight,command=lambda:number_click('1'))
button2=Button(root,text='2',width= bWidth,height= bHeight,command=lambda:number_click('2'))
button3=Button(root,text='3',width= bWidth,height= bHeight,command=lambda:number_click('3'))
button4=Button(root,text='4',width= bWidth,height= bHeight,command=lambda:number_click('4'))
button5=Button(root,text='5',width= bWidth,height= bHeight,command=lambda:number_click('5'))
button6=Button(root,text='6',width= bWidth,height= bHeight,command=lambda:number_click('6'))
button7=Button(root,text='7',width= bWidth,height= bHeight,command=lambda:number_click('7'))
button8=Button(root,text='8',width= bWidth,height= bHeight,command=lambda:number_click('8'))
button9=Button(root,text='9',width= bWidth,height= bHeight,command=lambda:number_click('9'))
buttonMul=Button(root,text='*',width= bWidth,height= bHeight,command=lambda:operator_click('*'))
buttonDiv=Button(root,text=r'/',width= bWidth,height= bHeight,command=lambda:operator_click(r'/'))
buttonAdd=Button(root,text='+',width= bWidth,height= bHeight,command=lambda:operator_click('+'))
buttonSub=Button(root,text='-',width= bWidth,height= bHeight,command=lambda:operator_click('-'))
buttonDec=Button(root,text='.',width= bWidth,height= bHeight,command=lambda:number_click('.'))
buttonSign=Button(root,text=r'+/-',width= bWidth,height= bHeight,command=lambda:single_operand_calc_click('Sign'))
buttonEq=Button(root,text='=',width= bWidth,height= bHeight,command= eq_click)
buttonPow=Button(root,text='xPow(y)',width= bWidth,height= bHeight,command=lambda:operator_click('**'))
buttonPer=Button(root,text='%',width= bWidth,height= bHeight,command= lambda:single_operand_calc_click('Per'))
buttonClear=Button(root,text='Clear',width= bWidth,height= bHeight,command= c_click)
buttonSqrt=Button(root,text='xPow(1/2)',width= bWidth,height= bHeight,command= lambda:single_operand_calc_click('Sqrt'))
buttonFact=Button(root,text='x!',width= bWidth,height= bHeight,command= lambda:single_operand_calc_click('Fact'))
buttonLog=Button(root,text='log10',width= bWidth,height= bHeight,command= lambda:single_operand_calc_click('Log'))
buttonLn=Button(root,text='ln',width= bWidth,height= bHeight,command= lambda:single_operand_calc_click('Ln'))
buttonRec=Button(root,text='1/x',width= bWidth,height= bHeight,command= lambda:single_operand_calc_click('Rec'))
buttonExp=Button(root,text='exp',width= bWidth,height= bHeight,command= lambda:single_operand_calc_click('Exp'))
buttonMshow=Button(root,text='Ms',width= bWidth,height= bHeight,command= lambda:mem_control_click('Mshow'))
buttonMadd=Button(root,text='M+',width= bWidth,height= bHeight,command= lambda:mem_control_click('Madd'))
buttonMsub=Button(root,text='M-',width= bWidth,height= bHeight,command= lambda:mem_control_click('Msub'))
buttonMrem=Button(root,text='Mr',width= bWidth,height= bHeight,command= lambda:mem_control_click('Mrem'))
buttonBack=Button(root,text='Backspace',width= bWidth,height= bHeight,command= backspace_click)
buttonDel=Button(root,text='Del',width= bWidth,height= bHeight,command= del_click)

#adding gui elements to screen
savedValue.grid(row=0,column=0,columnspan=4)
textField.grid(row=1,column=0,columnspan=4,padx=10,pady=5)
buttonBack.grid(row=1,column=4)
buttonDel.grid(row=0,column=4)
buttonClear.grid(row=3,column=0)
buttonPow.grid(row=3,column=1)
buttonPer.grid(row=3,column=2)
buttonDiv.grid(row=3,column=3)
button7.grid(row=4,column=0)
button8.grid(row=4,column=1)
button9.grid(row=4,column=2)
buttonMul.grid(row=4,column=3)
button4.grid(row=5,column=0)
button5.grid(row=5,column=1)
button6.grid(row=5,column=2)
buttonSub.grid(row=5,column=3)
button1.grid(row=6,column=0)
button2.grid(row=6,column=1)
button3.grid(row=6,column=2)
buttonAdd.grid(row=6,column=3)
buttonSign.grid(row=7,column=0)
buttonDec.grid(row=7,column=2)
buttonEq.grid(row=7,column=3)
buttonSqrt.grid(row=3,column=4)
buttonFact.grid(row=4,column=4)
buttonLog.grid(row=5,column=4)
buttonLn.grid(row=6,column=4)
buttonRec.grid(row=7,column=4)
buttonMshow.grid(row=2,column=0)
buttonMadd.grid(row=2,column=1)
buttonMsub.grid(row=2,column=2)
buttonMrem.grid(row=2,column=3)
buttonExp.grid(row=2,column=4)
button0.grid(row=7,column=1)        
root.mainloop() 


