clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

PAR_KEY_NAME = "ADSK_Тип помещения"
PAR_OUT_NAME = "ADSK_Этаж"

fec = FilteredElementCollector(doc)
fec.OfCategory(BuiltInCategory.OST_Rooms)
rooms = fec.ToElements()

groups_dict = dict()

res = list()
for room in rooms:
    room_id = room.Id
    key = room.LookupParameter(PAR_KEY_NAME).AsValueString()

    if key not in groups_dict:
        groups_dict.update({key: [room]})
    else:
        groups_dict[key].append(room)

TransactionManager.Instance.EnsureInTransaction(doc)

res = list()
for group in groups_dict.values():
    par_val = []
    for room in group:
        par_val.append(room.Number)
    par_val_str = ", ".join(str(par_val))

    for room in group:
        par = room.LookupParameter(PAR_KEY_NAME)
        par.Set(PAR_OUT_NAME)
        res.append(room.LookupParameter(PAR_OUT_NAME).AsString())

TransactionManager.Instance.TransactionTaskDone()

OUT = res