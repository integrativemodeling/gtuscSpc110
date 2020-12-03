import cPickle, base64
try:
	from SimpleSession.versions.v65 import beginRestore,\
	    registerAfterModelsCB, reportRestoreError, checkVersion
except ImportError:
	from chimera import UserError
	raise UserError('Cannot open session that was saved in a'
	    ' newer version of Chimera; update your version')
checkVersion([1, 14, 42094])
import chimera
from chimera import replyobj
replyobj.status('Restoring session...', \
    blankAfter=0)
replyobj.status('Beginning session restore...', \
    blankAfter=0, secondary=True)
beginRestore()

def restoreCoreModels():
	from SimpleSession.versions.v65 import init, restoreViewer, \
	     restoreMolecules, restoreColors, restoreSurfaces, \
	     restoreVRML, restorePseudoBondGroups, restoreModelAssociations
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwBOfYdVCWJhbGxTY2FsZXEDSwBOfYdVCXBvaW50U2l6ZXEESwBOfYdVBWNvbG9ycQVLAE59h1UKcmliYm9uVHlwZXEGSwBOfYdVCnN0aWNrU2NhbGVxB0sATn2HVQxtbUNJRkhlYWRlcnNxCF1VDGFyb21hdGljTW9kZXEJSwBOfYdVCnZkd0RlbnNpdHlxCksATn2HVQZoaWRkZW5xC0sATn2HVQ1hcm9tYXRpY0NvbG9ycQxLAE59h1UPcmliYm9uU21vb3RoaW5ncQ1LAE59h1UJYXV0b2NoYWlucQ5LAE59h1UKcGRiVmVyc2lvbnEPSwBOfYdVCG9wdGlvbmFscRB9VQ9sb3dlckNhc2VDaGFpbnNxEUsATn2HVQlsaW5lV2lkdGhxEksATn2HVQ9yZXNpZHVlTGFiZWxQb3NxE0sATn2HVQRuYW1lcRRLAE59h1UPYXJvbWF0aWNEaXNwbGF5cRVLAE59h1UPcmliYm9uU3RpZmZuZXNzcRZLAE59h1UKcGRiSGVhZGVyc3EXXVUDaWRzcRhLAE59h1UOc3VyZmFjZU9wYWNpdHlxGUsATn2HVRBhcm9tYXRpY0xpbmVUeXBlcRpLAE59h1UUcmliYm9uSGlkZXNNYWluY2hhaW5xG0sATn2HVQdkaXNwbGF5cRxLAE59h3Uu'))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksATn2HVQtmaWxsRGlzcGxheXEDSwBOfYdVBG5hbWVxBEsATn2HVQVjaGFpbnEFSwBOfYdVDnJpYmJvbkRyYXdNb2RlcQZLAE59h1UCc3NxB0sATn2HVQhtb2xlY3VsZXEISwBOfYdVC3JpYmJvbkNvbG9ycQlLAE59h1UFbGFiZWxxCksATn2HVQpsYWJlbENvbG9ycQtLAE59h1UIZmlsbE1vZGVxDEsATn2HVQVpc0hldHENSwBOfYdVC2xhYmVsT2Zmc2V0cQ5LAE59h1UIcG9zaXRpb25xD11VDXJpYmJvbkRpc3BsYXlxEEsATn2HVQhvcHRpb25hbHERfVUEc3NJZHESSwBOfYd1Lg=='))
	atomInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQdyZXNpZHVlcQJLAE59h1UIdmR3Q29sb3JxA0sATn2HVQRuYW1lcQRLAE59h1UDdmR3cQVLAE59h1UOc3VyZmFjZURpc3BsYXlxBksATn2HVQVjb2xvcnEHSwBOfYdVCWlkYXRtVHlwZXEISwBOfYdVBmFsdExvY3EJSwBOfYdVBWxhYmVscQpLAE59h1UOc3VyZmFjZU9wYWNpdHlxC0sATn2HVQdlbGVtZW50cQxLAE59h1UKbGFiZWxDb2xvcnENSwBOfYdVDHN1cmZhY2VDb2xvcnEOSwBOfYdVD3N1cmZhY2VDYXRlZ29yeXEPSwBOfYdVBnJhZGl1c3EQSwBOfYdVCmNvb3JkSW5kZXhxEV1VC2xhYmVsT2Zmc2V0cRJLAE59h1USbWluaW11bUxhYmVsUmFkaXVzcRNLAE59h1UIZHJhd01vZGVxFEsATn2HVQhvcHRpb25hbHEVfXEWVQxzZXJpYWxOdW1iZXJxF4iIXYdzVQdkaXNwbGF5cRhLAE59h3Uu'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVjb2xvcnECSwBOfYdVBWF0b21zcQNdVQVsYWJlbHEESwBOfYdVCGhhbGZib25kcQVLAE59h1UGcmFkaXVzcQZLAE59h1ULbGFiZWxPZmZzZXRxB0sATn2HVQhkcmF3TW9kZXEISwBOfYdVCG9wdGlvbmFscQl9VQdkaXNwbGF5cQpLAE59h3Uu'))
	crdInfo = cPickle.loads(base64.b64decode('gAJ9cQEu'))
	surfInfo = {'category': (0, None, {}), 'probeRadius': (0, None, {}), 'pointSize': (0, None, {}), 'name': [], 'density': (0, None, {}), 'colorMode': (0, None, {}), 'useLighting': (0, None, {}), 'transparencyBlendMode': (0, None, {}), 'molecule': [], 'smoothLines': (0, None, {}), 'lineWidth': (0, None, {}), 'allComponents': (0, None, {}), 'twoSidedLighting': (0, None, {}), 'customVisibility': [], 'drawMode': (0, None, {}), 'display': (0, None, {}), 'customColors': []}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {u'': ((0.329412, 0.360784, 0.94902), 1, u''), u'Ru': ((0.141176, 0.560784, 0.560784), 1, u'default'), u'Re': ((0.14902, 0.490196, 0.670588), 1, u'default'), u'Rf': ((0.8, 0, 0.34902), 1, u'default'), u'Ra': ((0, 0.490196, 0), 1, u'default'), u'Rb': ((0.439216, 0.180392, 0.690196), 1, u'default'), u'Rn': ((0.258824, 0.509804, 0.588235), 1, u'default'), u'Rh': ((0.0392157, 0.490196, 0.54902), 1, u'default'), u'Be': ((0.760784, 1, 0), 1, u'default'), u'Ba': ((0, 0.788235, 0), 1, u'default'), u'Bh': ((0.878431, 0, 0.219608), 1, u'default'), u'Bi': ((0.619608, 0.309804, 0.709804), 1, u'default'), u'Bk': ((0.541176, 0.309804, 0.890196), 1, u'default'), u'Br': ((0.65098, 0.160784, 0.160784), 1, u'default'), u'H': ((1, 1, 1), 1, u'default'), u'P': ((1, 0.501961, 0), 1, u'default'), u'Os': ((0.14902, 0.4, 0.588235), 1, u'default'), u'goldenrod': ((0.854902, 0.647059, 0.12549), 1, u'default'), u'Ge': ((0.4, 0.560784, 0.560784), 1, u'default'), u'Gd': ((0.270588, 1, 0.780392), 1, u'default'), u'Ga': ((0.760784, 0.560784, 0.560784), 1, u'default'), u'Pr': ((0.85098, 1, 0.780392), 1, u'default'),
u'Pt': ((0.815686, 0.815686, 0.878431), 1, u'default'), u'Pu': ((0, 0.419608, 1), 1, u'default'), u'C': ((0.564706, 0.564706, 0.564706), 1, u'default'), u'Pb': ((0.341176, 0.34902, 0.380392), 1, u'default'), u'forest green': ((0.133333, 0.545098, 0.133333), 1, u'default'), u'Pa': ((0, 0.631373, 1), 1, u'default'), u'Pd': ((0, 0.411765, 0.521569), 1, u'default'), u'Cd': ((1, 0.85098, 0.560784), 1, u'default'), u'Po': ((0.670588, 0.360784, 0), 1, u'default'), u'Pm': ((0.639216, 1, 0.780392), 1, u'default'), u'purple': ((0.627451, 0.12549, 0.941176), 1, u'default'), u'Hs': ((0.901961, 0, 0.180392), 1, u'default'), u'Ho': ((0, 1, 0.611765), 1, u'default'), u'Hf': ((0.301961, 0.760784, 1), 1, u'default'), u'Hg': ((0.721569, 0.721569, 0.815686), 1, u'default'), u'He': ((0.85098, 1, 1), 1, u'default'), u'Md': ((0.701961, 0.0509804, 0.65098), 1, u'default'), u'Mg': ((0.541176, 1, 0), 1, u'default'), u'K': ((0.560784, 0.25098, 0.831373), 1, u'default'), u'Mn': ((0.611765, 0.478431, 0.780392), 1, u'default'), u'O': ((1, 0.0509804, 0.0509804), 1, u'default'), u'Mt': ((0.921569, 0, 0.14902), 1, u'default'),
u'S': ((1, 1, 0.188235), 1, u'default'), u'W': ((0.129412, 0.580392, 0.839216), 1, u'default'), u'Zn': ((0.490196, 0.501961, 0.690196), 1, u'default'), u'Eu': ((0.380392, 1, 0.780392), 1, u'default'), u'Es': ((0.701961, 0.121569, 0.831373), 1, u'default'), u'Er': ((0, 0.901961, 0.458824), 1, u'default'), u'Ni': ((0.313725, 0.815686, 0.313725), 1, u'default'), u'No': ((0.741176, 0.0509804, 0.529412), 1, u'default'), u'Na': ((0.670588, 0.360784, 0.94902), 1, u'default'), u'Nb': ((0.45098, 0.760784, 0.788235), 1, u'default'), u'Nd': ((0.780392, 1, 0.780392), 1, u'default'), u'Ne': ((0.701961, 0.890196, 0.960784), 1, u'default'), u'Np': ((0, 0.501961, 1), 1, u'default'), u'Fr': ((0.258824, 0, 0.4), 1, u'default'), u'Fe': ((0.878431, 0.4, 0.2), 1, u'default'), u'Fm': ((0.701961, 0.121569, 0.729412), 1, u'default'), u'B': ((1, 0.709804, 0.709804), 1, u'default'), u'F': ((0.564706, 0.878431, 0.313725), 1, u'default'), u'Sr': ((0, 1, 0), 1, u'default'), u'N': ((0.188235, 0.313725, 0.972549), 1, u'default'), u'Kr': ((0.360784, 0.721569, 0.819608), 1, u'default'),
u'Si': ((0.941176, 0.784314, 0.627451), 1, u'default'), u'Sn': ((0.4, 0.501961, 0.501961), 1, u'default'), u'Sm': ((0.560784, 1, 0.780392), 1, u'default'), u'V': ((0.65098, 0.65098, 0.670588), 1, u'default'), u'Sc': ((0.901961, 0.901961, 0.901961), 1, u'default'), u'Sb': ((0.619608, 0.388235, 0.709804), 1, u'default'), u'light sea green': ((0.12549, 0.698039, 0.666667), 1, u'default'), u'Sg': ((0.85098, 0, 0.270588), 1, u'default'), u'Se': ((1, 0.631373, 0), 1, u'default'), u'Co': ((0.941176, 0.564706, 0.627451), 1, u'default'), u'Cm': ((0.470588, 0.360784, 0.890196), 1, u'default'), u'Cl': ((0.121569, 0.941176, 0.121569), 1, u'default'), u'Ca': ((0.239216, 1, 0), 1, u'default'), u'Cf': ((0.631373, 0.211765, 0.831373), 1, u'default'), u'Ce': ((1, 1, 0.780392), 1, u'default'), u'Xe': ((0.258824, 0.619608, 0.690196), 1, u'default'), u'Tm': ((0, 0.831373, 0.321569), 1, u'default'), u'Cs': ((0.341176, 0.0901961, 0.560784), 1, u'default'), u'Cr': ((0.541176, 0.6, 0.780392), 1, u'default'), u'Cu': ((0.784314, 0.501961, 0.2), 1, u'default'), u'La': ((0.439216, 0.831373, 1), 1, u'default'),
u'Li': ((0.8, 0.501961, 1), 1, u'default'), u'Tl': ((0.65098, 0.329412, 0.301961), 1, u'default'), u'Lu': ((0, 0.670588, 0.141176), 1, u'default'), u'Lr': ((0.780392, 0, 0.4), 1, u'default'), u'Th': ((0, 0.729412, 1), 1, u'default'), u'Ti': ((0.74902, 0.760784, 0.780392), 1, u'default'), u'Te': ((0.831373, 0.478431, 0), 1, u'default'), u'Tb': ((0.188235, 1, 0.780392), 1, u'default'), u'Tc': ((0.231373, 0.619608, 0.619608), 1, u'default'), u'Ta': ((0.301961, 0.65098, 1), 1, u'default'), u'pink': ((1, 0.752941, 0.796078), 1, u'default'), u'lime green': ((0.196078, 0.803922, 0.196078), 1, u'default'), u'Yb': ((0, 0.74902, 0.219608), 1, u'default'), u'Db': ((0.819608, 0, 0.309804), 1, u'default'), u'Zr': ((0.580392, 0.878431, 0.878431), 1, u'default'), u'Dy': ((0.121569, 1, 0.780392), 1, u'default'), u'I': ((0.580392, 0, 0.580392), 1, u'default'), u'U': ((0, 0.560784, 1), 1, u'default'), u'Y': ((0.580392, 1, 1), 1, u'default'), u'Ac': ((0.439216, 0.670588, 0.980392), 1, u'default'), u'Ag': ((0.752941, 0.752941, 0.752941), 1, u'default'), u'Ir': ((0.0901961, 0.329412, 0.529412), 1, u'default'),
u'Am': ((0.329412, 0.360784, 0.94902), 1, u'default'), u'Al': ((0.74902, 0.65098, 0.65098), 1, u'default'), u'As': ((0.741176, 0.501961, 0.890196), 1, u'default'), u'Ar': ((0.501961, 0.819608, 0.890196), 1, u'default'), u'Au': ((1, 0.819608, 0.137255), 1, u'default'), u'At': ((0.458824, 0.309804, 0.270588), 1, u'default'), u'In': ((0.65098, 0.458824, 0.45098), 1, u'default'), u'Mo': ((0.329412, 0.709804, 0.709804), 1, u'default')}
	materials = {u'default': ((0.85, 0.85, 0.85), 30), u'': ((0.85, 0.85, 0.85), 30)}
	pbInfo = {'category': [u'distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'labelOffset': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 0, {}), 'optional': {'fixedLabels': (True, False, (1, False, {}))}, 'display': (1, True, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = (3, (u'white', (1, 1, 1, 1)), {(u'green', (0, 1, 0, 1)): [2], (u'yellow', (1, 1, 0, 1)): [0]})
	viewerInfo = {'cameraAttrs': {'center': (-17.339942932129, -21.558036804199, 45.926021575928), 'fieldOfView': 35.491749422611, 'nearFar': (154.23474973413, -96.557069407242), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 45.926021575928}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'showShadows': False, 'viewSize': 105.9952294518, 'labelsOnTop': True, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 2, 'singleLayerTransparency': True, 'shadowTextureSize': 2048, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [('Chimera default', [(1, 1, 1, 1), (0, 0, 1, 1)], 1), 1, 0, 0], 'depthCue': True, 'highlight': 0, 'scaleFactor': 0.60697690359809, 'angleDependentTransparency': True, 'backgroundMethod': 0}, 'viewerHL': 2, 'cameraMode': 'mono', 'detail': 1.5, 'viewerFog': None, 'viewerBG': 1}

	replyobj.status("Initializing session restore...", blankAfter=0,
		secondary=True)
	from SimpleSession.versions.v65 import expandSummary
	init(dict(enumerate(expandSummary(colorInfo))))
	replyobj.status("Restoring colors...", blankAfter=0,
		secondary=True)
	restoreColors(colors, materials)
	replyobj.status("Restoring molecules...", blankAfter=0,
		secondary=True)
	restoreMolecules(molInfo, resInfo, atomInfo, bondInfo, crdInfo)
	replyobj.status("Restoring surfaces...", blankAfter=0,
		secondary=True)
	restoreSurfaces(surfInfo)
	replyobj.status("Restoring VRML models...", blankAfter=0,
		secondary=True)
	restoreVRML(vrmlInfo)
	replyobj.status("Restoring pseudobond groups...", blankAfter=0,
		secondary=True)
	restorePseudoBondGroups(pbInfo)
	replyobj.status("Restoring model associations...", blankAfter=0,
		secondary=True)
	restoreModelAssociations(modelAssociations)
	replyobj.status("Restoring camera...", blankAfter=0,
		secondary=True)
	restoreViewer(viewerInfo)

try:
	restoreCoreModels()
except:
	reportRestoreError("Error restoring core models")

	replyobj.status("Restoring extension info...", blankAfter=0,
		secondary=True)


try:
	import StructMeasure
	from StructMeasure.DistMonitor import restoreDistances
	registerAfterModelsCB(restoreDistances, 1)
except:
	reportRestoreError("Error restoring distances in session")


def restoreMidasBase():
	formattedPositions = {'session-start': (0.64877334281845, 105.9952294518, (-17.339942932129, -21.558036804199, 45.926021575928), (154.23474973413, -96.557069407242), 45.926021575928, {(0, 0): ((10.790542406362789, -50.213631987673345, 29.3508865184106), (-0.6464555979999888, 0.5495642147038083, 0.5292204963259296, 131.4543820677487)), (7, 0): ((-13.47192345733425, -43.885397698245505, -56.9395568608308), (-0.659359869419497, 0.5467075334885844, 0.5160963431627202, 131.45804407205927)), (3, 0): ((10.790542406362789, -50.213631987673345, 29.3508865184106), (-0.6464555979999888, 0.5495642147038083, 0.5292204963259296, 131.4543820677487)), (8, 0): ((-13.47192345733425, -43.885397698245505, -56.9395568608308), (-0.659359869419497, 0.5467075334885844, 0.5160963431627202, 131.45804407205927)), (6, 0): ((-13.47192345733425, -43.885397698245505, -56.9395568608308), (-0.659359869419497, 0.5467075334885844, 0.5160963431627202, 131.45804407205927)), (2, 0): ((10.790542406362789, -50.213631987673345, 29.3508865184106), (-0.6464555979999888, 0.5495642147038083, 0.5292204963259296, 131.4543820677487)), (5, 0): ((10.790542406362789, -50.213631987673345, 29.3508865184106), (-0.6464555979999888, 0.5495642147038083, 0.5292204963259296, 131.4543820677487)), (1, 0): ((10.790542406362789, -50.213631987673345, 29.3508865184106), (-0.6464555979999888, 0.5495642147038083, 0.5292204963259296, 131.4543820677487)), (4, 0): ((10.790542406362789, -50.213631987673345, 29.3508865184106), (-0.6464555979999888, 0.5495642147038083, 0.5292204963259296, 131.4543820677487))}, {(6, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (3, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (0, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (5, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (2, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (7, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (4, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (1, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (8, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0)}, 4, (17.997290964758292, -12.767672930149132, 28.838840163444942), False, 35.491749422611)}
	import Midas
	Midas.restoreMidasBase(formattedPositions)
try:
	restoreMidasBase()
except:
	reportRestoreError('Error restoring Midas base state')


def restoreMidasText():
	from Midas import midas_text
	midas_text.aliases = {}
	midas_text.userSurfCategories = {}

try:
	restoreMidasText()
except:
	reportRestoreError('Error restoring Midas text state')


def restore_cap_attributes():
 cap_attributes = \
  {
   'cap_attributes': [
     {
      'cap_color': None,
      'class': 'Model_Capper_State',
      'display_style': None,
      'surface': ( 0, 0, ),
      'version': 1,
     },
     {
      'cap_color': None,
      'class': 'Model_Capper_State',
      'display_style': None,
      'surface': ( 1, 0, ),
      'version': 1,
     },
     {
      'cap_color': None,
      'class': 'Model_Capper_State',
      'display_style': None,
      'surface': ( 2, 0, ),
      'version': 1,
     },
     {
      'cap_color': None,
      'class': 'Model_Capper_State',
      'display_style': None,
      'surface': ( 3, 0, ),
      'version': 1,
     },
     {
      'cap_color': None,
      'class': 'Model_Capper_State',
      'display_style': None,
      'surface': ( 4, 0, ),
      'version': 1,
     },
     {
      'cap_color': None,
      'class': 'Model_Capper_State',
      'display_style': None,
      'surface': ( 5, 0, ),
      'version': 1,
     },
     {
      'cap_color': None,
      'class': 'Model_Capper_State',
      'display_style': None,
      'surface': ( 6, 0, ),
      'version': 1,
     },
     {
      'cap_color': None,
      'class': 'Model_Capper_State',
      'display_style': None,
      'surface': ( 7, 0, ),
      'version': 1,
     },
     {
      'cap_color': None,
      'class': 'Model_Capper_State',
      'display_style': None,
      'surface': ( 8, 0, ),
      'version': 1,
     },
    ],
   'cap_color': None,
   'cap_offset': 0.01,
   'class': 'Caps_State',
   'default_cap_offset': 0.01,
   'mesh_style': False,
   'shown': True,
   'subdivision_factor': 1.0,
   'version': 1,
  }
 import SurfaceCap.session
 SurfaceCap.session.restore_cap_attributes(cap_attributes)
registerAfterModelsCB(restore_cap_attributes)


def restore_volume_data():
 volume_data_state = \
  {
   'class': 'Volume_Manager_State',
   'data_and_regions_state': [
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': 'Spc110.1-204-220.mrc',
       'path': 'Spc110.1-204-220.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 1, 0.7, 0.7, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 45, 47, 43, ),
          ( 1, 1, 1, ),
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 45, 47, 43, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': False,
          'cap_faces': True,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': True,
          'dim_transparent_voxels': True,
          'flip_normals': False,
          'limit_voxel_count': True,
          'line_thickness': 1.0,
          'linear_interpolation': True,
          'maximum_intensity_projection': False,
          'mesh_lighting': True,
          'minimal_texture_memory': False,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': False,
          'smooth_lines': False,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': True,
          'subdivide_surface': False,
          'subdivision_levels': 1,
          'surface_smoothing': False,
          'two_sided_lighting': True,
          'version': 1,
          'voxel_limit': 1.0,
         },
        'representation': 'surface',
        'session_volume_id': 'g(R\\\'#1"}C}"@S"w \t||si@G!fj;;+~0',
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 1, 0.7, 0.7, 1, ),
          ( 1, 0.7, 0.7, 1, ),
          ( 1, 0.7, 0.7, 1, ),
         ],
        'solid_levels': [
          ( 0.0, 0, ),
          ( 0.0011129363775253295, 0.99, ),
          ( 0.13572394847869873, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.13333334028720856, 0.545098066329956, 0.13333334028720856, 0.6000000238418579, ),
         ],
        'surface_levels': [ 0.008730096751329849, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 5,
          'name': u'Spc110.1-204-220.mrc',
          'osl_identifier': u'#5',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 131.4543820677487,
            'rotation_axis': ( -0.6464555979999888, 0.5495642147038083, 0.5292204963259296, ),
            'translation': ( 10.790542406362789, -50.213631987673345, 29.3508865184106, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.2,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': 'Spc110.0-164-203.mrc',
       'path': 'Spc110.0-164-203.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 1, 1, 0.7, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 44, 41, 45, ),
          ( 1, 1, 1, ),
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 44, 41, 45, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': False,
          'cap_faces': True,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': True,
          'dim_transparent_voxels': True,
          'flip_normals': False,
          'limit_voxel_count': True,
          'line_thickness': 1.0,
          'linear_interpolation': True,
          'maximum_intensity_projection': False,
          'mesh_lighting': True,
          'minimal_texture_memory': False,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': False,
          'smooth_lines': False,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': True,
          'subdivide_surface': False,
          'subdivision_levels': 1,
          'surface_smoothing': False,
          'two_sided_lighting': True,
          'version': 1,
          'voxel_limit': 1.0,
         },
        'representation': 'surface',
        'session_volume_id': "d,n'+\x0cQnZWP}Ps9\rtG6HW22~Nid 0oiN",
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 1, 1, 0.7, 1, ),
          ( 1, 1, 0.7, 1, ),
          ( 1, 1, 0.7, 1, ),
         ],
        'solid_levels': [
          ( 0.0, 0, ),
          ( 0.0020412205666303636, 0.99, ),
          ( 0.3459695875644684, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.19607843458652496, 0.8039215803146362, 0.19607843458652496, 0.6000000238418579, ),
         ],
        'surface_levels': [ 0.02145788109320768, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 1,
          'name': u'Spc110.0-164-203.mrc',
          'osl_identifier': u'#1',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 131.4543820677487,
            'rotation_axis': ( -0.6464555979999888, 0.5495642147038083, 0.5292204963259296, ),
            'translation': ( 10.790542406362789, -50.213631987673345, 29.3508865184106, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.2,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': 'Spc110.0-1-163.mrc',
       'path': 'Spc110.0-1-163.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.7, 0.7, 0.7, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 63, 60, 70, ),
          ( 1, 1, 1, ),
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 63, 60, 70, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': False,
          'cap_faces': True,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': True,
          'dim_transparent_voxels': True,
          'flip_normals': False,
          'limit_voxel_count': True,
          'line_thickness': 1.0,
          'linear_interpolation': True,
          'maximum_intensity_projection': False,
          'mesh_lighting': True,
          'minimal_texture_memory': False,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': False,
          'smooth_lines': False,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': True,
          'subdivide_surface': False,
          'subdivision_levels': 1,
          'surface_smoothing': False,
          'two_sided_lighting': True,
          'version': 1,
          'voxel_limit': 1.0,
         },
        'representation': 'surface',
        'session_volume_id': 'O<\reM^ FQ&yd9@vTDRzT2sYZgHw IW!z',
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 1.0, 1.0, 1.0, 1, ),
          ( 1.0, 1.0, 1.0, 1, ),
          ( 1.0, 1.0, 1.0, 1, ),
         ],
        'solid_levels': [
          ( 0.0, 0, ),
          ( 0.01054811793267727, 0.99, ),
          ( 0.42704930901527405, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.19607843458652496, 0.8039215803146362, 0.19607843458652496, 0.6000000238418579, ),
         ],
        'surface_levels': [ 0.0265, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 0,
          'name': u'Spc110.0-1-163.mrc',
          'osl_identifier': u'#0',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 131.4543820677487,
            'rotation_axis': ( -0.6464555979999888, 0.5495642147038083, 0.5292204963259296, ),
            'translation': ( 10.790542406362789, -50.213631987673345, 29.3508865184106, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.2,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': 'Tub4.mrc',
       'path': 'Tub4.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.6, 0.75, 0.9, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 63, 65, 57, ),
          ( 1, 1, 1, ),
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 63, 65, 57, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': False,
          'cap_faces': True,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': True,
          'dim_transparent_voxels': True,
          'flip_normals': False,
          'limit_voxel_count': True,
          'line_thickness': 1.0,
          'linear_interpolation': True,
          'maximum_intensity_projection': False,
          'mesh_lighting': True,
          'minimal_texture_memory': False,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': False,
          'smooth_lines': False,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': True,
          'subdivide_surface': False,
          'subdivision_levels': 1,
          'surface_smoothing': False,
          'two_sided_lighting': True,
          'version': 1,
          'voxel_limit': 1.0,
         },
        'representation': 'surface',
        'session_volume_id': ' Z!HVR\x0c7HN\x0cjv:X:z>O+k=bqdb=n&p,B',
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 0.6666666666666666, 0.8333333333333333, 1.0, 1, ),
          ( 0.6666666666666666, 0.8333333333333333, 1.0, 1, ),
          ( 0.6666666666666666, 0.8333333333333333, 1.0, 1, ),
         ],
        'solid_levels': [
          ( 0.0, 0, ),
          ( 0.04811013025045395, 0.99, ),
          ( 0.7636528611183167, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.8549019694328308, 0.6470588445663452, 0.125490203499794, 0.6000000238418579, ),
         ],
        'surface_levels': [ 0.052524308638421106, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 8,
          'name': u'Tub4.mrc',
          'osl_identifier': u'#8',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 131.45804407205927,
            'rotation_axis': ( -0.659359869419497, 0.5467075334885844, 0.5160963431627202, ),
            'translation': ( -13.47192345733425, -43.885397698245505, -56.9395568608308, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.2,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': 'Spc97.mrc',
       'path': 'Spc97.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.7, 1, 0.7, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 72, 68, 72, ),
          ( 1, 1, 1, ),
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 72, 68, 72, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': False,
          'cap_faces': True,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': True,
          'dim_transparent_voxels': True,
          'flip_normals': False,
          'limit_voxel_count': True,
          'line_thickness': 1.0,
          'linear_interpolation': True,
          'maximum_intensity_projection': False,
          'mesh_lighting': True,
          'minimal_texture_memory': False,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': False,
          'smooth_lines': False,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': True,
          'subdivide_surface': False,
          'subdivision_levels': 1,
          'surface_smoothing': False,
          'two_sided_lighting': True,
          'version': 1,
          'voxel_limit': 1.0,
         },
        'representation': 'surface',
        'session_volume_id': '{VUFP@ZUi5P_IQ=Le]>p8\r\\{f1C["dtl',
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 0.7, 1, 0.7, 1, ),
          ( 0.7, 1, 0.7, 1, ),
          ( 0.7, 1, 0.7, 1, ),
         ],
        'solid_levels': [
          ( 0.0, 0, ),
          ( 0.02303996977210045, 0.99, ),
          ( 0.7863470911979675, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.125490203499794, 0.6980392336845398, 0.6666666865348816, 0.6000000238418579, ),
         ],
        'surface_levels': [ 0.04716, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 6,
          'name': u'Spc97.mrc',
          'osl_identifier': u'#6',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 131.45804407205927,
            'rotation_axis': ( -0.659359869419497, 0.5467075334885844, 0.5160963431627202, ),
            'translation': ( -13.47192345733425, -43.885397698245505, -56.9395568608308, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.2,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': 'Spc110.0-204-220.mrc',
       'path': 'Spc110.0-204-220.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.7, 1, 1, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 43, 48, 43, ),
          ( 1, 1, 1, ),
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 43, 48, 43, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': False,
          'cap_faces': True,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': True,
          'dim_transparent_voxels': True,
          'flip_normals': False,
          'limit_voxel_count': True,
          'line_thickness': 1.0,
          'linear_interpolation': True,
          'maximum_intensity_projection': False,
          'mesh_lighting': True,
          'minimal_texture_memory': False,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': False,
          'smooth_lines': False,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': True,
          'subdivide_surface': False,
          'subdivision_levels': 1,
          'surface_smoothing': False,
          'two_sided_lighting': True,
          'version': 1,
          'voxel_limit': 1.0,
         },
        'representation': 'surface',
        'session_volume_id': '/6kJIxS#IB\t*[!RZ(a{sm\\!b<\rxpJd),',
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 0.7, 1, 1, 1, ),
          ( 0.7, 1, 1, 1, ),
          ( 0.7, 1, 1, 1, ),
         ],
        'solid_levels': [
          ( 0.0, 0, ),
          ( 0.0011423904150724411, 0.99, ),
          ( 0.14646030962467194, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.19607843458652496, 0.8039215803146362, 0.19607843458652496, 0.6000000238418579, ),
         ],
        'surface_levels': [ 0.009362101669518317, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 2,
          'name': u'Spc110.0-204-220.mrc',
          'osl_identifier': u'#2',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 131.4543820677487,
            'rotation_axis': ( -0.6464555979999888, 0.5495642147038083, 0.5292204963259296, ),
            'translation': ( 10.790542406362789, -50.213631987673345, 29.3508865184106, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.2,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': 'Spc110.1-1-163.mrc',
       'path': 'Spc110.1-1-163.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.7, 0.7, 1, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 61, 58, 65, ),
          ( 1, 1, 1, ),
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 61, 58, 65, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': False,
          'cap_faces': True,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': True,
          'dim_transparent_voxels': True,
          'flip_normals': False,
          'limit_voxel_count': True,
          'line_thickness': 1.0,
          'linear_interpolation': True,
          'maximum_intensity_projection': False,
          'mesh_lighting': True,
          'minimal_texture_memory': False,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': False,
          'smooth_lines': False,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': True,
          'subdivide_surface': False,
          'subdivision_levels': 1,
          'surface_smoothing': False,
          'two_sided_lighting': True,
          'version': 1,
          'voxel_limit': 1.0,
         },
        'representation': 'surface',
        'session_volume_id': "/nV,5G(+)#{5'q2$>IsI;\nS)o[bf0%Q?",
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 0.7, 0.7, 1, 1, ),
          ( 0.7, 0.7, 1, 1, ),
          ( 0.7, 0.7, 1, 1, ),
         ],
        'solid_levels': [
          ( 0.0, 0, ),
          ( 0.010876027584075928, 0.99, ),
          ( 0.3577640652656555, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.13333334028720856, 0.545098066329956, 0.13333334028720856, 0.6000000238418579, ),
         ],
        'surface_levels': [ 0.0254786424928782, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 3,
          'name': u'Spc110.1-1-163.mrc',
          'osl_identifier': u'#3',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 131.4543820677487,
            'rotation_axis': ( -0.6464555979999888, 0.5495642147038083, 0.5292204963259296, ),
            'translation': ( 10.790542406362789, -50.213631987673345, 29.3508865184106, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.2,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': 'Spc98.mrc',
       'path': 'Spc98.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.9, 0.75, 0.6, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 69, 68, 76, ),
          ( 1, 1, 1, ),
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 69, 68, 76, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': False,
          'cap_faces': True,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': True,
          'dim_transparent_voxels': True,
          'flip_normals': False,
          'limit_voxel_count': True,
          'line_thickness': 1.0,
          'linear_interpolation': True,
          'maximum_intensity_projection': False,
          'mesh_lighting': True,
          'minimal_texture_memory': False,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': False,
          'smooth_lines': False,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': True,
          'subdivide_surface': False,
          'subdivision_levels': 1,
          'surface_smoothing': False,
          'two_sided_lighting': True,
          'version': 1,
          'voxel_limit': 1.0,
         },
        'representation': 'surface',
        'session_volume_id': ")U&$\r4zD\nVP~h~'yVCH'O.XJ6m'R9of%",
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 1.0, 0.8333333333333333, 0.6666666666666666, 1, ),
          ( 1.0, 0.8333333333333333, 0.6666666666666666, 1, ),
          ( 1.0, 0.8333333333333333, 0.6666666666666666, 1, ),
         ],
        'solid_levels': [
          ( 0.0, 0, ),
          ( 0.019367289733886718, 0.99, ),
          ( 1.3449506759643555, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.0, 0.0, 1.0, 0.6000000238418579, ),
         ],
        'surface_levels': [ 0.08112522893633162, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 7,
          'name': u'Spc98.mrc',
          'osl_identifier': u'#7',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 131.45804407205927,
            'rotation_axis': ( -0.659359869419497, 0.5467075334885844, 0.5160963431627202, ),
            'translation': ( -13.47192345733425, -43.885397698245505, -56.9395568608308, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.2,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90.0, 90.0, 90.0, ),
       'class': 'Data_State',
       'file_type': 'mrc',
       'grid_id': '',
       'name': 'Spc110.1-164-203.mrc',
       'path': 'Spc110.1-164-203.mrc',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 1, 0.7, 1, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 47, 41, 45, ),
          ( 1, 1, 1, ),
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 47, 41, 45, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': False,
          'cap_faces': True,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': True,
          'dim_transparent_voxels': True,
          'flip_normals': False,
          'limit_voxel_count': True,
          'line_thickness': 1.0,
          'linear_interpolation': True,
          'maximum_intensity_projection': False,
          'mesh_lighting': True,
          'minimal_texture_memory': False,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': False,
          'smooth_lines': False,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': True,
          'subdivide_surface': False,
          'subdivision_levels': 1,
          'surface_smoothing': False,
          'two_sided_lighting': True,
          'version': 1,
          'voxel_limit': 1.0,
         },
        'representation': 'surface',
        'session_volume_id': '1t#`r\\!hJ\x0cR|a^,z6J`*\\o`#/\x0c?o\tOd4',
        'solid_brightness_factor': 1.0,
        'solid_colors': [
          ( 1, 0.7, 1, 1, ),
          ( 1, 0.7, 1, 1, ),
          ( 1, 0.7, 1, 1, ),
         ],
        'solid_levels': [
          ( 0.0, 0, ),
          ( 0.001614929586648941, 0.99, ),
          ( 0.3229859173297882, 1, ),
         ],
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.13333334028720856, 0.545098066329956, 0.13333334028720856, 0.6000000238418579, ),
         ],
        'surface_levels': [ 0.02056563391977427, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 4,
          'name': u'Spc110.1-164-203.mrc',
          'osl_identifier': u'#4',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 131.4543820677487,
            'rotation_axis': ( -0.6464555979999888, 0.5495642147038083, 0.5292204963259296, ),
            'translation': ( 10.790542406362789, -50.213631987673345, 29.3508865184106, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.2,
        'version': 6,
       },
      ],
     ),
    ],
   'version': 2,
  }
 from VolumeViewer import session
 session.restore_volume_data_state(volume_data_state)

try:
  restore_volume_data()
except:
  reportRestoreError('Error restoring volume data')


def restore_volume_dialog():
 volume_dialog_state = \
  {
   'adjust_camera': False,
   'auto_show_subregion': False,
   'box_padding': '0',
   'class': 'Volume_Dialog_State',
   'data_cache_size': '512',
   'focus_volume': ' Z!HVR\x0c7HN\x0cjv:X:z>O+k=bqdb=n&p,B',
   'geometry': u'362x405+843+396',
   'histogram_active_order': [ 1, 2, 0, ],
   'histogram_volumes': [ '{VUFP@ZUi5P_IQ=Le]>p8\r\\{f1C["dtl', ' Z!HVR\x0c7HN\x0cjv:X:z>O+k=bqdb=n&p,B', ")U&$\r4zD\nVP~h~'yVCH'O.XJ6m'R9of%", ],
   'immediate_update': True,
   'initial_colors': (
     ( 0.7, 0.7, 0.7, 1, ),
     ( 1, 1, 0.7, 1, ),
     ( 0.7, 1, 1, 1, ),
     ( 0.7, 0.7, 1, 1, ),
     ( 1, 0.7, 1, 1, ),
     ( 1, 0.7, 0.7, 1, ),
     ( 0.7, 1, 0.7, 1, ),
     ( 0.9, 0.75, 0.6, 1, ),
     ( 0.6, 0.75, 0.9, 1, ),
     ( 0.8, 0.8, 0.6, 1, ),
    ),
   'is_visible': False,
   'max_histograms': '3',
   'representation': 'surface',
   'selectable_subregions': False,
   'show_on_open': True,
   'show_plane': True,
   'shown_panels': [ 'Threshold and Color', 'Display style', ],
   'subregion_button': 'middle',
   'use_initial_colors': True,
   'version': 12,
   'voxel_limit_for_open': '256',
   'voxel_limit_for_plane': '256',
   'zone_radius': 2.0,
  }
 from VolumeViewer import session
 session.restore_volume_dialog_state(volume_dialog_state)

try:
  restore_volume_dialog()
except:
  reportRestoreError('Error restoring volume dialog')

geomData = {'AxisManager': {}, 'CentroidManager': {}, 'PlaneManager': {}}

try:
	from StructMeasure.Geometry import geomManager
	geomManager._restoreSession(geomData)
except:
	reportRestoreError("Error restoring geometry objects in session")


def restoreSession_RibbonStyleEditor():
	import SimpleSession
	import RibbonStyleEditor
	userScalings = [('TPPfront', [[0.5, 0.5], [0.9, 0.25], [0.9, 0.25], [1.8, 0.25, 0.25, 0.25], [0.9, 0.25]]), ('Margy_thin', [[0.25, 0.25], [0.4, 0.25], [0.4, 0.25], [1.5, 0.25, 0.25, 0.25], [1.5, 0.25]]), ('FAT', [[0.6, 0.6], [1.5, 0.6], [1.5, 0.6], [3, 0.25, 0.25, 0.25], [0.7, 0.7]]), ('BS', [[0.3, 0.3], [1.5, 0.3], [1.5, 0.3], [3, 0.3, 0.25, 0.3], [1.5, 0.3]]), ('for3Dprint1', [[0.5, 0.5], [0.9, 0.5], [0.9, 0.5], [1.8, 0.5, 0.5, 0.5], [0.9, 0.5]]), ('encyclo_virol_2006_FAT', [[0.6, 0.6], [1.5, 0.6], [1.5, 0.6], [3, 0.25, 0.25, 0.25], [0.6, 0.6]]), ('Liz1', [[0.5, 0.5], [0.9, 0.25], [0.9, 0.25], [1.8, 0.25, 0.25, 0.25], [0.9, 0.25]]), ('histon_1_s1', [[0.25, 0.25], [1.5, 0.25], [1.5, 0.25], [3, 0.25, 0.25, 0.25], [1.5, 0.25]]), ('licorice', [[0.35, 0.35], [0.35, 0.35], [0.35, 0.35], [0.35, 0.35, 0.35, 0.35], [0.35, 0.35]]), ('minus_20%', [[0.2, 0.2], [1.2, 0.2], [1.2, 0.2], [2.4, 0.2, 0.2, 0.2], [1.2, 0.2]]), ('slimrib', [[0.2, 0.2], [1, 0.2], [1, 0.2], [0.2, 0.2, 2, 0.2], [1, 0.2]]), ('narrow nucleic 2 -gary', [[0.2, 0.2], [0.9, 0.2], [0.95, 0.2], [1.8, 0.2, 0.2, 0.2], [0.35, 0.35]]),
('plump', [[0.3, 0.3], [1.2, 0.3], [1.2, 0.3], [2, 0.3, 0.3, 0.3], [1.2, 0.3]]), ('80percent', [[0.2, 0.2], [1.2, 0.2], [1.2, 0.2], [2.4, 0.2, 0.2, 0.2], [1.2, 0.2]]), ('thin even', [[0.4, 0.4], [0.4, 0.4], [0.4, 0.4], [0.4, 0.4, 0.4, 0.4], [1.5, 0.25]]), ('testdefault', [[0.25, 0.25], [1.5, 0.25], [1.5, 0.25], [3, 0.25, 0.25, 0.25], [1.5, 0.25]]), ('fatz', [[0.25, 0.25], [2.5, 0.25], [2.5, 0.25], [3, 0.25, 0.25, 0.25], [1.5, 0.25]]), ('user default', [[0.25, 0.25], [1.5, 0.25], [1.5, 0.25], [0.25, 0.25, 3, 0.25], [1.5, 0.25]]), ('default', [[0.25, 0.25], [1.5, 0.25], [1.5, 0.25], [0.25, 0.25, 3, 0.25], [1.5, 0.25]]), ('Margy_medium', [[0.45, 0.25], [0.7, 0.25], [0.7, 0.25], [1.5, 0.25, 0.45, 0.25], [1.5, 0.25]]), ('encyclo_virol_2006_STD', [[0.4, 0.4], [1.5, 0.4], [1.5, 0.4], [3, 0.25, 0.25, 0.25], [0.4, 0.4]]), ('thin', [[0.15, 0.15], [0.75, 0.15], [0.75, 0.15], [1.75, 0.15, 0.15, 0.15], [1.5, 0.25]]), ('aa', [[0.25, 0.25], [1.7, 0.25], [1.5, 0.25], [0.25, 0.25, 3, 0.25], [1.7, 0.25]]), ('slim', [[0.2, 0.2], [1.2, 0.2], [1.2, 0.2], [2.4, 0.2, 0.2, 0.2], [1.2, 0.2]]),
('irina', [[0.25, 0.2], [1.4, 0.1], [1.3, 0.1], [2.5, 0.15, 0.1, 0.15], [1.5, 0.15]]), ('SUPERFAT', [[0.7, 0.7], [1.6, 0.7], [1.6, 0.7], [3.1, 0.35, 0.35, 0.35], [0.7, 0.7]]), ('60%', [[0.15, 0.15], [0.9, 0.15], [0.9, 0.15], [1.8, 0.15, 0.15, 0.15], [0.9, 0.15]]), ('60_percent', [[0.15, 0.15], [0.9, 0.15], [0.9, 0.15], [2.4, 0.15, 0.15, 0.15], [0.9, 0.15]]), ('ssccmv_ribbon_scale', [[0.3, 0.3], [1.25, 0.5], [1.25, 0.5], [2.25, 0.25, 0.25, 0.25], [1.5, 0.25]]), ('spaghetti', [[0.25, 0.25], [0.25, 0.25], [0.25, 0.25], [0.25, 0.25, 0.25, 0.25], [0.25, 0.25]]), ('thin2', [[0.25, 0.15], [0.4, 0.15], [0.4, 0.15], [1, 0.15, 0.25, 0.15], [1.5, 0.25]]), ('no-helix', [[0.25, 0.25], [0.25, 0.25], [1.5, 0.25], [3, 0.25, 0.25, 0.25], [1.5, 0.25]]), ('thinturn', [[0.1, 0.25], [1.5, 0.25], [1.5, 0.25], [3, 0.25, 0.25, 0.25], [1.5, 0.25]]), ('linguini', [[0.1, 0.1], [0.1, 0.1], [0.1, 0.1], [0.1, 0.1, 0.1, 0.1], [0.1, 0.1]]), ('TPP_Front', [[0.5, 0.5], [1.25, 0.25], [1.25, 0.25], [1.8, 0.25, 0.25, 0.25], [0.9, 0.25]]), ('irina_3', [[0.2, 0.2], [1, 0.2], [1, 0.2], [2, 0.2, 0.1, 0.1], [0.8, 0.2]]),
('irina_2', [[0.2, 0.2], [1.3, 0.2], [1.2, 0.2], [2, 0.2, 0.2, 0.2], [0.9, 0.2]]), ('60percent', [[0.15, 0.15], [0.9, 0.15], [0.9, 0.15], [1.8, 0.15, 0.15, 0.15], [0.9, 0.15]]), ('extrafatty', [[0.5, 0.35], [1.2, 0.35], [1.2, 0.35], [1.9, 0.25, 0.25, 0.25], [0.9, 0.25]]), ('fatty', [[0.35, 0.25], [0.95, 0.25], [0.95, 0.25], [1.9, 0.25, 0.25, 0.25], [0.9, 0.25]]), ('40%', [[0.1, 0.1], [0.6, 0.1], [0.6, 0.1], [1.2, 0.1, 0.1, 0.1], [0.6, 0.1]]), ('narrow nucleic - gary', [[0.2, 0.2], [0.9, 0.2], [0.95, 0.2], [1.8, 0.2, 0.2, 0.2], [0.35, 0.2]]), ('20%', [[0.05, 0.05], [0.3, 0.05], [0.3, 0.05], [0.6, 0.05, 0.05, 0.05], [0.3, 0.05]]), ('for3Dprint1round', [[0.8, 0.8], [1.5, 0.8], [1.5, 0.8], [2.4, 0.8, 0.8, 0.8], [1, 0.6]]), ('slim2029', [[0.2, 0.2], [1.2, 0.2], [1.2, 0.2], [2.4, 0.2, 0.2, 0.2], [1.2, 0.2]]), ('skinny', [[0.25, 0.25], [0.75, 0.25], [0.75, 0.25], [1.5, 0.25, 0.25, 0.25], [1.5, 0.25]])]
	userXSections = [('', ([(4, 4), (5, 5), (6, 5), (7, 4), (7, 3), (6, 2), (5, 2), (4, 3)], 1, 1, 1, 10)), ('diamond', ([(3, 3), (0, 5), (3, 7), (7, 7), (10, 5), (7, 3)], 0, 1, 1, 10)), ('large_octagon', ([(1, 3), (1, 5), (3, 7), (5, 7), (7, 5), (7, 3), (5, 1), (3, 1)], 1, 1, 1, 8)), ('octagon', ([(4, 4), (5, 5), (6, 5), (7, 4), (7, 3), (6, 2), (5, 2), (4, 3)], 1, 1, 1, 10)), ('thin_round_square', ([(4, 2), (5, 2), (6, 5), (4, 3), (4, 4), (4, 5), (6, 4), (5, 4), (5, 3), (6, 3)], True, True, True, 10)), ('ibeam', ([(10, 0), (8, 0), (8, 4), (2, 4), (2, 0), (0, 0), (0, 10), (2, 10), (2, 6), (8, 6), (8, 10), (10, 10)], 0, 1, 1, 10)), ('aitch', ([(0, 0), (0, 10), (3, 10), (3, 6), (7, 6), (7, 10), (10, 10), (10, 0), (7, 0), (7, 4), (3, 4), (3, 0), (0, 0)], 1, True, False, 10)), ('ocatagon', ([(4, 4), (5, 5), (6, 5), (7, 4), (7, 3), (6, 2), (5, 2), (4, 3)], 1, 1, 1, 10)), ('wave', ([(18, 18), (18, 19), (18, 31), (31, 31), (31, 18)], True, True, True, 50))]
	userResidueClasses = [('aa-nomain-ca-o', ('CA', 'O', False, False, {})), ('aa-camain-ca-n', ('CA', 'N', False, False, {'CA': 0.5})), ('aa-camain-ca-o', ('CA', 'O', False, False, {'CA': 0.5})), ('aa-camain-ca-c', ('CA', 'C', False, False, {'CA': 0.5})), ('pguide', ('P', "C1'", False, True, {"C5'": 0.5, 'P': 0.166667, "O3'": 1, 'O1P': 0.166667, 'O3P': 0.166667, "O5'": 0.333333, 'O3T': 1, 'O2P': 0.166667, 'O5T': 0})), ('aa-nomain-c-o', ('C', 'O', False, False, {})), ('pguiderot', ('P', "C1'", 1, True, {"C5'": 0.5, 'P': 0.166667, "O3'": 1, 'O1P': 0.166667, 'O3P': 0.166667, "O5'": 0.333333, 'O3T': 1, 'O2P': 0.166667, 'O5T': 0}))]
	residueData = []
	flags = RibbonStyleEditor.NucleicDefault1
	SimpleSession.registerAfterModelsCB(RibbonStyleEditor.restoreState,
				(userScalings, userXSections,
				userResidueClasses, residueData, flags))
try:
	restoreSession_RibbonStyleEditor()
except:
	reportRestoreError("Error restoring RibbonStyleEditor state")

trPickle = 'gAJjQW5pbWF0ZS5UcmFuc2l0aW9ucwpUcmFuc2l0aW9ucwpxASmBcQJ9cQMoVQxjdXN0b21fc2NlbmVxBGNBbmltYXRlLlRyYW5zaXRpb24KVHJhbnNpdGlvbgpxBSmBcQZ9cQcoVQZmcmFtZXNxCEsBVQ1kaXNjcmV0ZUZyYW1lcQlLAVUKcHJvcGVydGllc3EKXXELVQNhbGxxDGFVBG5hbWVxDVUMY3VzdG9tX3NjZW5lcQ5VBG1vZGVxD1UGbGluZWFycRB1YlUIa2V5ZnJhbWVxEWgFKYFxEn1xEyhoCEsUaAlLAWgKXXEUaAxhaA1VCGtleWZyYW1lcRVoD2gQdWJVBXNjZW5lcRZoBSmBcRd9cRgoaAhLAWgJSwFoCl1xGWgMYWgNVQVzY2VuZXEaaA9oEHVidWIu'
scPickle = 'gAJjQW5pbWF0ZS5TY2VuZXMKU2NlbmVzCnEBKYFxAn1xA1UHbWFwX2lkc3EEfXNiLg=='
kfPickle = 'gAJjQW5pbWF0ZS5LZXlmcmFtZXMKS2V5ZnJhbWVzCnEBKYFxAn1xA1UHZW50cmllc3EEXXEFc2Iu'
def restoreAnimation():
	'A method to unpickle and restore animation objects'
	# Scenes must be unpickled after restoring transitions, because each
	# scene links to a 'scene' transition. Likewise, keyframes must be 
	# unpickled after restoring scenes, because each keyframe links to a scene.
	# The unpickle process is left to the restore* functions, it's 
	# important that it doesn't happen prior to calling those functions.
	import SimpleSession
	from Animate.Session import restoreTransitions
	from Animate.Session import restoreScenes
	from Animate.Session import restoreKeyframes
	SimpleSession.registerAfterModelsCB(restoreTransitions, trPickle)
	SimpleSession.registerAfterModelsCB(restoreScenes, scPickle)
	SimpleSession.registerAfterModelsCB(restoreKeyframes, kfPickle)
try:
	restoreAnimation()
except:
	reportRestoreError('Error in Animate.Session')

def restoreLightController():
	import Lighting
	Lighting._setFromParams({'ratio': 1.25, 'brightness': 1.16, 'material': [30.0, (0.85, 0.85, 0.85), 1.0], 'back': [(0.3574067443365933, 0.6604015517481455, -0.6604015517481456), (1.0, 1.0, 1.0), 0.0], 'mode': 'two-point', 'key': [(-0.3574067443365933, 0.6604015517481455, 0.6604015517481456), (1.0, 1.0, 1.0), 1.0], 'contrast': 0.83, 'fill': [(0.2505628070857316, 0.2505628070857316, 0.9351131265310294), (1.0, 1.0, 1.0), 0.0]})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")


try:
	import Ilabel
	il = Ilabel.LabelsModel(create=False)
	if il:
		il.destroy()
	il = Ilabel.LabelsModel()
	il.restoreSession({'labelIDs': ['Spc110.0-204-220_lab', 'Spc110.1-1-163_lab', 'Spc97_lab', 'Spc98_lab', 'Tub4_lab', 'label2d_id_9'], 'curLabel': 5, 'labels': [{'opacity': 1.0, 'lines': [[{'args': (u'S',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.19607843137254902, 0.803921568627451, 0.19607843137254902, 1.0), 'size': 30}}, {'args': (u'p',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.19607843137254902, 0.803921568627451, 0.19607843137254902, 1.0), 'size': 30}}, {'args': (u'c',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.19607843137254902, 0.803921568627451, 0.19607843137254902, 1.0), 'size': 30}}, {'args': (u'1',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.19607843137254902, 0.803921568627451, 0.19607843137254902, 1.0), 'size': 30}}, {'args': (u'1',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.19607843137254902, 0.803921568627451, 0.19607843137254902, 1.0), 'size': 30}}, {'args': (u'0',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.19607843137254902, 0.803921568627451, 0.19607843137254902, 1.0), 'size': 30}}, {'args': (u'1',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.19607843137254902, 0.803921568627451, 0.19607843137254902, 1.0), 'size': 20}}]], 'shown': True, 'args': ((0.7528, 0.8584884994523548),), 'kw': {'margin': 9.0, 'outline': 0.0, 'background': None}}, {'opacity': 1.0, 'lines': [[{'args': (u'S',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.13333333333333333, 0.5450980392156862, 0.13333333333333333, 1.0), 'size': 30}}, {'args': (u'p',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.13333333333333333, 0.5450980392156862, 0.13333333333333333, 1.0), 'size': 30}}, {'args': (u'c',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.13333333333333333, 0.5450980392156862, 0.13333333333333333, 1.0), 'size': 30}}, {'args': (u'1',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.13333333333333333, 0.5450980392156862, 0.13333333333333333, 1.0), 'size': 30}}, {'args': (u'1',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.13333333333333333, 0.5450980392156862, 0.13333333333333333, 1.0), 'size': 30}}, {'args': (u'0',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.13333333333333333, 0.5450980392156862, 0.13333333333333333, 1.0), 'size': 30}}, {'args': (u'2',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.13333333333333333, 0.5450980392156862, 0.13333333333333333, 1.0), 'size': 20}}]], 'shown': True, 'args': ((0.37120000000000003, 0.3955640744797372),), 'kw': {'margin': 9.0, 'outline': 0.0, 'background': None}}, {'opacity': 1.0, 'lines': [[{'args': (u'S',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.12549019607843137, 0.6980392156862745, 0.6666666666666666, 1.0), 'size': 30}}, {'args': (u'p',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.12549019607843137, 0.6980392156862745, 0.6666666666666666, 1.0), 'size': 30}}, {'args': (u'c',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.12549019607843137, 0.6980392156862745, 0.6666666666666666, 1.0), 'size': 30}}, {'args': (u'9',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.12549019607843137, 0.6980392156862745, 0.6666666666666666, 1.0), 'size': 30}}, {'args': (u'7',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.12549019607843137, 0.6980392156862745, 0.6666666666666666, 1.0), 'size': 30}}]], 'shown': True, 'args': ((0.72, 0.4930996714129245),), 'kw': {'margin': 9.0, 'outline': 0.0, 'background': None}}, {'opacity': 1.0, 'lines': [[{'args': (u'S',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.0, 0.0, 1.0, 1.0), 'size': 30}}, {'args': (u'p',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.0, 0.0, 1.0, 1.0), 'size': 30}}, {'args': (u'c',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.0, 0.0, 1.0, 1.0), 'size': 30}}, {'args': (u'9',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.0, 0.0, 1.0, 1.0), 'size': 30}}, {'args': (u'8',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.0, 0.0, 1.0, 1.0), 'size': 30}}]], 'shown': True, 'args': ((0.368, 0.49238773274917846),), 'kw': {'margin': 9.0, 'outline': 0.0, 'background': None}}, {'opacity': 1.0, 'lines': [[{'args': (u'T',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.8549019607843137, 0.6470588235294118, 0.12549019607843137, 1.0), 'size': 30}}, {'args': (u'u',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.8549019607843137, 0.6470588235294118, 0.12549019607843137, 1.0), 'size': 30}}, {'args': (u'b',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.8549019607843137, 0.6470588235294118, 0.12549019607843137, 1.0), 'size': 30}}, {'args': (u'4',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0.8549019607843137, 0.6470588235294118, 0.12549019607843137, 1.0), 'size': 30}}]], 'shown': True, 'args': ((0.332, 0.8323110624315443),), 'kw': {'margin': 9.0, 'outline': 0.0, 'background': None}}, {'opacity': 1.0, 'lines': [[]], 'shown': True, 'args': ((0.772, 0.32749178532311063),), 'kw': {'margin': 9.0, 'outline': 0.0, 'background': None}}], 'labelUID': 10})
	del Ilabel, il
except:
	reportRestoreError("Error restoring IlabelModel instance in session")


try:
	from Ilabel.Arrows import ArrowsModel
	ArrowsModel().restore({'arrows': []})
except:
	reportRestoreError("Error restoring 2D arrows in session")



try:
	from Ilabel.ColorKey import getKeyModel
	getKeyModel()._restoreSession({'label spacing': 'proportional to value', 'label justification': 'decimal point', 'font size': 24, 'label positions': 'right/bottom', 'show ticks': False, 'border width': 2, 'label offset': 0, 'color depiction': 'blended', 'label color': (1, 1, 1), 'font name': 'Sans Serif', 'tick length': 10, 'border color': (1, 1, 1, 1.0), 'key position': None, 'font typeface': 0, 'tick thickness': 4, 'colors/labels': [((0, 0, 1, 1), 'min'), ((1, 1, 1, 1), ''), ((1, 0, 0, 1), 'max')]})
except:
	reportRestoreError("Error restoring color key")



def restore2DLabelDialog(info):
	from chimera.dialogs import find
	from Ilabel.gui import IlabelDialog
	dlg = find(IlabelDialog.name)
	if dlg is not None:
		dlg.destroy()
	dlg = find(IlabelDialog.name, create=True)
	dlg._restoreSession(info)

import SimpleSession
SimpleSession.registerAfterModelsCB(restore2DLabelDialog, {'mouse func': 'labeling', 'sel ranges': (), 'dialog shown': 1})



def restoreRemainder():
	from SimpleSession.versions.v65 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip, restoreSilhouettes

	curSelIds =  []
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 4 }
	windowSize = (1250, 901)
	xformMap = {}
	fontInfo = {'face': ('Sans Serif', 'Normal', 16)}
	clipPlaneInfo = {}
	silhouettes = {0: True}

	replyobj.status("Restoring window...", blankAfter=0,
		secondary=True)
	restoreWindowSize(windowSize)
	replyobj.status("Restoring open states...", blankAfter=0,
		secondary=True)
	restoreOpenStates(xformMap)
	replyobj.status("Restoring font info...", blankAfter=0,
		secondary=True)
	restoreFontInfo(fontInfo)
	replyobj.status("Restoring selections...", blankAfter=0,
		secondary=True)
	restoreSelections(curSelIds, savedSels)
	replyobj.status("Restoring openModel attributes...", blankAfter=0,
		secondary=True)
	restoreOpenModelsAttrs(openModelsAttrs)
	replyobj.status("Restoring model clipping...", blankAfter=0,
		secondary=True)
	restoreModelClip(clipPlaneInfo)
	replyobj.status("Restoring per-model silhouettes...", blankAfter=0,
		secondary=True)
	restoreSilhouettes(silhouettes)

	replyobj.status("Restoring remaining extension info...", blankAfter=0,
		secondary=True)
try:
	restoreRemainder()
except:
	reportRestoreError("Error restoring post-model state")
from SimpleSession.versions.v65 import makeAfterModelsCBs
makeAfterModelsCBs()

from SimpleSession.versions.v65 import endRestore
replyobj.status('Finishing restore...', blankAfter=0, secondary=True)
endRestore({})
replyobj.status('', secondary=True)
replyobj.status('Restore finished.')

