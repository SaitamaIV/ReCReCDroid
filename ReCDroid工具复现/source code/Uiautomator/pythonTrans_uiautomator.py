'''
Created on Jun 12, 2017

@author: yu
'''
from numpy.compat import unicode
from spacy.lang.en import English #源码此处导入地址有误（应该是资源更新了），已修正
import spacy
#import strand
import re
from xml.dom.minidom import Document
from xml.dom import minidom
import time
import os
from gensim.models import Word2Vec #语义匹配模型
import codecs
import shutil
import copy
import os
#grammar = nltk.parse_cfg()
runable=1


def addnlptotext(doc,nlp,node):
    #把nlp解析元组插入到nlp.xml文件（好像是吧，在run.py中找到了呼应的代码）
    for subnode in node.childNodes:        
        if(subnode.nodeType == minidom.Node.ELEMENT_NODE):
            #time.sleep(1)          
            if subnode.hasChildNodes():
            
                if subnode.nodeName.endswith("text"):
                    
                    
                    
                    text=subnode.firstChild.nodeValue.lower()
                    sent=nlp(unicode(text))
                    textnlpelement=doc.createElement(subnode.nodeName+"nlp")
                    node.appendChild(textnlpelement)
                    
                    i=0
                    for word in sent:
                        IDelement=doc.createElement("ID"+str(i))
                        textnlpelement.appendChild(IDelement)
                        wordelement=doc.createTextNode(word.lemma_)
                        IDelement.appendChild(wordelement)
                        i=i+1
                else:
                    addnlptotext(doc,nlp,subnode)
                    
                    
                 #   textnlpelement=doc.createElement("ID"+str(i))
                    
                    
                    
                    
                 #   alltextnlp.appendChild(alltextnlpelement)
                 #   textelement=doc.createTextNode(word.lemma_)
                 #   alltextnlpelement.appendChild(textelement)
                 #   i=i+1




def translate(root, root_new, doc_newresult, packageName, classNameStr):
    #从.xml格式翻译到uiaotomator可以理解的格式
    step=doc_newresult.createElement("Step");
    root_new.appendChild(step);
    
    
    classNameEle=doc_newresult.createElement("Classname");
    step.appendChild(classNameEle);    
    textnode=doc_newresult.createTextNode(classNameStr)
    classNameEle.appendChild(textnode)
    
    
    easyoperate=doc_newresult.createElement("Easyoperate");
    step.appendChild(easyoperate);
    
    alltextset=set()
    
    global runable
    runable=1
    
    iterateTree(root, easyoperate, doc_newresult, alltextset, packageName)
    
    #this is for allText
    allText=doc_newresult.createElement("AllText");
    step.appendChild(allText);
    
    for strItem in alltextset:
        IDtext=doc_newresult.createElement("IDtext");
        allText.appendChild(IDtext)
        textnode=doc_newresult.createTextNode(strItem)
        IDtext.appendChild(textnode)
           
           

#迭代动态有序事件树
def iterateTree(root, step, doc_newresult, alltextset, packageName):
    groupview=["android.widget.ListView","android.widget.LinearLayout"]
    #ListView是一个视图组，显示可滚动项目的列表。并将每个项目结果转换为放置到列表中的视图。
    #线性布局控件，它包含的子控件将以横向或竖向的方式排列，按照相对位置来排列所有的widgets或者其他的containers,超过边界时，某些控件将缺失或消失
    signleview=["android.widget.TextView"]
    
    
    global runable
    
    for node in root.childNodes:
        
        if node.nodeType == node.TEXT_NODE:
            continue
        
        
        if not node.getAttribute("package")==packageName:
            continue
        
        
        
        if node.getAttribute("clickable")=="true":
            
            classname=node.getAttribute("class");

            #这里的class好像又是指的组件（虽然我明明记得之前看到的代码中有class表示页面的，但这里好像不对）
            if classname not in groupview:
                        
                #enabled="true" focusable="true" 
                
                #record.xml中的runableID与run.xml中的subID有相同的含义，即组件的id。
                #下面就是隔着设置和添加
                runableID=doc_newresult.createElement("runableID")
                step.appendChild(runableID)
                runableID.setAttribute("id",str(runable))
                runable=runable+1
                
                if classname=="android.widget.EditText":#here adds the edittype, because uiautomator can not justify the digit and string, at here I only give string.
                    edittype=doc_newresult.createElement("edittype")
                    runableID.appendChild(edittype)
                    textnode=doc_newresult.createTextNode("string")
                    edittype.appendChild(textnode)
                    # here should add an ancestor match, but due to the time limit, I will not adjacyText.
                    
                    # focusable
                    focusable=doc_newresult.createElement("focusable")
                    runableID.appendChild(focusable)
                    textnode=doc_newresult.createTextNode(node.getAttribute("focused"))
                    focusable.appendChild(textnode)
                    
                    
                    
                
                viewclass=doc_newresult.createElement("viewclass")
                runableID.appendChild(viewclass)
                textnode=doc_newresult.createTextNode(node.getAttribute("class"))
                viewclass.appendChild(textnode)    
    
    
                if not node.getAttribute("content-desc")=="":
                    contentext=doc_newresult.createElement("contentext")
                    runableID.appendChild(contentext)
                    textnode=doc_newresult.createTextNode(node.getAttribute("content-desc"))
                    contentext.appendChild(textnode)
                    
                    alltextset.add(node.getAttribute("content-desc"))#all text
    
                
                viewtext=doc_newresult.createElement("viewtext")
                runableID.appendChild(viewtext)
                textnode=doc_newresult.createTextNode(node.getAttribute("text"))
                viewtext.appendChild(textnode)
                           
                alltextset.add(node.getAttribute("text"))#alltext
    
                #this is for source id
                androidid=doc_newresult.createElement("androidid")
                runableID.appendChild(androidid)
                
                ownid=doc_newresult.createElement("ownid")
                androidid.appendChild(ownid)
                textnode=doc_newresult.createTextNode(node.getAttribute("resource-id"))
                ownid.appendChild(textnode)
                
                owntext=doc_newresult.createElement("ownText")
                androidid.appendChild(owntext)
                textnode=doc_newresult.createTextNode(node.getAttribute("resource-id"))
                owntext.appendChild(textnode)
    
                
                #positions
                bounds=node.getAttribute("bounds")
                boundArray=re.findall(r'\d+',bounds)
                
                xvalue=(int(boundArray[0])+int(boundArray[2]))/2;
                yvalue=(int(boundArray[1])+int(boundArray[3]))/2;            
                
                
                #xposition
                xposition=doc_newresult.createElement("xposition")
                runableID.appendChild(xposition)
                textnode=doc_newresult.createTextNode(str(xvalue))
                xposition.appendChild(textnode)
                
                yposition=doc_newresult.createElement("yposition")
                runableID.appendChild(yposition)
                textnode=doc_newresult.createTextNode(str(yvalue))
                yposition.appendChild(textnode)
                
                
                #index
                index=doc_newresult.createElement("index")
                runableID.appendChild(index)
                textnode=doc_newresult.createTextNode(node.getAttribute("index"))
                index.appendChild(textnode)
                
                #clicktype
                
                clicktype=doc_newresult.createElement("clicktype")
                runableID.appendChild(clicktype)
                if node.getAttribute("long-clickable")=="false":
                        textnode=doc_newresult.createTextNode("short")
                        clicktype.appendChild(textnode)
                else:
                        if classname!="android.widget.EditText":
                        ### for long
                            runableIDlong=copy.deepcopy(runableID)
                            step.appendChild(runableIDlong)
                            runableIDlong.setAttribute("id",str(runable))
                            runable=runable+1
    
                            clickTypeLong=runableIDlong.getElementsByTagName("clicktype") 
                            textnode=doc_newresult.createTextNode("long")
                            clickTypeLong[0].appendChild(textnode)
                    
                
                        ###########add the short
                        textnode=doc_newresult.createTextNode("short")
                        clicktype.appendChild(textnode)
                
                '''
                if node.getAttribute("long-clickable")=="true":
                    textnode=doc_newresult.createTextNode("long")
                    clicktype.appendChild(textnode)
                else:
                    textnode=doc_newresult.createTextNode("short")
                    clicktype.appendChild(textnode)
                '''

            #若该组件在当前控件组中
            else:
                for child in node.childNodes:
                    
                    
                    if child.nodeType == node.TEXT_NODE:
                        continue
                    
                    
                    runableID=doc_newresult.createElement("runableID")
                    step.appendChild(runableID)
                    runableID.setAttribute("id",str(runable))
                    runable=runable+1
                    
                    
                    motherviewclass=doc_newresult.createElement("motherviewclass")#、motherviewclass 表示是一个控件组
                    runableID.appendChild(motherviewclass)
                    textnode=doc_newresult.createTextNode(node.getAttribute("class"))
                    motherviewclass.appendChild(textnode)
                    
                    childviewclass=doc_newresult.createElement("childviewclass")
                    runableID.appendChild(childviewclass)
                    textnode=doc_newresult.createTextNode(child.getAttribute("class"))
                    childviewclass.appendChild(textnode)
                    
                    strlist=[]
                    getAllChildText(child, strlist)# get all its child's text into the strlist
                    
                    for item in strlist:
                        viewtext=doc_newresult.createElement("viewtext")
                        runableID.appendChild(viewtext)
                        textnode=doc_newresult.createTextNode(item)
                        viewtext.appendChild(textnode)
                        
                        alltextset.add(node.getAttribute("text"))#alltext
                    
                    #this is for source id
                    androidid=doc_newresult.createElement("androidid")
                    runableID.appendChild(androidid)
                    
                    ownid=doc_newresult.createElement("ownid")
                    androidid.appendChild(ownid)
                    textnode=doc_newresult.createTextNode(child.getAttribute("resource-id"))
                    ownid.appendChild(textnode)
                    
                    owntext=doc_newresult.createElement("owntext")
                    androidid.appendChild(owntext)
                    textnode=doc_newresult.createTextNode(child.getAttribute("resource-id"))
                    owntext.appendChild(textnode)
                    
                    #positions
                    bounds=child.getAttribute("bounds")
                    boundArray=re.findall(r'\d+',bounds)
                    
                    xvalue=(int(boundArray[0])+int(boundArray[2]))/2;
                    yvalue=(int(boundArray[1])+int(boundArray[3]))/2;            
                    
                    
                    #xposition
                    xposition=doc_newresult.createElement("xposition")
                    runableID.appendChild(xposition)
                    textnode=doc_newresult.createTextNode(str(xvalue))
                    xposition.appendChild(textnode)
                    
                    yposition=doc_newresult.createElement("yposition")
                    runableID.appendChild(yposition)
                    textnode=doc_newresult.createTextNode(str(yvalue))
                    yposition.appendChild(textnode)
                    
                    
                    #index
                    index=doc_newresult.createElement("index")
                    runableID.appendChild(index)
                    textnode=doc_newresult.createTextNode(child.getAttribute("index"))
                    index.appendChild(textnode)
                         
                         
                    clicktype=doc_newresult.createElement("clicktype")
                    runableID.appendChild(clicktype)
                    if node.getAttribute("long-clickable")=="false":
                        textnode=doc_newresult.createTextNode("short")
                        clicktype.appendChild(textnode)
                    else:
                        if classname!="android.widget.EditText":
                        ### for long
                            runableIDlong=copy.deepcopy(runableID)
                            step.appendChild(runableIDlong)
                            runableIDlong.setAttribute("id",str(runable))
                            runable=runable+1
    
                            clickTypeLong=runableIDlong.getElementsByTagName("clicktype") 
                            textnode=doc_newresult.createTextNode("long")
                            clickTypeLong[0].appendChild(textnode)
                        
                        
                        ################add the short
                        textnode=doc_newresult.createTextNode("short")
                        clicktype.appendChild(textnode)
                    
                continue #in this case, we do not to explore its child any more
                
                
                
                
            
            
        #从子节点向下深搜，继续迭代
        iterateTree(node, step, doc_newresult, alltextset, packageName)
    
    
    


def getAllChildText(child, strlist):
    
    if not child.getAttribute("content-desc")=="":
        strlist.append(child.getAttribute("content-desc"))
    
    
    strlist.append(child.getAttribute("text"))

    for subchild in child.childNodes:
        if subchild.nodeType == subchild.TEXT_NODE:
            continue
        
        getAllChildText(subchild, strlist)
            
        


def main():
    
    
    packageName="com.example.terin.asu_flashcardapp"
    
    
    #address="/home/yu/repeatbugreport"
    address=".."
    nlp = English()
    #model= Word2Vec.load('wiki.en.word2vec.model')#or yumodel
    #model= Word2Vec.load('yumodel')
    #model;

    #doc = nlp(u"VIDEOSq")

    #for token in doc:
    #    print(token, token.lemma, token.lemma_)
    #print pluralize('child')
#    aa=model.wv.similarity('movie', 'video')
    
    print("load finish")
    
    
    err2times=0
    while(1):
        
        
       
        
        '''
        if (os.path.exists('/home/yu/repeatbugreport/similarity.xml')):
            #################read the similarity.xml and pick the root############
            doc=minidom.parse('/home/yu/repeatbugreport/similarity.xml')
            root=doc.documentElement
        
        
        
            apples=nlp(u"good")
            orange=nlp(u"better")
    
            print(apples.similarity(orange))
            

            model= Word2Vec.load('yumodel')
            model.wv.similarity('refueling', 'refuel')

            
            #################write
            file_write = open("/home/yu/repeatbugreport/output/similarity.xml","wb")
            doc_write =Document()
        
            doc_write.appendChild(root)            
            doc_write.writexml(file_write)
            file_write.close()
        '''
        
        className=""
        if (os.path.exists(address+'/middleResults/result.xml')):
            time.sleep(0.5)
            ##################read the result.xml and pick the root###############           
            try:
                doc=minidom.parse(address+'/middleResults/result.xml')
                root=doc.documentElement
                
                fo = open(address+"/middleResults/packInfo", "rw+")
                strLine = fo.readline()
                className=strLine.split(" ")[-2]
                
                
                fo.close()
                
                

            except Exception as err:
                print("null file error : err")
                continue
            #######compute similarity#################################
            ###################
            ###########3
            ######3
            sentmap={}#key is the sentence id, value is a list of sentence string.
            
            file_sim = open(address+"/middleResults/output/similarity.xml","wb")
            doc_sim=Document()
            root_sim=doc_sim.createElement("Similarity")
            doc_sim.appendChild(root_sim)
            
            '''

            doc_sim.writexml(file_sim)
            file_sim.close()
            '''
            simid=0
            sentid=None
            
            ###########################first to transfer the allcases into sentmap##################

            #将所有事件映射和自然语言描述之间形成映射关系，这里涉及语义匹配
            docallsent=minidom.parse(address+'/middleResults/allcases.xml')
            rootallsent=docallsent.documentElement
            
            
            for sent in rootallsent.childNodes:
                if (sent.nodeType == minidom.Node.ELEMENT_NODE):##minidom is a little bit ugly
                    #sentid=str(-1)
                    for item in sent.childNodes:
                        if (item.nodeType == minidom.Node.ELEMENT_NODE):##minidom is a little bit ugly
                            
                            if(item.nodeName=="Sentid"):
                                sentid=item.firstChild.nodeValue
                                sentwordlist=list()
                                sentmap.update({sentid:sentwordlist})
                            
                                
                            if(item.nodeName=="sentence"):
                                for word in item.childNodes:
                                    if (word.nodeType == minidom.Node.ELEMENT_NODE):##minidom is a little bit ugly
                                        if word.hasChildNodes():
                                            sentmap.get(sentid).append(word.firstChild.nodeValue)
                                            
                            
                    
            ################################deal with 
            #for stepnode in root.childNodes:### this root is from result.xml
            #try:    ##it should be added in later
                
                #add 8.2.2018
            if True:    
                
                doc_newresult=Document()
                root_new=doc_newresult.createElement("Result")
                
                '''
                translate(root, root_new, doc_newresult)#translate from the xml from uiautomator.
                file_new = open(address+"/middleResults/output/resulttrans.xml","wb")
                doc_newresult.writexml(file_new)
                '''
                
                translate(root, root_new, doc_newresult, packageName, className)#translate from the xml from uiautomator.

                #将更新的执行序列输出到文件
                doc_write =Document()
                doc_write.appendChild(root_new)  
                with codecs.open(address+"/middleResults/output/resulttrans.xml","wb","utf-8") as out:
                    doc_write.writexml(out)
                
                
                out.close()
                 
                
                
                
                
                
                
                #语义匹配阶段
                model= Word2Vec.load('yumodel')

                stepnode=(root_new.childNodes)[-1] 
                
                
                if (stepnode.nodeType == minidom.Node.ELEMENT_NODE):##minidom is a little bit ugly

                    #遍历本次迭代节点的所有子节点
                    for functionode in stepnode.childNodes:
                        ###########alltext cases
                        if (functionode.nodeName =="AllText"):
                            for textnode in functionode.childNodes:
                                if (textnode.nodeType == minidom.Node.ELEMENT_NODE):##minidom is a little bit ugly
                                    try:
                                        text=textnode.firstChild.nodeValue
                                        
                                        sent=nlp(unicode(text))
                                    except Exception as err:
                                        continue

                                    #遍历句子里的词
                                    for word in sent:
                                        resultwordtext=word.lemma_
                                        
                                        keylist=sentmap.keys()## sentmap is from all sents
                                        for k in keylist:
                                            allsenttextlist=sentmap.get(k)
                                            
                                            for allsenttext in allsenttextlist:
                                            
                                                ### here should be added a exception
                                                #判断组件和描述中的名词是否语义匹配
                                                if (resultwordtext in model.wv.vocab) and (allsenttext in model.wv.vocab):
                
                                                    similarity=model.wv.similarity(resultwordtext, allsenttext)
                                                    '''
                                                    print(resultwordtext)
                                                    print(allsenttext)
                                                    print(similarity)
                                                    print("\n")
                                                    '''

                                                    #语义相符
                                                    if similarity>0.8:
                                                        onesimilarity=doc_sim.createElement("ID"+str(simid))
                                                        root_sim.appendChild(onesimilarity)
                                                        
                                                        sentid=doc_sim.createElement("SentenceID")
                                                        onesimilarity.appendChild(sentid)
                                                        textnode=doc_sim.createTextNode(k)
                                                        sentid.appendChild(textnode)
                                                        
                                                        sentword=doc_sim.createElement("SentenceWord")
                                                        onesimilarity.appendChild(sentword)
                                                        textnode=doc_sim.createTextNode(allsenttext)
                                                        sentword.appendChild(textnode)
                                                        
                                                        resultword=doc_sim.createElement("ResultWord")
                                                        onesimilarity.appendChild(resultword)
                                                        textnode=doc_sim.createTextNode(resultwordtext)
                                                        resultword.appendChild(textnode)
                                                        
                                                        
                                                                                                       
                
                                                        simid+=1
            try:
                a=1+1
            except Exception as err:
                if err2times<10:
                    err2times+=1
                    print("null file error : err2")
                    continue
                else:#creat a blank result and similarity
                    err2times=0
                    
                    docResultBlank = Document()
                    rootblank = docResultBlank.createElement('Result')
                    docResultBlank.appendChild(rootblank);
                    
                    rootblank.setAttribute("back", "false")
                    step1=docResultBlank.createElement("Step1");
                    step2=docResultBlank.createElement("Step2");
                    rootblank.appendChild(step1)
                    rootblank.appendChild(step2)
                    
                    Classname=docResultBlank.createElement('Classname')
                    text=docResultBlank.createTextNode("error may be crashed")
                    Classname.appendChild(text)
                    
                    ViewGroup=docResultBlank.createElement('ViewGroup')
                    NoGroup=docResultBlank.createElement('NoGroup')
                    Easyoperate=docResultBlank.createElement('Easyoperate')
                    AllText=docResultBlank.createElement('AllText')
                    
                    step1.appendChild(copy.deepcopy(Classname))
                    step1.appendChild(copy.deepcopy(ViewGroup))
                    step1.appendChild(copy.deepcopy(NoGroup))
                    step1.appendChild(copy.deepcopy(Easyoperate))
                    step1.appendChild(copy.deepcopy(AllText))
                    
                    step2.appendChild(copy.deepcopy(Classname))
                    step2.appendChild(copy.deepcopy(ViewGroup))
                    step2.appendChild(copy.deepcopy(NoGroup))
                    step2.appendChild(copy.deepcopy(Easyoperate))
                    step2.appendChild(copy.deepcopy(AllText))
                    #rootblank=
                    #rootblank
                     
                    with codecs.open(address+"/middleResults/output/result.xml","wb","utf-8") as out:
                        docResultBlank.writexml(out)
            
                    out.close()        
                    
                    os.remove(address+'/middleResults/result.xml')
                    
                    doc_sim.writexml(file_sim)
                    file_sim.close()
                    #shutil.copy(address+'/middleResults/output/resultcopy.xml',address+'/middleResults/output/result.xml');
                    #shutil.copy(address+'/middleResults/output/similaritycopy.xml',address+'/middleResults/output/similarity.xml');

                    continue
            doc_sim.writexml(file_sim)
            file_sim.close()
            ##################similarity end##########
            ###############
            ########
            ###                            
                                        
                                        
                                         
                                
                                

            
            ##################write the result.xml in output######################
            #file_write = open("/home/yu/repeatbugreport/middleResults/output/result.xml","wb")

            #将每个子节点添加到动态有序事件树里
            for stepnode in root_new.childNodes:
                addnlptotext(doc,nlp,stepnode)
            #生成新的result文件
            doc_write =Document()
            doc_write.appendChild(root_new)  
            with codecs.open(address+"/middleResults/output/result.xml","wb","utf-8") as out:
                doc_write.writexml(out)
            
            
            out.close()
            '''
            file_write = open("/home/yu/repeatbugreport/middleResults/output/result.xml","wb")
            doc_write =Document()
            
            
            ###################process on all element end with task
            for stepnode in root.childNodes:
                addnlptotext(doc,nlp,stepnode)
            
            
            ##################write the result.xml in output######################
            doc_write.appendChild(root)            
            doc_write.writexml(file_write)
            file_write.close()
            '''



            ####################remove the orignal file#################################
            os.remove(address+'/middleResults/result.xml')#原序列删除是很必要的，会干扰下轮迭代的执行
            
            
            
        time.sleep(1)
    
if __name__ == '__main__':
    main()         

    