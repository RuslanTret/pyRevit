"""This script removes all custom "unused" parameters from family."""
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

# grab params, dimensions and other elements
params = revit.doc.FamilyManager.GetParameters()
dims = DB.FilteredElementCollector(revit.doc)\
            .OfClass(DB.Dimension)\
            .WhereElementIsNotElementType()

allelements = DB.FilteredElementCollector(revit.doc)\
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

# wired to elements
visibParams = set()
for el in allelements:
    try:
        visible_param = el.Parameter[DB.BuiltInParameter.IS_VISIBLE_PARAM]
        if visible_param is not None:
            famvisibparam = \
                revit.doc.FamilyManager.GetAssociatedFamilyParameter(
                    visible_param
                    )

            if famvisibparam is not None \
                    and isinstance(famvisibparam, DB.FamilyParameter):
                visibParams.add(famvisibparam.Id.IntegerValue)
    except Exception:
        continue

with revit.TransactionGroup('Remove all family parameters'):
    total_params = len(params)
    output.update_progress(0, total_params)
    for idx, param in enumerate(params):
        # if param is builtin, id is < 0
        if param.Id.IntegerValue > 0:
            try:
                if param.Id.IntegerValue not in labelParams \
                        and param.Id.IntegerValue not in visibParams:
                    print('\nRemoving Family Parameter:\nId: {}\tName: {}'
                        .format(param.Id, param.Definition.Name))
                    with revit.Transaction('Remove parameter', log_errors=False):
                        revit.doc.FamilyManager.RemoveParameter(param)
                else:
                    print('\nSkipping Used Family Parameter:\nId: {}\tName: {}'
                        .format(param.Id, param.Definition.Name))
            except Exception:
                logger.error("Can not delete: %s", param.Definition.Name)
                # if param.StorageType == DB.StorageType.String:
                #     with revit.Transaction('Reset string parameter'):
                #         revit.doc.FamilyManager.Set(param, '')
            
        output.update_progress(idx + 1, total_params)
