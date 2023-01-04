import os
import cv2
import numpy as np

tot = 0
print(os.listdir('./'))
eps = os.listdir('./svgs')
 
for i in eps:
    if i[-4:]=='.svg' or i[-4:]=='.SVG':
        # print(i)
        command = 'rsvg-convert -d 90 -p 90 ./svgs/'+i+' -o ./pngs_ori/'+i[:-4]+'.png'
        os.system(command)
        command = 'convert -background white ./pngs_ori/'+i[:-4]+'.png ./jpg/'+i[:-4]+'.jpg'
        os.system(command)
        file_name = i[:-4]+'.jpg'
        image = cv2.imread('./jpg/'+file_name)
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                # print(image[i, j])
                if image[x, y][0] > 100 and image[x, y][1] > 100 and image[x, y][2] > 100 :
                    image[x, y] = [0,0,0]
                elif image[x, y][0] <= 100 and image[x, y][1] <= 100 and image[x, y][2] <= 100 :
                    image[x,y] = [255,255,255]
                # print(image[i,j])

            #     break
            # break
        # print(image)
        # break
        cv2.imwrite('./jpg/'+file_name, image)
        # break
        with open('./svgs/'+i, 'r') as f:
            data = f.readlines()
            with open('./svgs_after/'+i, 'w') as fw:
                num = 0
                for j in data:
                    if num <=2:
                        fw.writelines(j)
                        num += 1
                    else:
                        if 'stroke-width' in j:
                            fw.writelines(j)
                fw.writelines('</g>\n'
                            '</svg>')
        
        with open('./svgs_after/'+i,'r')as f:
            data = f.readlines()
            all = []
            for j in data:
                # print(j)
                tmp = j.split(';')
                # print(tmp)
                t = ''
                for x in tmp:
                    # fill:rgb(70.506287%,70.506287%,70.506287%);fill-opacity:1;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;
                    if x[:4] == 'fill':
                        continue
                    if x[:11] == 'stroke-line':
                        continue
                    if x[:12] == 'stroke-width':
                        f = 'stroke-width:1'
                        if t == '':
                            t = f
                        else:
                            t = t+';'+f
                    elif x[:10] == 'stroke:rgb':
                        f = 'stroke:rgb(100%,100%,100%)'
                        if t == '':
                            t = f
                        else:
                            t = t+';'+f
                    elif x[:17] == '<path style="fill':
                        f = '<path style="fill:none'
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
        with open('./svgs_after/'+i,'w') as fw:
            for j in all:
                fw.writelines(j)
        command = 'rsvg-convert -d 90 -p 90 ./svgs_after/'+i+' -o ./pngs_after/'+i[:-4]+'.png'
        # command = 'convert ./svgs_after/'+i+' -background white ./pngs_after/'+i[:-4]+'.png'
        os.system(command)
        command = 'convert -background white ./pngs_after/'+i[:-4]+'.png ./pngs_after/'+i[:-4]+'.jpg'
        os.system(command)
        file_name = i[:-4]+'.png'
        image = cv2.imread('./pngs_after/'+file_name)
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                # print(image[i, j])
                if image[x, y][0] > 100 and image[x, y][1] > 100 and image[x, y][2] > 100 :
                    image[x, y] = [255,255,255]
                elif image[x, y][0] <= 100 and image[x, y][1] <= 100 and image[x, y][2] <= 100 :
                    image[x,y] = [0,0,0]

                break
            break
        # print(image)
        # break
        os.system('rm ./pngs_after/*.jpg')
        cv2.imwrite('./pngs_after/'+file_name[:-4]+'.png', image)
        tot += 1
        if tot%10 == 0:
            print(tot/len(eps))
        # break
