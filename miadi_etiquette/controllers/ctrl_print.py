# -*- coding: utf-8 -*-

from odoo import models,fields,api
#from . import models,wizards
import os, sys
#import win32print


def printlabelonwindows(printer,labelmodelfile,charSep,parameters):
    
    
    
    contenu = "";
    with open(labelmodelfile) as fichierEtiq:
        for line in fichierEtiq:
            contenu += line + "\r\n"
    
    for paramName,value in parameters:
                
        if contenu.find(charSep + paramName.lower() + charSep) != -1:
            contenu = contenu.replace(charSep + paramName.lower() + charSep, value)
        
    #print(sys.version_info)    
      
    if sys.version_info >= (3,):
        raw_data = bytes(contenu,"utf-8")
    else:
        raw_data = contenu
      
      
    #Odoo sh
    #connection = cups.Connection(host="82.127.121.129", port="631")
    #connection.printFile("GK420t",
    #                     "/home/odoo/user/src/hubi/label/Etiq_Base.txt",
    #                     "/home/odoo/user/src/hubi/label/Etiq_Base.txt",
    #                    {})
    
    
    #Windows
    #hPrinter = win32print.OpenPrinter (printer)
    #try:
    #    hJob = win32print.StartDocPrinter(hPrinter, 1, ("print", None, "RAW"))
    #    try:
    #        win32print.StartPagePrinter (hPrinter)
    #        win32print.WritePrinter (hPrinter, raw_data)
    #        win32print.EndPagePrinter (hPrinter)
    #    finally:
    #        win32print.EndDocPrinter (hPrinter)
    #finally:
    #    win32print.ClosePrinter (hPrinter)

def callFonction(self):
    return