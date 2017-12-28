"""
C:\\Users\\黃\\Desktop\\test
TreeExample-BranchInfo.txt
TreeExample-Branches.txt
"""

########
#Input 兩個TXT
#先定義再放入
#####
def main ():
    from queue import Queue
    import os
    q=Queue()
    my_path = input ('輸入你的路徑:')
    os.chdir(my_path) #切換路徑
    d=input("輸入你要的檔名.txt: ") 
    d=open(d,"w")
###
##data-in
###
    def inpu():
        tree_ex_braninfo=input("輸入braninfo.txt:")
        tree_ex_bran=input("輸入bran.txt:")
        if os.path.isfile(tree_ex_braninfo) and tree_ex_braninfo.endswith('.txt'):
            tree= open(tree_ex_braninfo)
        else: print("no_exist:braninfo")
        if os.path.isfile(tree_ex_bran) and tree_ex_bran.endswith('.txt'):
            tre= open(tree_ex_bran)
        else: print("no_exist:bran")
        braninfo=tree.readlines()
        bran=tre.readlines()
        return braninfo,bran
#list = os.listdir(my_path)
###
#data_process-ini
###
    def d_process_ini(infor):
        braninfo=infor[0]
        bran=infor[1]
        bran_info=[]
        bran_ex=[]
        total_branch = []
        i=0
        bran_info=[]
        length_ratio=[]
        for var in braninfo:
            if var.startswith('Total branch point'):
                uid = var.split()[5]
                total_branch.append([uid])
         #bran_name = bran_cp = bran_volength = bran_level = bran_parent = None
            elif var.startswith('TreeExample',21):
                bran_name = var.split()[0]
                bran_cp = var.split()[1]
                bran_volength = var.split()[4]
                bran_level = var.split()[12]
                bran_parent = var.split()[13]
                bran_info.append([bran_name,bran_cp,bran_volength,bran_level,bran_parent])
        for var in bran:
            i=i+1
            if var.startswith("Parent ID = 0"):
        #initialize
                bran_ex_ID=bran[i-2]
                #bran_ex_parentID=bran[i-1]
                bran_ex_level=bran[i]
                bran_ex_CP=bran[i+1]
                bran_ex_CP=bran_ex_CP.split()
                bran_ex_vlength=bran[i+4]
                cp=int(bran_ex_CP[2])
                BP_num=bran[cp+14+i]
                bp=int(BP_num.split()[2])
                BP_CHild_ID=[]
                for cha in range(1,bp+1):
                    BP_CHild_ID.append(bran[cp+15+i+bp+cha])
                bran_ex_cp_num=[]
                for num in range(1,cp+1):
                    bran_ex_cp_num.append(bran[i+12+num])
                level=1
        def offspring(BP_CHild_ID):
            div=[]
            for var in BP_CHild_ID:
                x=var.split()[3]
                div.append(x)
            return div  
        d.write("total_branch:")
        d.write(str(total_branch[0]))
        d.write("\n")
        d.write("==============")
        d.write("\n")
        d.write("from: ")
        d.write(str(bran_ex_ID))
        d.write("\n")
        d.write(str(bran_ex_vlength))
        d.write("\n")
        div=offspring(BP_CHild_ID)
        BP_CHild=[]
        child_le=[]
        #倒敘
        d.write("to: ")
        d.write("\n")
        for i in range(len(div)-1, -1, -1): 
            child=div.pop(i)
            a="ID = "
            a=a+str(int(child))+("\n")
            d.write(a)
            d.write(": ")
            t=0
            for var in bran:
                t=t+1
                if var.startswith("ID") and a == bran[t-1]   :
                    child_vlength=bran[t+5].split()[2]
                    d.writelines(bran[t+5])#voxel_length
                    child_vlength=float(child_vlength)
                    child_le.append(child_vlength)

        child_le=sorted(child_le,key=float,reverse=True)#finish sort 
        bran_ex_vlength=float(bran_ex_vlength.split()[2])
        length_ratio.append([1])
        for dd in child_le:
            length_ratio.append([float((float(dd))/bran_ex_vlength)])
        d.write("\n")
        d.write("level zero : ")
        d.write(str(level))
        d.write("\n")
        d.write("length_ratio :")
        d.write(str(length_ratio))    
        d.write("\n")
        d.write("\n")
        d.write("==============")
        d.write("\n")
        d.write(str(bran_ex_ID))
        d.write("\n")
        for dd in bran_ex_cp_num:
            d.write(str(dd))
        d.write("==============")
        print(child_le)
        os.system("pause")
        return child_le,BP_CHild_ID,bran_info
###advance_process
##sorting 順序
##放入queue
##小bug
###
    def sorting(ini,q):
        child_le=ini[0]
        BP_CHild_ID=ini[1]
        bran_info=ini[2]
        t=0
        for d in child_le:
            for var in bran_info:
                if (float(var[2])) == d:
                    t=t+1
                    cd=var[0]
                    q.put(cd)
        return t #總共幾個
    
    def sorting_ad(ini,q):
        for ch in ini:
            child_le=ch[0]
            BP_CHild_ID=ch[1]
            bran_info=ch[2]
            t=0
            for d in child_le:
                for var in bran_info:
                    if (float(var[2])) == d:
                        t=t+1
                        cd=var[0]
                        q.put(cd)
        return t #總共幾個
###       
##input(offspring)
###
    def d_process_a(q,t):
        proce_ID=[]
        for var in range(t):
            proce_ID.append(q.get())
        if proce_ID == [] :
            return proce_ID
        #print(type(proce_ID[0]))#str
        return proce_ID
    def d_process_ad(proce_ID,infor):
        bran=infor[1]
        braninfo=infor[0]
        bran_info=[]
        for var in braninfo:
            if var.startswith('TreeExample',21):
                bran_name = var.split()[0]
                bran_cp = var.split()[1]
                bran_volength = var.split()[4]
                bran_level = var.split()[12]
                bran_parent = var.split()[13]
                bran_info.append([bran_name,bran_cp,bran_volength,bran_level,bran_parent])
        if proce_ID == []:
            return
        def offspring(BP_CHild_ID):
            div=[]
            for var in BP_CHild_ID:
                x=var.split()[3]
                div.append(x)
            return div
        #倒敘
        fk=0
        d.write("\n")
        d.write("==============")
        for ch in proce_ID:
            i=0
            length_ratio=[]
            BP_CHild_ID=[]
            bran_ex_cp_num=[]
            BP_CHild=[]
            child_le=[]
            ini=[]
            for var in bran:
                i=i+1
                if ch in var:
                    bran_ex_ID=bran[i]
                #bran_ex_parentID=bran[i-1]
                    bran_ex_level=bran[i+2]
                    bran_ex_CP=bran[i+3]
                    bran_ex_CP=bran_ex_CP.split()
                    bran_ex_vlength=bran[i+6]
                    cp=int(bran_ex_CP[2])
                    BP_num=bran[cp+16+i]
                    bp=int(BP_num.split()[2])
                    
                    for cha in range(1,bp+1):
    
                        BP_CHild_ID.append(bran[cp+17+i+bp+cha])
                    
                    for num in range(1,cp+1):
                        bran_ex_cp_num.append(bran[i+14+num])
                    d.write("\n")
                    d.write("from: ")
                    d.write(str(bran_ex_ID))
                    d.write("\n")
                    d.write(str(bran_ex_vlength))
                    d.write("\n")
                    d.write("to: ")
                    d.write("\n")
                    div=offspring(BP_CHild_ID)
                    for i in range(len(div)-1, -1, -1):
                        child=div.pop(i)
                        a="ID = "
                        a=a+str(int(child))+("\n")
                        d.write(a)
                        d.write(": ")
                        t=0
                        if a == "ID = 0\n":
                            d.write("Length(V) = 0")
                            d.write("\n")
                        for var in bran:
                            t=t+1
                            if var.startswith("ID") and a == bran[t-1]   :
                                child_vlength=bran[t+5].split()[2]
                                d.writelines(bran[t+5])#voxel_length
                                child_vlength=float(child_vlength)
                                child_le.append(child_vlength)
                        child_le=sorted(child_le,key=float,reverse=True)#finish sort 
                    bran_ex_vlength=float(bran_ex_vlength.split()[2])
                    length_ratio.append([1])
                    for dd in child_le:
                        length_ratio.append([float((float(dd))/bran_ex_vlength)])
                    d.write("\n")
                    d.write("level zero : ")
                    d.write(bran_ex_level)
                    d.write("\n")
                    d.write("length_ratio :")
                    d.write(str(length_ratio))    
                    d.write("\n")
                    d.write("\n")
                    d.write("==============")
                    d.write("\n")
                    d.write(str(bran_ex_ID))
                    d.write("\n")
                    for dd in bran_ex_cp_num:
                        d.write(str(dd))
                    d.write("\n")
                    d.write("==============")
                    ini.append([child_le,BP_CHild_ID,bran_info])
                    fk=fk+sorting_ad(ini,q)
                    #return child_le,BP_CHild_ID,bran_info
    
        proce_ID=d_process_a(q,fk)  
        d_process_ad(proce_ID,infor)        
#####call(offspring):length
###執行function
    
    infor=inpu()           
    ini=d_process_ini(infor)
    t=sorting(ini,q)
    proce_ID=d_process_a(q,t)
    d_process_ad(proce_ID,infor)
    d.close()
if __name__ == "__main__":
  main()

