import xlrd
import json

import xls_processor

filename = 'data/ISO10383_MIC.xls'
tabname = 'MICs List by CC'


def test_input_is_xls():
    workbook = xlrd.open_workbook(filename)
    assert(True)


def test_input_is_not_xls():
    try:
        workbook = xlrd.open_workbook('data/dummy.xls')
        assert False
    except Exception, e:
        assert True
        #assert e.message  == 'File size is 0 bytes'


def test_input_is_not_valid_file():
    try:
        workbook = xlrd.open_workbook('file_does_not_exit.xls')
        assert False
    except Exception, e:
        assert True
        #assert e.message  == 'No such file or directory'


def test_tab_exists():
    workbook = xlrd.open_workbook(filename)
    worksheet = workbook.sheet_by_name(tabname)
    assert(True)
    try:
        worksheet = workbook.sheet_by_name('does_not_exist')
    except Exception, e:
        assert True


def test_extract():
    a = xls_processor.handle(filename, tabname)
    assert type(a) == type('str')
    assert type(json.loads(a)) == type([])
    assert type(json.loads(a)[0]) == type({})
