# Juliana Duran 202220671 Mateo Rincon 202221402
def separarBloques(lista):
    
    lineasBloque=""
    bloques=[] 
    contadorabre=0
    contadorcierra=0
    for linea in lista:
        
        if linea not in palabras_bloque:
            lineasBloque+=linea
        for caracter in linea:
            if caracter=="{":
                contadorabre+=1
            if caracter=="}":
                contadorcierra+=1
                
        if contadorabre==contadorcierra and contadorabre>0:
            bloques.append(lineasBloque)
            lineasBloque=""
            contadorabre=0
            contadorcierra=0
    return bloques
    
   
def solorevisarparentesis(string):
    abren=0
    cierran=0
    
    
    for x in string:
        
        if x=="}":
            cierran=cierran+1
        if x=="{":
            abren=abren+1
            
        
    if string[0]=="}":
        return False     
    elif cierran!=abren:
        return False
    else:
        return True
     
 
def instruccion_sin_def(string):
    
    
    direcciones=["front","right","left","back"]
    if "not" in string:
        separar=string.split(":")
        cond=separar[1]
        if (instruccion_sin_def(cond)==False):
            return False
        else:
            return True
    if "("not in string or ")" not in string:
        return False
    go=["goNorth()","goSouth()","goEast()","goWest()"]
    
    if "can"in string:
        
        
        s=string[4:]
        split=s.split("{")
        est=False
        contador=0
        for ss in split:
            if contador==0:
                ss=ss[:-1]
            corch=0
            while corch==0:
                
                if len(ss)>0:
                    if ss[len(ss)-1]=="}":
                        ss=ss[:-1]
                    else:
                        corch=1
                    
                
            if instruccion_sin_def(ss)==False:
               
                return False
            else:
                est=True
            contador=contador+1
        if est==True:
            return True
    
    
    
    
    split= string.split("(")
    ins= split[0]
    com=(split[1])[:-1]

    solo_una_variable=["drop","get","grab","letGo"] #
    solo_dos_variables=["jump"] #
    una_o_dos_variables=["walk","leap"]#
    solo_direccion= ["turn"] #
    solo_coordenandas=["turnto"] #
    
    if ins in una_o_dos_variables  and ","not in com:
        if com.isnumeric()==True:
            return True
        else:
            return False
    elif ins in una_o_dos_variables  and ","in com:
        
        split=com.split(",")
      
        if split[0].isnumeric() and split[1] in coordenas:
            return True
        else:
            
            return False
    elif ins in solo_una_variable:
        
        if com.isnumeric():
            return True
        else:
            return False
    elif "jump" == ins:
        
        split=com.split(",")
        if split[0].isnumeric() and split[1].isnumeric():
            return True
        else:
            return False
    elif "turn" == ins:
        if com in direcciones:
            return True
        else:
            return False
    elif "turnto" == ins:
        if com in coordenas:
            return True
        else:
            return False
    elif "facing"== ins:
        if com in coordenas:
            return True
        else:
            return False
    elif "can"== ins:
        if instruccion_sin_def(com)==True:
            return True
        else:
            return False       
    else:
        return False
    
    
 
def instruccion_con_def(string,listavar):
    if "nop"in string:
        string=string[0:12]
    
    direcciones=["front","right","left","back"]
    
    put= ("put"+(listavar[0]).upper()+(listavar[1]).upper())
    
    if string=="defProc":
        return True
    go=["goNorth()","goSouth()","goEast()","goWest()","goNorth","goSouth","goEast","goWest"]
    
    if "go" in string and string in go:
        return True
    
    
    if "can" in string:
        
        s=string[4:]
        split=s.split("{")
        est=False
        contador=0
        for ss in split:
            if contador==0:
                ss=ss[:-1]
                
            if  not instruccion_con_def(ss,listavar):
                
                return False
            else:
                est=True
            contador=contador+1
        if est==True:
            return True
            
    
    if "not" in string:
        separar=string.split(":")
        cond=separar[1]
        if (instruccion_con_def(cond)==False):
            return False
        else:
            return True
    
    if "(" not in string or ")" not in string:
        return False
    
    nop=["nop"]
    if "nop" in string and string!="nop()":
        return False
    
    split= string.split("(")
    ins= split[0]
    com=(split[1])[:-1]
    

    solo_una_variable=["drop","get","grab","letGo"] #
    solo_dos_variables=["jump",put] #
    una_o_dos_variables=["walk","leap"]#
    solo_direccion= ["turn"] #
    solo_coordenandas=["turnto"] #
    if ins in una_o_dos_variables  and "," not in com:
     
        if com.isnumeric() or com in listavar:
            return True
        else:
            return False
    elif ins in una_o_dos_variables  and ","in com:
        split=com.split(",")
        if (split[0].isnumeric() or split[0] in listavar)and (split[1] in coordenas):
            return True
        else:
            return False
    elif ins in solo_una_variable:

        if com.isnumeric() or com in listavar:
            return True
        
        else:
            return False
    elif ins in solo_dos_variables:
        split=com.split(",")
        if (split[0].isnumeric() or split[0] in listavar) and (split[1].isnumeric() or split[1] in listavar):
            
            return True
        else:
            
            return False
    elif "turn" == ins:
        if com in direcciones:
            return True
        else:
            return False
    elif "turnto" == ins:
        if com in coordenas:
            return True
        else:
            return False
    elif "facing"== ins:
        if com in coordenas:
            return True
        else:
            return False
    else:
        return False

def base (nombrearchivo):
    
    archivo = open(nombrearchivo)
    string=archivo.read()
    listaa=string.split()
    lista=[]
    
    
    for i in listaa:
       
        if "defVar" not in i:
            
            lista.append(i)
      
    
    # def var?
    
    if solorevisarparentesis(string)==False:
        
        return False
    else:
        if "defProc" not in string : #sea todo menos def 
            bloques=separarBloques(lista) 
           
            for bloque in bloques:
                
                if revisarBloque(bloque)==False and revisarCondiciones(bloque)==False:
                    
                    return False          
                
            
        else:
            
            
            var1=(lista[2])[1]
            var2=(lista[3])[0]
            listavar=[var1,var2]
            listanueva=[]
            
            p="put"+(var1.upper())+(var2.upper())
            for l in lista:
                if len(l)!=2 and len(l)!=3 and "def" not in l and p!=l:
                   listanueva.append(l)
                    
            
            bloques=separarBloques(listanueva)  
            
            for bloque in bloques:
               
                
                if revisarBloque_def(bloque,listavar)==False:
                    
                    return False 
                 
    return True



def revisarBloque(linea):
   
    for palabra in palabras_bloque:
        if palabra in linea:
            nuevaCadena=""
            contadorabre=0
            contadorcierra=0
            if linea[0]=="{":
                linea=linea[1:]
            for caracter in linea:
                
                if caracter=="{":
                    contadorabre+=1
                if caracter=="}":
                    contadorcierra+=1
                if contadorabre>0:
                    nuevaCadena+=caracter
                    if contadorabre==contadorcierra and contadorabre>0:
                        new=separarBloques(nuevaCadena)
                        for a in new:
                            sies=True
                            if revisarBloque_def(a)==False:
                                return False
                        return True
                                     
                        
                        
    if linea[0]=="{":
        bloquesincorchetes= linea[1:len(linea)-1] 
        split=bloquesincorchetes.split(";")
    else:
        bloquesincorchetes= linea[:len(linea)-1] 
        split=bloquesincorchetes.split(";")
    
    
    
    for s in split:
        
        if len(s)!=0:
            if s[len(s)-1]=="}":
                s=s[:-1]
            if s[0]=="{":
                s=s[1:]
            resp=instruccion_sin_def(s)
      
        if resp==False:
          
            return False
    return True


def revisarCondiciones(linea):
    for palabra in palabras_bloque:
        if palabra in linea:
            nuevaCadena=""
            contadorabre=0
            contadorcierra=0
            for caracter in linea:
                if caracter=="(":
                    contadorabre+=1
                if caracter==")":
                    contadorcierra+=1
                if caracter=="{"or caracter=="}":
                    return False
                if contadorabre>0:
                    nuevaCadena+=caracter
                    if contadorabre==contadorcierra:
                        xxx=nuevaCadena[1:len(nuevaCadena)-2]
                        xxx+=";"
                        xxx=revisarCondiciones(nuevaCadena)
                        if xxx==False:
                            return False 
        
    if linea[0]=="{":
        bloquesincorchetes= linea[1:len(linea)-1] 
        split=bloquesincorchetes.split(";")
    else:
        bloquesincorchetes= linea[:len(linea)-1] 
        split=bloquesincorchetes.split(";")
    
    
    for s in split:
        resp=instruccion_sin_def(s)
       
        if resp==False:
            return False
    return True


def revisarBloque_def(linea,listavar):
   
    for palabra in palabras_bloque:
        if palabra in linea:
            nuevaCadena=""
            contadorabre=0
            contadorcierra=0
            if linea[0]=="{":
                linea=linea[1:]
            for caracter in linea:
                
                if caracter=="{":
                    contadorabre+=1
                if caracter=="}":
                    contadorcierra+=1
                if contadorabre>0:
                    nuevaCadena+=caracter
                    if contadorabre==contadorcierra and contadorabre>0:
                        new=separarBloques(nuevaCadena)
                        for a in new:
                            sies=True
                            if revisarBloque_def(a,listavar)==False:
                                return False
                        return True
                                     
                        
                        
    if linea[0]=="{":
        bloquesincorchetes= linea[1:len(linea)-1] 
        split=bloquesincorchetes.split(";")
    else:
        bloquesincorchetes= linea[:len(linea)-1] 
        split=bloquesincorchetes.split(";")
    
    
    
    for s in split:
        
        if len(s)!=0:
            if s[len(s)-1]=="}":
                s=s[:-1]
            if s[0]=="{":
                s=s[1:]
            resp=instruccion_con_def(s,listavar)
      
        if resp==False:
            
            return False
    return True
        
        

def revisarCondiciones_def(linea,listavar):
    for palabra in palabras_bloque:
        if palabra in linea:
            nuevaCadena=""
            contadorabre=0
            contadorcierra=0
            for caracter in linea:
           
                if caracter=="(":
                    contadorabre+=1
                if caracter==")":
                    contadorcierra+=1
                if contadorabre>0:
                    nuevaCadena+=caracter
                    if contadorabre==contadorcierra and contadorabre>0:
                        xxx=nuevaCadena[1:len(nuevaCadena)-2]
                        xxx+=";"
                        xxx=revisarCondiciones_def(nuevaCadena,listavar)
                        if xxx==False:
                            
                            return False 
    if linea[0]=="{":
        bloquesincorchetes= linea[1:len(linea)-1] 
        split=bloquesincorchetes.split(";")
    else:
        bloquesincorchetes= linea[:len(linea)-1] 
        split=bloquesincorchetes.split(";")
        
    for s in split:
        resp=instruccion_con_def(s,listavar)
       
        if resp==False:
            
            return False
    return True    


solo_una_variable=["drop","get","grab","letGo"]
solo_dos_variables=["jump"]
una_o_dos_variables=["walk","leap"]
solo_direccion= ["turn"]
solo_coordenandas=["turnto"]
nop=["nop"]
go=["goNorth","goSouth","goEast","goWest"]
    
instrucciones=["goNorth","goSouth","goEast","goWest","nop","turnto","turn","walk","leap","jump","drop","get","grab","letGo"]
coordenas=["north","south","east","west"]
direcciones=["front","right","left","back"]
conditions=["facing","can","not"]
palabras_bloque=["while","for","repeat","defProc","if","goNorth()","goSouth()","goEast()","goWest()","else"]








#aca se mete el nombre del archivo
fileName=input("ingrese el nombre del archivo txt")
respuesta=base(fileName)
if respuesta==False:
     print("El programa no es valido")
else:
     print("El programa es valido")