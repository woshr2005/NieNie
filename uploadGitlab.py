from gitlab import Gitlab
import os
import mysql.connector
#import base64

#token = "sYxizzwV92jo5LGophAx"  
#url = "https://gitlab.atsspec.net/"
#gl = Gitlab(url,token)
#groups = gl.groups.list()

#group = gl.groups.get(50)
#members = group.members.list()
#for i in members:
#    print(i.username)
#    print(i.id)
mytoken = "1FDodQugYf7BTxgzMA6U" 


def sub(token=mytoken,branch = 'Jun'):
    url = "https://gitlab.atsspec.net/"
    gl = Gitlab(url,token)
    prp_obj = gl.projects.get(180) 
    path = "C:/ATS/file/Code"
    files = os.listdir(path)
    #print (files)

    #projects = gl.projects.list (all=True)
    #for i in projects:
        #print(i.name) 
       # print(i.id)
    #print(prp_obj.title)
    
    #a = prp_obj.members.list()
   # for i in a:
       # print(i) 
    #prp_obj.commits.list()
    
    
    for i in files:
        file = open (i,"r")
        prp_obj.files.create({'file_path': i,
                                  'branch': branch,
                                  'content': file.read(),
                                  'author_email': 'jun@atsspec.com',
                                  'author_name': 'Jun Xiong',
                                  'commit_message': i})
        print ("uploading: "+str(i))
        file.close()

def sub2(token=mytoken,branch = 'Jun'):
    url = "https://gitlab.atsspec.net/"
    gl = Gitlab(url,token)
    prp_obj = gl.projects.get(180) 
    path = "C:/ATS/file/Code"
    files = os.listdir(path)
    #print (files)

    #projects = gl.projects.list (all=True)
    #for i in projects:
        #print(i.name) 
       # print(i.id)
    #print(prp_obj.title)
    
    #a = prp_obj.members.list()
   # for i in a:
       # print(i) 
    #prp_obj.commits.list()
    
    
    for i in files:
        file = open (i,"r")
        prp_obj.files.create({'file_path': i,
                                  'branch': branch,
                                  'content': file.read(),
                                  'author_email': 'jun@atsspec.com',
                                  'author_name': 'Jun Xiong',
                                  'commit_message': i})
        print ("uploading: "+str(i))
        file.close()

def merge(token=mytoken,branch = 'Jun'):
   url = "https://gitlab.atsspec.net/"
   gl = Gitlab(url,token)
   prp_obj = gl.projects.get(180) 
   prp_obj.mergerequests.create({'source_branch': branch,
                                  'target_branch': 'staging',
                                  'title': 'Jun',
                                  'assignee_id': 56})#33 roseanna 56 Jun
    
def mergeASAP(token=mytoken):
   url = "https://gitlab.atsspec.net/"
   gl = Gitlab(url,token)
   prp_obj = gl.projects.get(180) 
   prp_obj.mergerequests.create({'source_branch': 'Jun',
                                  'target_branch': 'staging',
                                  'title': 'Jun ASAP',
                                  'assignee_id': 56})#33 roseanna 56 Jun  
#sub()
#merge()

def mastermerge(token=mytoken,branch = 'staging'):
   url = "https://gitlab.atsspec.net/"
   gl = Gitlab(url,token)
   prp_obj = gl.projects.get(180) 
   prp_obj.mergerequests.create({'source_branch': branch,
                                  'target_branch': 'master',
                                  'title': 'Jun',})#33 roseanna 56 Jun
    
    
    
    
    
    
def deleteFiles(token=mytoken):
    url = "https://gitlab.atsspec.net/"
    gl = Gitlab(url,token)
    prp_obj = gl.projects.get(180)
    #f = prp_obj.files.get(file_path="QUOTE-2018-11-12-17.08-Jun_IMS2_Insert_List4.sql", ref='Jun')
    #f.content = open('QUOTE-2018-11-12-17.08-Jun_IMS2_Insert_List4.sql').read() + "###"
    #f.save(branch='Jun', commit_message='Clean')    
    for i in range(70,73):
        name = "QUOTE-2018-11-12-17.08-Jun_IMS2_Insert_List"+ str(i)+".sql"
        f = prp_obj.files.get(file_path=name, ref='Jun')
        f.content = open(name).read() + "#####"
        f.save(branch='Jun', commit_message='Resubmit')
        
#deleteFiles()
#merge()





def testquerries(token=mytoken,testdatabase="atsspec_net_data_team"):
    url = "https://gitlab.atsspec.net/"
    gl = Gitlab(url,token)
    prp_obj = gl.projects.get(180)    
    mrs = prp_obj.mergerequests.list()   
    for i in mrs:
        if i.state == "opened":
            print ("Tilte: "+ i.title)
            print ("ID: "+ str(i.iid))
            print("Branch: " + str(i.source_branch) + "\n")
            mr = prp_obj.mergerequests.get(i.iid)
            changes = mr.changes()
            changelist = changes.get("changes")
            for p in changelist:
                filename = str(p.get("old_path"))
                print(filename)
                f = prp_obj.files.get(file_path=filename, ref=i.source_branch)
                sql = str(f.decode())
                sql = sql.replace("\\'","'")
                sql = sql.replace("\\n"," ")
                sql = sql.replace("\\t"," ")
                line = sql.split(";")
                line[0] = "START TRANSACTION"
                line.pop()                
                try:
                    mydb = mysql.connector.connect(
                          host="10.2.4.9",
                          user="data.jun",
                          passwd="junjun",
                          database=testdatabase)                   
                    mycursor = mydb.cursor()
                    for g in line:
                        mycursor.execute(g+";")
                        mydb.commit()
                    mydb.close()    
                except mysql.connector.Error as err:
                  print("Something went wrong: {}".format(err))
                  print("In line "+str(line.index(g)))
                  print(g)



def mergeapprove(token=mytoken):
    url = "https://gitlab.atsspec.net/"
    gl = Gitlab(url,token)
    prp_obj = gl.projects.get(180)    
    mrs = prp_obj.mergerequests.list()   
    for i in mrs:
        if i.state == "opened":
            print ("Tilte: "+ i.title + " Merged")
            print ("ID: "+ str(i.iid))
            print("Branch: " + str(i.source_branch) + "\n")
            mr = prp_obj.mergerequests.get(i.iid)
            mr.merge()


def mastermergeapprove(token=mytoken):
    url = "https://gitlab.atsspec.net/"
    gl = Gitlab(url,token)
    prp_obj = gl.projects.get(180)    
    mrs = prp_obj.mergerequests.list()   
    for i in mrs:
        if i.state == "opened":
            if i.source_branch == "staging":
                mr = prp_obj.mergerequests.get(i.iid)
                mr.merge()
                print ("Tilte: "+ i.title + " Merged")
                print ("ID: "+ str(i.iid))
                print("Branch: " + str(i.source_branch) + "\n")






def createtag(token=mytoken):
    url = "https://gitlab.atsspec.net/"
    gl = Gitlab(url,token)
    prp_obj = gl.projects.get(180)   
    tags = prp_obj.tags.list()
    lasttag = str(tags[0].name)
    num = lasttag.split(".")[-1]
    day = lasttag.split(".")[0]
    tag_name = str(day) + ".0." + str(int(num)+1)
    prp_obj.tags.create({'tag_name': str(tag_name), 'ref': 'master'})
    print(tag_name + " created")

def create1sttag(token=mytoken):
    url = "https://gitlab.atsspec.net/"
    gl = Gitlab(url,token)
    prp_obj = gl.projects.get(180)   
    tags = prp_obj.tags.list()
    lasttag = str(tags[0].name)
    day = lasttag.split(".")[0]
    tag_name = str(int(day)+1) + ".0.1"
    prp_obj.tags.create({'tag_name': str(tag_name), 'ref': 'master'})
    print(tag_name + " created")








def testquerries2(token=mytoken):
    url = "https://gitlab.atsspec.net/"
    gl = Gitlab(url,token)
    prp_obj = gl.projects.get(180)    
    mrs = prp_obj.mergerequests.list()   
    for i in mrs:
        if i.state == "opened":
            print ("Tilte: "+ i.title)
            print ("ID: "+ str(i.iid))
            print("Branch: " + str(i.source_branch) + "\n")
            mr = prp_obj.mergerequests.get(i.iid)
            changes = mr.changes()
            changelist = changes.get("changes")
            for p in changelist:
                filename = str(p.get("old_path"))
                print(filename)
                f = prp_obj.files.get(file_path=filename, ref=i.source_branch)
                sql = str(f.decode())
                sql = sql.replace("\\'","'")
                sql = sql.replace("\\n","")
                sql = sql.replace("\\t","")
                line = sql.split(";")
                line[0] = "START TRANSACTION"
                line.pop()                
                try:
                    mydb = mysql.connector.connect(
                          host="10.2.4.9",
                          user="data.jun",
                          passwd="junjun",
                          database="atsspec_net_hotfixes")                   
                    mycursor = mydb.cursor()
                    for g in line:
                        mycursor.execute(g+";")
                        mydb.commit()
                    mydb.close()    
                except mysql.connector.Error as err:
                  print("Something went wrong: {}".format(err))
                  print("In line "+str(line.index(g)))
                  print(g)








def codetest():    
    f = prp_obj.files.get(file_path="QUOTE-2018-12-27-1.22_PM-Mathankan_ASAP_IMS.sql", ref='mathankan')
    #sql = f.decode()
    sql = str(f.decode())
    sql = sql.replace("\\'","'")
    sql = sql.replace("\\n","")
    line = sql.split(";")
    line[0] = "START TRANSACTION"
    line.pop()
        
    try:
        mydb = mysql.connector.connect(
              host="10.2.4.9",
              user="data.jun",
              passwd="junjun",
              database="atsspec_net_data_team")
        #print(mydb)
        
        mycursor = mydb.cursor()
        for g in line:
            mycursor.execute(g+";")
            #mycursor.rowcount
            #myresult = mycursor.fetchall()
            mydb.commit()
            #print(mycursor.rowcount, "record(s) affected")
        mydb.close()    
    except mysql.connector.Error as err:
      print("Something went wrong: {}".format(err))
      print("In line "+line.index(g))
      print(g)