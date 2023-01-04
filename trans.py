import os

tot = 0
print(os.listdir('../'))
eps = os.listdir('../eps')
 
for i in eps:
    if i[-4:]=='.eps' or i[-4:]=='.EPS':
        command = 'cp ../eps/'+str(i)+' ../eps_after/'+str(tot)+'.eps'
        os.system(command)
        command = 'ps2pdf -dEPSCrop ../eps_after/'+str(tot)+'.eps'
        os.system(command)
        # print(os.listdir('./'))
        command = 'pdf2svg '+str(tot)+'.pdf ../svgs/'+str(tot)+'.svg'
        os.system(command)
        all = []
        # print(tot)
        with open('../svgs/'+str(tot)+'.svg','r')as f:
            data = f.readlines()
            num = 0
            for j in data:
                if num == 1:
                    # print(j)
                    num += 1
                    tmp = j.split(' ')
                    t = ''
                    for x in tmp:
                        # print(x)
                        if x[:6] == 'width=':
                            f = 'width="256"'
                            if t == '':
                                t = f
                            else:
                                t = t + ' '+f
                        elif x[:7] == 'height=':
                            f = 'height="256"'
                            if t == '':
                                t = f
                            else:
                                t = t+' '+f
                        else:
                            if t == '':
                                t = x
                            else:
                                t = t +' '+x
                    all.append(t)
                    continue
                num += 1

                # print(j)
                tmp = j.split(';')
                # print(tmp)
                t = ''
                for x in tmp:
                    if x[:10] == 'stroke:rgb':
                        f = 'stroke:rgb(100%,100%,100%)'
                        if t == '':
                            t = f
                        else:
                            t = t+';'+f
                    elif x[:8] == 'fill:rgb':
                        f = 'fill:rgb(100%,100%,100%)'
                        if t == '':
                            t = f
                        else:
                            t = t+';'+f
                    else:
                        if t == '':
                            t = x
                        else:
                            t = t+';'+x
                # print(t)
                # fw.writelines(t)
                all.append(t)
        with open('../svgs/'+str(tot)+'.svg','w') as fw:
            for i in all:
                fw.writelines(i)

        # break
        # command = 'rsvg-convert -d 450 -p 450 ../svgs/'+str(tot)+'.svg -o ../pngs_ori/'+str(tot)+'.png'
        # os.system(command)
        # command = 'convert -background white ../pngs_ori/'+str(tot)+'.png ../jpg/'+str(tot)+'.jpg'
        # os.system(command)
        # command = 'rsvg-convert -d 450 -p 450 ../svgs_after/'+str(tot)+'.svg -o ../pngs_after/'+str(tot)+'.png'
        # os.system(command)
        # rsvg-convert -d 900 -p 900 0.svg -o 0.png
        tot += 1
        if tot%10 == 0:
            print(tot/len(eps))
        # break
