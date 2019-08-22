import pytesseract
import os 
import csv
import time
from PIL import Image,ImageDraw

'''
    N 中间点和周围8个点的重复次数 若超过G次判定此点为噪点。
    C 降噪次数
    G 二值化的阈值
'''

def Noise_reduction(path,G,C,N):
    img=Image.open(path)
    t2val={}
    #将图像转换为二值表保存在t2val中
    for x in range(0,img.size[0]):
        for y in range(0,img.size[1]):
            g=img.getpixel((x,y))
            if g<G :
                t2val[(x,y)]=0
            else:
                t2val[(x,y)]=1
    #根据二值表，进行降噪处理
    #某点与周围的8个点值作比较，不同的值越多，说明该点越有可能是噪点   
    for i in range(0,C):
        t2val[(0,0)]=1
        t2val[(img.size[0]-1,img.size[1]-1)]=1
        for x in range(1,img.size[0]-1):
            for y in range(1,img.size[1]-1):
                nearDotsCount=0
                L=t2val[(x,y)]
                if L==t2val[(x-1,y-1)]:
                    nearDotsCount+=1
                if L==t2val[(x-1,y)]:
                    nearDotsCount+=1
                if L==t2val[(x-1,y+1)]:
                    nearDotsCount+=1
                if L==t2val[(x,y-1)]:
                    nearDotsCount+=1
                if L==t2val[(x-1,y+1)]:
                    nearDotsCount+=1
                if L==t2val[(x+1,y-1)]:
                    nearDotsCount+=1
                if L==t2val[(x+1,y)]:
                    nearDotsCount+=1
                if L==t2val[(x+1,y+1)]:
                    nearDotsCount+=1
                if nearDotsCount < N :
                    t2val[(x,y)]=1
    #新建画布，重新绘制图像
    im=Image.new("1",img.size)
    draw = ImageDraw.Draw(im)

    for x in range(0,img.size[0]):
        for y in range(0,img.size[1]):
            draw.point((x,y),t2val[(x,y)])
    im.save('out/t2val.png')
    return im


def Getgry(path):
    #重新定向输出文件目录
    image=Image.open(path)
    path=path.replace('source_png','out')
    #转化为灰度图
    imgry=image.convert('L')
    path=path.replace('.png','-grey.png')
    imgry.save(path)
    #转换为二值图
    out = imgry.point(table,'1')
    path=path.replace('-grey.png','-2val.png')
    out.save(path)


def test(path):
    r,g,b=0,0,0
    img=Image.open(path)
    w,h=img.size
    for x in range(w):
        for y in range(h):
            r,g,b,a=img.getpixel((x,y))
            if 190<=r<=255 and 170<=g<=255 and 0<=b<=140:
                img.putpixel((x,y),(0,0,0))
            if 0<=r<=90 and 210<=g<=255 and 0<=b<=90:
                img.putpixel((x,y),(0,0,0))
    img=img.convert('L').point([0]*150+[1]*(256-150),'1')
    return img

if __name__=="__main__":
    thershold=140
    pathlist=[]
    table=[]
    rate,ok,ng,count=0.0,0,0,0
    for i in range(256):
        if i < thershold:
            table.append(0)
        else:
            table.append(1)

    for root,sub_dirs,files in os.walk('./source_png/'):
        for filename in files:
            filename=os.path.join(root,filename)
            if '.png' in filename :
                pathlist.append(filename)
                print(filename)
    
    for filename in pathlist :
        Getgry(filename)
        im = Noise_reduction(filename,(127,127,127,127),3,3)
        target=filename.split('/')[-1].replace('.png','')
        outstr=pytesseract.image_to_string(im)
        if target==outstr:
            ok+=1
        else:
            ng+=1
        count+=1
        if '/' in outstr:
            outstr=outstr.replace('/','*')
        path=filename.replace('.png','('+outstr+')'+'.png')
        path=path.replace('source_png','out')
        print('the orginal code:'+target)
        print('after scanning...'+outstr)
        im.save(path)
    rate=ok/count*100
    print('pass:'+str(ok)+'\n'+'NG:'+str(ng)+'\n'+'Rate:'+str(rate)+'%')

    if os.path.exists('tongji.csv')==False:
        with open('tongji.csv','w+') as fp:
            writer=csv.writer(fp)
            writer.writerow(['Time','Count','OK','NG','Rate','LineNumber'])

    fp=open('tongji.csv','a+')
    writer=csv.writer(fp)
    writer.writerow([time.asctime(),str(count),str(ok),str(ng),str(rate)+'%','9'])
    fp.close()

    

#    im=test(path)
#    im.save('./verification/2val.png')
