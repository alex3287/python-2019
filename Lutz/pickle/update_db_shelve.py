from initdata import tom
import shelve

db = shelve.open('people-shelve')
# sue = db['sue']
# sue['pay'] *= 1.5
# db['sue'] = sue
# db['tom'] = tom
del(db['Bill'])
db.close()