from PIL import Image, ImageDraw, ImageFont
import pandas as bhalu
import qrcode


def drawidkwhatfuncname(txt,txt2,txt3,a):
    img = Image.open("cert.png")
    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("ProductSans-Medium.ttf", 130)
    fnt2 = ImageFont.truetype("ProductSans-Regular.ttf", 50)
    fnt3 = ImageFont.truetype("ProductSans-Regular.ttf", 30)
    draw.text((1055, 920),font=fnt,text=txt,fill =(0, 0, 0))
    draw.text((1060, 865),font=fnt2, text=txt2,fill=(140,143,148))
    draw.text((2411, 2696),font=fnt3, text=txt3,fill=(103,107,115))
    kewR = qrcode.make(txt3)
    img.paste(kewR,(2810,2150))
    pdf=img.convert('RGB')
    pdf.save(r"Certs/"+txt+".pdf")

xls=bhalu.ExcelFile("GCCP-ABESIT.xlsx") 
Naam = bhalu.read_excel(xls, "FINAL")   
Links = bhalu.read_excel(xls, "ABES Institute of Technology - ")
col1 = Naam[Naam.columns[1]].values.tolist()
col2 = Links[Links.columns[0]].values.tolist()
col3 = Links[Links.columns[11]].values.tolist()
NameList=[]
ProfileList=[]

for i in range(len(col1)):
    for j in range(len(col2)):
        if col1[i] in col2[j]:  
            if col1[i] not in NameList:
                NameList.append(col1[i])
                ProfileList.append(col3[j])

print(len(NameList),len(col1),len(ProfileList))                                                             #testttttttttt

for i in range(len(NameList)):
    print(NameList[i].title() , ProfileList[i])
    
    drawidkwhatfuncname(NameList[i].title(),"Nov 2, 2023" ,ProfileList[i],i)
                                                                                                            #UwU                                                                   