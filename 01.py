import string, random 

def coupon_creator(digit):
    coupon = ''
    for i in range(digit):
        coupon += random.choice(string.ascii_uppercase + string.digits)
    return coupon 

def create_some_coupons():
    data = ''
    for i in range(200):
        digit = 12 
        j = i+1
        data += 'coupon No.' + str(j) + ' ' + coupon_creator(digit) + '\n'
    return data

with open('coupondata.txt','w') as f:
    f.write(create_some_coupons())

db = pymysql.connect('localhost','root', 'newpass','test')
cursor = db.cursor()

sql = '''create table fruit_price(
       id int primary key auto_increment,
       name char(20)
       price int);
       '''

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

cursor.close()
db.close()