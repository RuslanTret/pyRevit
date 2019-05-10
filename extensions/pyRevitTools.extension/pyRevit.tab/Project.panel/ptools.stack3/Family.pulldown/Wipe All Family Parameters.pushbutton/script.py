"""This script removes all custom parameters from family."""
#pylint: disable=E0401
from pyrevit import revit, DB, UI
from pyrevit import script
from pyrevit import forms


logger = script.get_logger()
output = script.get_output()

# make sure they know what they are doing
res = \
    forms.alert('Make sure your models are saved and synced. '
                'Hit OK to continue...', cancel=True, exitscript=True)

# ensure document is a family
forms.check_familydoc(doc=revit.doc, exitscript=True)

params = revit.doc.FamilyManager.GetParameters()
dims = DB.FilteredElementCollector(revit.doc)\
            .OfClass(DB.Dimension)\
            .WhereElementIsNotElementType()

# collect all used params
# on dims
labelParams = set()
for d in dims:
    try:
        if isinstance(d.FamilyLabel, DB.FamilyParameter):
            labelParams.add(d.FamilyLabel.Id.IntegerValue)
    except Exception:
        continue

with revit.TransactionGroup('Remove all family parameters'):
    total_params = len(params)
    output.update_progress(0, total_params)
    for idx, param in enumerate(params):
        # if param is builtin, id is < 0
        if param.Id.IntegerValue > 0:
            try:
                print('\nRemoving Family Parameter:\nId: {}\tName: {}'
                    .format(param.Id, param.Definition.Name))
                with revit.Transaction('Remove parameter', log_errors=False):
                    revit.doc.FamilyManager.RemoveParameter(param)
            except Exception:
                logger.error("Can not delete: %s", param.Definition.Name)
        
        output.update_progress(idx + 1, total_params)