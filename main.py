from ms_sqlserver import DbAccessor
import bom

instance = "DESKTOP-8B0KCU1\\SQLEXPRESS"
user = "python"
password = "python"
db = "KGWS"

sql = '''select *
           from bom where parts_number = ?  or  parts_number = ?'''
parameter = (100, 101)

tmp = DbAccessor(instance, db, user, password)
res = tmp.query_df(sql, parameter)
print(res)
sql = """update bom set parts_number = 10 """
parameter = None

res = tmp.execute(sql, parameter)
print(res)

tmp = bom.Bom("a", "b")
print(tmp.partsname)
print(tmp.partsnumber)
