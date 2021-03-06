#Definition of inputs and outputs
#==================================
##BC=group
##PG04_WaterQualityParameters_02_C2RCC=name
##ParameterNumber|AverageSalinity|Average Salinity|0|None|1.0
##ParameterNumber|AverageTemperature|Average Temperature|0|None|15.0
##ParameterString|validExpression|Valid pixel expression|not quality_flags.invalid and (not pixel_classif_flags.IDEPIX_LAND or quality_flags.fresh_inland_water) and not (pixel_classif_flags.IDEPIX_CLOUD or pixel_classif_flags.IDEPIX_CLOUD_BUFFER)
#ParameterNumber|Vic01|Vicarious gains for Oa01|0|None|1.0206
#ParameterNumber|Vic02|Vicarious gains for Oa02|0|None|1.0290
#ParameterNumber|Vic03|Vicarious gains for Oa03|0|None|1.0260
#ParameterNumber|Vic04|Vicarious gains for Oa04|0|None|1.0224
#ParameterNumber|Vic05|Vicarious gains for Oa05|0|None|1.0176
#ParameterNumber|Vic06|Vicarious gains for Oa06|0|None|1.0110
#ParameterNumber|Vic07|Vicarious gains for Oa07|0|None|1.0079
#ParameterNumber|Vic08|Vicarious gains for Oa08|0|None|1.0081
#ParameterNumber|Vic09|Vicarious gains for Oa09|0|None|1.0057
#ParameterNumber|Vic10|Vicarious gains for Oa10|0|None|1.0038
#ParameterNumber|Vic11|Vicarious gains for Oa11|0|None|1.0040
#ParameterNumber|Vic12|Vicarious gains for Oa12|0|None|0.9970
#ParameterNumber|Vic13|Vicarious gains for Oa13|0|None|1.0000
#ParameterNumber|Vic14|Vicarious gains for Oa14|0|None|1.0000
#ParameterNumber|Vic15|Vicarious gains for Oa15|0|None|1.0000
#ParameterNumber|Vic16|Vicarious gains for Oa16|0|None|0.9950
#ParameterNumber|Vic17|Vicarious gains for Oa17|0|None|1.0000
#ParameterNumber|Vic18|Vicarious gains for Oa18|0|None|1.0040
#ParameterNumber|Vic19|Vicarious gains for Oa19|0|None|1.0000
#ParameterNumber|Vic20|Vicarious gains for Oa20|0|None|1.0000
#ParameterNumber|Vic21|Vicarious gains for Oa21|0|None|1.0941


import os
import glob
import tempfile

tempfolder = 'wq_scripts_'
Vic01 = 1.0206
Vic02 = 1.0290
Vic03 = 1.0260
Vic04 = 1.0224
Vic05 = 1.0176
Vic06 = 1.0110
Vic07 = 1.0079
Vic08 = 1.0081
Vic09 = 1.0057
Vic10 = 1.0038
Vic11 = 1.0040
Vic12 = 0.9970
Vic13 = 1.0000
Vic14 = 1.0000
Vic15 = 1.0000
Vic16 = 0.9950
Vic17 = 1.0000
Vic18 = 1.0040
Vic19 = 1.0000
Vic20 = 1.0000
Vic21 = 1.0941

def folder_check(tempfolder):
    try:
        tempdir = glob.glob(os.path.join(tempfile.gettempdir(), tempfolder + '*'))[0]
        return False
    except IndexError:
        progress.setConsoleInfo('ERROR: Parameter folder could not be found. Please execute step 1 first!')
        return True
        
def convert(AverageSalinity, AverageTemperature):
    AverageSalinityS = '%.2f' % AverageSalinity
    AverageTemperatureS = '%.2f' % AverageTemperature
    
    return AverageSalinityS, AverageTemperatureS

def create_parameterfile(tempdir, AverageSalinityS, AverageTemperatureS, validExpression, Vic01, Vic02, Vic03, Vic04, Vic05, Vic06, Vic07, Vic08, Vic09, Vic10, Vic11, Vic12, Vic13, Vic14, Vic15, Vic16, Vic17, Vic18, Vic19, Vic20, Vic21):
    with open(tempdir + "WaterQualityParametersOLCI02.txt", "w") as text_file:
        text_file.write('averageSalinity='+ AverageSalinityS + '\n') 
        text_file.write('averageTemperature='+ AverageTemperatureS + '\n')
        text_file.write('c2ValidExpression='+ validExpression + '\n')
        text_file.write('Oa01_vic='+ str(Vic01) + '\n')
        text_file.write('Oa02_vic='+ str(Vic02) + '\n')
        text_file.write('Oa03_vic='+ str(Vic03) + '\n')
        text_file.write('Oa04_vic='+ str(Vic04) + '\n')
        text_file.write('Oa05_vic='+ str(Vic05) + '\n')
        text_file.write('Oa06_vic='+ str(Vic06) + '\n')
        text_file.write('Oa07_vic='+ str(Vic07) + '\n')
        text_file.write('Oa08_vic='+ str(Vic08) + '\n')
        text_file.write('Oa09_vic='+ str(Vic09) + '\n')
        text_file.write('Oa10_vic='+ str(Vic10) + '\n')
        text_file.write('Oa11_vic='+ str(Vic11) + '\n')
        text_file.write('Oa12_vic='+ str(Vic12) + '\n')
        text_file.write('Oa13_vic='+ str(Vic13) + '\n')
        text_file.write('Oa14_vic='+ str(Vic14) + '\n')
        text_file.write('Oa15_vic='+ str(Vic15) + '\n')
        text_file.write('Oa16_vic='+ str(Vic16) + '\n')
        text_file.write('Oa17_vic='+ str(Vic17) + '\n')
        text_file.write('Oa18_vic='+ str(Vic18) + '\n')
        text_file.write('Oa19_vic='+ str(Vic19) + '\n')
        text_file.write('Oa20_vic='+ str(Vic20) + '\n')
        text_file.write('Oa21_vic='+ str(Vic21) + '\n')


def execution(tempfolder):
    if folder_check(tempfolder):
        return
    else:
        tempdir = glob.glob(os.path.join(tempfile.gettempdir(), tempfolder + '*'))[0] + '/'
        AverageSalinityS, AverageTemperatureS = convert(AverageSalinity, AverageTemperature)
        create_parameterfile(tempdir, AverageSalinityS, AverageTemperatureS, validExpression, Vic01, Vic02, Vic03, Vic04, Vic05, Vic06, Vic07, Vic08, Vic09, Vic10, Vic11, Vic12, Vic13, Vic14, Vic15, Vic16, Vic17, Vic18, Vic19, Vic20, Vic21)

execution(tempfolder)