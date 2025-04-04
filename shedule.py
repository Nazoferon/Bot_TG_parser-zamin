from bs4 import BeautifulSoup as bs
import requests

class Shedule:
    mainurl = "http://rcnubip.org.ua/studentu/zmini-do-rozkladu/"
    index : bs
    lines : bs
    filemode = False
    def __init__(self, url = None, filemode = False):
        self.filemode = filemode
        if url: self.mainurl = url
        self.update()

    def update(self):
        if not self.filemode:
            self.index = bs(requests.get(self.mainurl).text, 'html.parser')
        else:
            self.index = bs(open(self.mainurl, "r", encoding="utf-8").read(), 'html.parser')
        self.lines = self.index.find("table").find_all("tr")

    def getGroupsChanges(self, groups):
        if type(groups) is list:
            for group in groups:
                if not self.checkGroupName(group):
                    return {"error": f"Помилка в назві групи '{group}'"}
        else:
            if not self.checkGroupName(groups):
                return {"error": f"Помилка в назві групи '{groups}'"}
        changes = {}
        if type(groups) is list:
            for group in groups:
                changes[group] = self.groupChanges(group)
        else:
            changes[groups] = self.groupChanges(groups)
        return changes

    def checkGroupName(self, gname):
        if len(gname) < 4 or gname[2] != "-" or not (gname[0].isdigit() and gname[1].isdigit()):
            return False
        return True

    def groupChanges(self, gname):
        flag = -1
        changes = []
        for tr in self.lines:
            if len(tr) == 6:
                if flag != -1:
                    if tr.contents[flag].p.text != "\xa0" or tr.contents[flag+1].p.text == "\xa0" or tr.contents[flag+2].p.text == "\xa0":
                        break
                    changes.append({"num": str(tr.contents[flag+1].p.text), "name": tr.contents[flag+2].p.text})
                else:
                    if tr.contents[0].p.text != "\xa0":
                        if tr.contents[0].p.text.replace(" ", "") == gname:
                            flag = 0
                            changes.append({"num": str(tr.contents[flag+1].p.text), "name": tr.contents[flag+2].p.text})
                    if tr.contents[3].p.text != "\xa0":
                        if tr.contents[3].p.text.replace(" ", "") == gname:
                            flag = 3
                            changes.append({"num": str(tr.contents[flag+1].p.text), "name": tr.contents[flag+2].p.text})
        return changes

