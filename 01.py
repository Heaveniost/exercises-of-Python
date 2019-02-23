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

def storeInMysql(codelist):
    try:
        conn = pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='mysql')
        cur = conn.cursor()
    except BaseException as e:
        print(e)
    else:
        try:
            cur.execute('CREATE DATABASE IF NOT EXISTS activation_code')
            cur.execute('USE activation_code')
            cur.execute('''CREATE TABLE IF NOT EXISTS code(
                            id INT NOT NULL AUTO_INCREMENT,
                            code VARCHAR(32) NOT NULL,
                            PRIMARY KEY(id)
                        )''')
            for code in codelist:
                cur.execute('INSERT INTO code(code) VALUES(%s)',(code))
                cur.connection.commit()
        except BaseException as e:
            print(e)
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    storeInMysql(generateActivationCode(200))
    print('OK!')

