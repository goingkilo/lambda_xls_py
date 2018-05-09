import json
import xlrd

def handle( filename, tabname):
    try :
        workbook = xlrd.open_workbook( filename)
        worksheet = workbook.sheet_by_name( tabname)
    except Exception as e:
        return "Processing of File :{0} , Tab :{1}  : failed due to followng reason : {2}".format( filename, tabname, e)

    l = []
    keys = [x.value for x in worksheet.row(0)]
    for i in range( worksheet.nrows):
        # skip the headers
        if i == 0:
            continue
    
        values = [x.value for x in worksheet.row(i)]
        if not len(keys) == len(values):
            print( 'Mismatch : row ', i)
        dictionary = dict( zip( keys, values))
        l.append( dictionary)
    ret = json.dumps( l, indent=4)
    return ret



