###########################################
#
# iLCSoft versions for release v01-11
#
# F.Gaede, DESY 07.10.2010
#
###########################################


# --------- ilcsoft release version ------------------------------------------
ilcsoft_release='v01-11-pre'
# ----------------------------------------------------------------------------


# --------- install dir ------------------------------------------------------
#ilcsoft_install_prefix = "/scratch/$USER/ilcsoft/"
ilcsoft_install_prefix = ilcsoft_afs_path[ arch ]
#ilcsoft_install_dir = os.path.join( ilcsoft_install_prefix, ilcsoft_release )
# ----------------------------------------------------------------------------


# --------- ilcsoft home -----------------------------------------------------
# python variable for referring the ILC Home directory
# used to link or use already installed packages (SL4 or SL5)
# no need to set this variable if using SL4 or SL5 with access to /afs/desy.de/
#ilcPath = '/afs/desy.de/project/ilcsoft/sw/i386_gcc34_sl4/'
#ilcPath = ilcsoft_afs_path[ arch ]
# ----------------------------------------------------------------------------



# ======================= PACKAGE VERSIONS ===================================


ROOT_version = "5.27.06"

MySQL_version = "5.0.45"

Java_version = "1.6.0"

Geant4_version = "9.3.p02"

CERNLIB_version = "2006" 

CLHEP_version = "2.0.4.5" 

GSL_version = "1.8" 

QT_version = "4.2.2" 

CMake_version = "2.8.3" 



# -------------------------------------------

LCIO_version = "v01-51-02" # update?

GEAR_version = "v00-17-pre"

CED_version = "v01-01-01" # update?

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-2" # update?

#CMakeModules_version = "v01-10-01" # DEPRECATED
ILCUTIL_version = "v00-01-pre"

dcap_version = "1.9.5-5" # remove?

FastJet_version = "2.4.2"
FastJetClustering_version = "v00-01" # TODO


StandardConfig_version = "v02-02" # update?
MokkaDBConfig_version = "v02-02"
LCFI_MokkaBasedNets_version = "v00-01" 



# -------------------------------------------

KalTest_version = "v01-00" # TODO

KalDet_version = "v01-00" # TODO

LCCD_version = "v01-02-pre"

RAIDA_version = "v01-06-pre" 

MarlinUtil_version = "v01-02-pre"

Marlin_version = "v00-13-01" # TODO

Mokka_version = "mokka-07-06" # update?

MarlinReco_version = "v00-19" # TODO

PandoraPFA_version = "v03-02-02" # update/remove??

PandoraPFANew_version = "v00-04" # TODO
MarlinPandora_version = "v00-03" # TODO

LCFIVertex_version = "v00-04" # TODO

CEDViewer_version = "v01-01-01" # TODO

Overlay_version = "v00-08" # TODO

Eutelescope_version = "v00-04-04" # TODO    

MarlinTPC_version = "v00-08-03" # TODO

SiliconDigi_version = "v00-04-02" # update/remove??

Druid_version = "1.8" 

Garlic_version = "v2.0.3" # TODO
