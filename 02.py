import string, random,re,pymysql

def coupon_creator(digit):
    coupon = ''
    for i in range(digit):
        coupon += random.choice(string.ascii_uppercase + string.digits)
    return coupon 

def create_some_coupons():
    data = ''
    for i in range(20):
        digit = 12 
        data += coupon_creator(digit) + ','
    # coupons = str(data)
    # l = list(coupons)
    # print(l)
    # print(data)
    return data

def storeInMysql(data):
    try:
        db = pymysql.connect('localhost','root','newpass','test')
        cur = db.cursor()
    except BaseException as e:
        print(e)
    else:
        try:
            sql = '''
                create table if not exists coupons(
                id int not null auto_increment,
                code varchar(32) not null,
                primary key(id)
                );
                '''
            cur.execute(sql)
            l = data.split(',')
            l.pop()
            for i in l:
                cur.execute('insert into coupons(code) values(%s)', (i))
                db.commit()
        except BaseException as e:
            print(e)
        finally:
            cur.close()
            db.close()

if __name__ == '__main__':
    storeInMysql(create_some_coupons())
    print('OK')










