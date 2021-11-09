import psycopg2

class Product:
    def __init__(self,id,asin):
        self.id = id
        self.asin = asin
        self.title = ""
        self.group = ""
        self.salesrank = 0

    def toDB(self):
        return 

class Similar:
    def __init__(self):
        self.product_id = 0
        self.product_tog_id = 0

class Subcat:
    def __init__(self):
        self.cat_id = 0
        self.cat_name = ""
        self.subcat_id = 0
        self.subcat_name = ""

class Cat_prod:
    def __init__(self):
        self.catid = 0
        self.product_asin = ""

class Reviews:
    def __init__(self):
        self.product_asin = ""
        self.date = ""
        self.customer_id = 0
        self.rating = 0
        self.votes = 0
        self.helpf = 0



def parser():
    with open('ptest.txt') as file:
        file_contents = file.read()
        file_split_by_id = file_contents.split('Id:   ',-1)
        x = 1
        while(x < len(file_split_by_id)):
            file_split_by_line = file_split_by_id[x].split('\n',-1)
            z = 0
            while(z < len(file_split_by_line)):
                l=1
                file_split_by_space = file_split_by_line[z].split(' ',-1)
                if(z == 0 ):
                    product_data = Product(int(file_split_by_line[z]),"")
                elif(z == 1 ):
                    product_data.asin = file_split_by_space[1]
                elif(z == 2 and file_split_by_line[z] != '  discontinued product'):
                    split_title = file_split_by_line[2].split(' ',3)
                    product_data.title = split_title[3]
                elif(z == 2 and file_split_by_line[z] == '  discontinued product') :
                    print("commit")
                    z = len(file_split_by_line)
                elif(z == 3):
                    product_data.group = file_split_by_space[3]
                elif(z == 4):
                    product_data.salesrank = file_split_by_space[3]
                    print(product_data.id,product_data.asin,product_data.title,product_data.group,product_data.salesrank)
                elif(z == 5):
                    qtSim = int(file_split_by_space[3])
                elif(z == 6):
                    qtCat = int(file_split_by_space[3])
                elif(z == qtCat + 7):
                    qtRev = int(file_split_by_space[4])
                    l = z+1
                    while (l < qtRev + z+1):
                        review_data = Reviews
                        review = file_split_by_line[l].split(' ',-1)
                        key = review[0]
                        print(review)
                        i = 0
                        while(i < len(review)):
                            if(review[i] == key):
                                del(review[i])
                            else:
                                i+=1
                        print(review)

                        l+=1
                    print(review_data.product_asin,review_data.date,review_data.customer_id,review_data.rating,review_data.votes,review_data.helpf)
                z+=1
            x+=1


    fr = "|Books[283155]|Subjects[1000]|Religion & Spirituality[22]|Christianity[12290]|Clergy[12360]|Preaching[12368]"
    fd = fr.split('|',-1)

    
    cd = fd[1].split('[',1)
    
    catID = int(''.join(filter(str.isdigit,fd[1])))




parser()