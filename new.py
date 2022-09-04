import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  database='MUSIC',
  user="root",
  password="12345678"
)
data=[]
cursor=mydb.cursor()

cursor.execute("SELECT * FROM xyz")
row = cursor.fetchone()
while row is not None:
    data.append(row)
    row = cursor.fetchone()
songs=[]
x=input("enter username : ")
for c in data:
    if (c[0]==x):
        for i in range(1,9):
            songs.append(c[i])
DATA=['mood','sugar','light switch','outside','time','beliver','thunder','girls like you']
i=0
for c in songs:
    if(c==max(songs)):
        print(DATA[i])
        songs.remove(c)
        del DATA[i]
        break
    i+=1
i=0
for c in songs:
    if(c==max(songs)):
        print(DATA[i])
        songs.remove(c)
        del DATA[i]
        break
    i+=1    
    
    
        


