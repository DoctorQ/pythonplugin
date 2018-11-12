import sys
from PluginManager import PluginManager
from PluginManager import __ALLMODEL__

if __name__ == '__main__':
    PluginManager.LoadAllPlugin()

    for SingleModel in __ALLMODEL__:
        plugins = SingleModel.GetPluginObject()
        for item in plugins:
            item.Start()


    pluginName = 'plugin1.Plugin2'
    obj = PluginManager.GetPluginByName(pluginName)
    if obj:
        obj.Start()
    else:
        print 'plugin[%s] is not exists'%pluginName
