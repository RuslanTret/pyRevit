"""Base module for handling extensions parsing."""
from collections import namedtuple

from pyrevit import HOST_APP, EXEC_PARAMS

# Extension types
# ------------------------------------------------------------------------------

ExtensionType = namedtuple('ExtensionType', ['ID', 'POSTFIX'])


class ExtensionTypes:
    UI_EXTENSION = ExtensionType(ID='extension', POSTFIX='.extension')
    LIB_EXTENSION = ExtensionType(ID='lib', POSTFIX='.lib')
    RUN_EXTENSION = ExtensionType(ID='run', POSTFIX='.run')
    THEME_EXTENSION = ExtensionType(ID='theme', POSTFIX='.theme')

    @classmethod
    def get_ext_types(cls):
        ext_types = set()
        for attr in dir(cls):
            if attr.endswith('_EXTENSION'):
                ext_types.add(getattr(cls, attr))
        return ext_types

    @classmethod
    def is_cli_ext(cls, ext_type):
        """Check if this is a pyRevit CLI extension."""
        return ext_type == cls.RUN_EXTENSION

    @classmethod
    def is_theme_ext(cls, ext_type):
        """Check if this is a pyRevit theme extension."""
        return ext_type == cls.THEME_EXTENSION

# bundle files
PYTHON_SCRIPT_FILE_FORMAT = '.py'
CSHARP_SCRIPT_FILE_FORMAT = '.cs'
VB_SCRIPT_FILE_FORMAT = '.vb'
RUBY_SCRIPT_FILE_FORMAT = '.rb'
DYNAMO_SCRIPT_FILE_FORMAT = '.dyn'
YAML_FILE_FORMAT = '.yaml'
JSON_FILE_FORMAT = '.json'

# extension manifest file
EXT_MANIFEST_NAME = 'extension'
EXT_MANIFEST_TEMPLATES_KEY = 'templates'
EXT_MANIFEST_FILE = EXT_MANIFEST_NAME + JSON_FILE_FORMAT

# extension startup file
EXT_STARTUP_NAME = 'startup'
EXT_STARTUP_FILE = EXT_STARTUP_NAME + PYTHON_SCRIPT_FILE_FORMAT

# bundle types
TAB_POSTFIX = '.tab'
PANEL_POSTFIX = '.panel'
LINK_BUTTON_POSTFIX = '.linkbutton'
PUSH_BUTTON_POSTFIX = '.pushbutton'
TOGGLE_BUTTON_POSTFIX = '.toggle'
SMART_BUTTON_POSTFIX = '.smartbutton'
PULLDOWN_BUTTON_POSTFIX = '.pulldown'
STACKTHREE_BUTTON_POSTFIX = '.stack3'
STACKTWO_BUTTON_POSTFIX = '.stack2'
SPLIT_BUTTON_POSTFIX = '.splitbutton'
SPLITPUSH_BUTTON_POSTFIX = '.splitpushbutton'
PANEL_PUSH_BUTTON_POSTFIX = '.panelbutton'
NOGUI_COMMAND_POSTFIX = '.nobutton'

# Component layout elements
DEFAULT_LAYOUT_FILE_NAME = '_layout'
SEPARATOR_IDENTIFIER = '---'
SLIDEOUT_IDENTIFIER = '>>>'

# Component icon
ICON_FILE_FORMAT = '.png'

DEFAULT_ICON_FILE = 'icon' + ICON_FILE_FORMAT
DEFAULT_ON_ICON_FILE = 'on' + ICON_FILE_FORMAT
DEFAULT_OFF_ICON_FILE = 'off' + ICON_FILE_FORMAT

# Component image for tooltips
DEFAULT_TOOLTIP_IMAGE_FILE = 'tooltip.png'
# Component video for tooltips
DEFAULT_TOOLTIP_VIDEO_FILE = 'tooltip.swf'
if not EXEC_PARAMS.doc_mode and HOST_APP.is_newer_than(2019, or_equal=True):
    DEFAULT_TOOLTIP_VIDEO_FILE = 'tooltip.mp4'


# unique ids
UNIQUE_ID_SEPARATOR = '-'

# Command supported languages
PYTHON_LANG = 'python'
CSHARP_LANG = 'csharp'
VB_LANG = 'visualbasic'
DYNAMO_LANG = 'dynamobim'

# Component scripts
DEFAULT_SCRIPT_NAME = 'script'
DEFAULT_CONFIG_NAME = 'config'

# Hash file for caching directory state hash value
EXTENSION_HASH_CACHE_FILENAME = 'ext_hash'

# script files
PYTHON_SCRIPT_POSTFIX = DEFAULT_SCRIPT_NAME + PYTHON_SCRIPT_FILE_FORMAT
CSHARP_SCRIPT_POSTFIX = DEFAULT_SCRIPT_NAME + CSHARP_SCRIPT_FILE_FORMAT
VB_SCRIPT_POSTFIX = DEFAULT_SCRIPT_NAME + VB_SCRIPT_FILE_FORMAT
RUBY_SCRIPT_POSTFIX = DEFAULT_SCRIPT_NAME + RUBY_SCRIPT_FILE_FORMAT
DYNAMO_SCRIPT_POSTFIX = DEFAULT_SCRIPT_NAME + DYNAMO_SCRIPT_FILE_FORMAT
CONFIG_SCRIPT_POSTFIX = DEFAULT_CONFIG_NAME + PYTHON_SCRIPT_FILE_FORMAT

# Command component defaults
UI_TITLE_PARAM = '__title__'
DOCSTRING_PARAM = '__doc__'
AUTHOR_PARAM = '__author__'

COMMAND_HELP_URL = '__helpurl__'
COMMAND_CONTEXT_PARAM = '__context__'
MIN_REVIT_VERSION_PARAM = '__min_revit_ver__'
MAX_REVIT_VERSION_PARAM = '__max_revit_ver__'
SHIFT_CLICK_PARAM = '__shiftclick__'
BETA_SCRIPT_PARAM = '__beta__'

LINK_BUTTON_ASSEMBLY_PARAM = '__assembly__'
LINK_BUTTON_COMMAND_CLASS_PARAM = '__commandclass__'

CLEAN_ENGINE_SCRIPT_PARAM = '__cleanengine__'
FULLFRAME_ENGINE_PARAM = '__fullframeengine__'
PERSISTENT_ENGINE_PARAM = '__persistentengine__'

COMMAND_AVAILABILITY_NAME_POSTFIX = 'Availab'
COMP_LIBRARY_DIR_NAME = 'lib'

CTX_SELETION = 'selection'
CTX_ZERODOC = ['zero-doc', 'zerodoc']
