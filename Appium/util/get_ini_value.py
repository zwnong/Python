# coding = utf-8
import sys
sys.path.append('D:\git\Python\Appium')
from util.read_ini import ReadIni

class GetIniValue:
    
    def __init__(self,driver):
        self.driver = driver
        
    def get_ini_element(self,key):
        read_ini = ReadIni()
        value = read_ini.get_value(key)
        by = value.split('>')[0]
        value_by = value.split('>')[0]
        
        if value != None:
            if by == 'id':
                return self.driver.find_element_by_id(value_by)
            
            elif by == 'className':
                return self.driver.find_element_by_class_name(value_by)
            
            else:
                return None
        

if __name__ == '__main__':
    value = GetIniValue()
    value.get_ini_value('FlymeAccount')
