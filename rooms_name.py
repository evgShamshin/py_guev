import clr

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

def group_by_par_val(rooms, par_name):
    groups_dict = dict()
    for room in rooms:
        room_id = room.Id
        key = room.LookupParameter(par_name).AsString()

        if key not in groups_dict:
            groups_dict.update({key: [room]})
        else:
            groups_dict[key].append(room)
    return groups_dict


fec = FilteredElementCollector(doc)
fec.OfCategory(BuiltInCategory.OST_Rooms)
rooms = fec.ToElements()

groups_dict = group_by_par_val(rooms, IN[0])

TransactionManager.Instance.EnsureInTransaction(doc)

res = list()
for group in groups_dict.values():
    par_val = []
    for room in group:
        par_val.append(room.Number)
    par_val_str = ", ".join(str(par_val))

    for room in group:
        par = room.LookupParameter(IN[1])
        par.Set(par_val_str)
        res.append(room.LookupParameter(IN[1]).AsString())

TransactionManager.Instance.TransactionTaskDone()

OUT = res