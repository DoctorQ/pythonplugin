import os
import sys
from imp import find_module
from imp import load_module
class PluginManager(type):
    __PluginPath = 'Plugins'

    def __init__(self,name,bases,dict):
        if not hasattr(self,'AllPlugins'):
            self.__AllPlugins = {}
        else:
            self.RegisterAllPlugin(self)


    @staticmethod
    def SetPluginPath(path):
        if os.path.isdir(path):
            PluginManager.__PluginPath = path
        else:
            print '%s is not a valid path'%path



    @staticmethod
    def LoadAllPlugin():
        pluginPath = PluginManager.__PluginPath
        if not os.path.isdir(pluginPath):
            raise EnvironmentError,'%s is not a directory'%pluginPath
        items = os.listdir(pluginPath)
        for item in items:
            if os.path.isdir(os.path.join(pluginPath,item)):
                PluginManager.__PluginPath = os.path.join(pluginPath,item)
                PluginManager.LoadAllPlugin()
            else:
                if item.endswith('.py') and item != '__init__.py':
                    moduleName = item[:-3]
                    if moduleName not in sys.modules:
                        fileHandle,filePath,dect = find_module(moduleName,[pluginPath])
                    try:
                        moduleObj = load_module(moduleName,fileHandle,filePath,dect)
                    finally:
                        if fileHandle : fileHandle.close() 


    @property
    def AllPlugins(self):
        return self.__AllPlugins

    def RegisterAllPlugin(self,aPlugin):
        pluginName = '.'.join([aPlugin.__module__,aPlugin.__name__])
        pluginObj = aPlugin()
        #print 'plugin name is %s'%pluginName
        self.__AllPlugins[pluginName] = pluginObj


    def UnregisterPlugin(self,pluginName):
        if pluginName in self.__AllPlugins:
            pluginObj = self.__AllPlugins[pluginName]
            del pluginObj



    def GetPluginObject(self,pluginName = None):
        if pluginName is None:
            return self.__AllPlugins.values()
        else:
            result = self.__AllPlugins[pluginName] if pluginName in self.__AllPlugins else None
            return result
    @staticmethod
    def GetPluginByName(pluginName):
        if pluginName is None:
            return None
        else:
            for SingleModel in __ALLMODEL__:
                plugin = SingleModel.GetPluginObject(pluginName)
                if plugin:
                    return plugin



class Model_Component(object):
    __metaclass__ = PluginManager

    def Start(self):
        print 'Please write the Start() function'

    def ChangeLanguage(self,language):
        print 'Please write the ChangeLanguage() function'

class Model_MenuObj(object):
    __metaclass__ = PluginManager

    def Start(self):
        print 'Please write the Start() function'

    def ChangeLanguage(self,language):
        print 'Please write the ChangeLanguage() function'

class Model_ToolBarObj(object):
    __metaclass__ = PluginManager

    def Start(self):
        print 'Please write the Start() function'

    def ChangeLanguage(self,language):
        print 'Please write the ChangeLanguage() function'

class Model_ParamPanelObj(object):
    __metaclass__ = PluginManager

    def Start(self):
        print 'Please write the Start() function'

    def ChangeLanguage(self,language):
        print 'Please write the ChangeLanguage() function'

__ALLMODEL__ = (Model_ParamPanelObj,Model_ToolBarObj,Model_MenuObj,Model_Component)
