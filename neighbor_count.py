#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Charles.Ferguson
#
# Created:     22/08/2016
# Copyright:   (c) Charles.Ferguson 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys, os, arcpy
oidLst = ['24724', '24725', '24726', '24727', '24728', '24729', '24730', '24731', '24732', '24733', '24734', '24735', '24736', '24737', '24738', '24739', '24740', '24741', '24742', '24743', '24744', '24745', '24746', '24747', '24748', '24749', '24750', '24751', '24752', '24753', '24754', '24755', '24756', '24757', '24758', '24759', '24760', '24761', '24762', '24763', '24764', '24765', '24766', '24767', '24768', '24769', '24770', '24771', '24772', '24773', '24774', '24775', '24776', '24777', '24778', '24779', '24780', '24781', '24782', '24783', '24784', '24785', '24786', '24787', '24788', '24789', '24790', '24791', '24792', '24793', '24794', '24795', '24796', '24797', '24798', '24799', '24800', '24801', '24802', '24803', '24804', '24805', '24806', '24807', '24808', '24809', '24810', '24811', '24812', '24813', '24814', '24815', '24816', '24817', '24818', '24819', '24820', '24821', '24822', '24823', '24824', '24825', '24826', '24827', '24828', '24829', '24830', '24831', '24832', '24833', '24834', '24835', '24836', '24837', '24838', '24839', '24840', '24841', '24842', '24843', '24844', '24845', '24846', '24847', '24848', '24849', '24850', '24851', '24852', '24853', '24854', '24855', '24856', '24857', '24858', '24859', '24860', '24861', '24862', '24863', '24864', '24865', '24866', '24867', '24868', '24869', '24870', '24871', '24872', '24873', '24874', '24875', '24876', '24877', '24878', '24879', '24880', '24881', '24882', '24883', '24884', '24885', '24886', '24887', '24888', '24889', '24890', '24891', '24892', '24893', '24894', '24895', '24896', '24897', '24898', '24899', '24900', '24901', '24902', '24903', '24904', '24905', '24906', '24907', '24908', '24909', '24910', '24911', '24912', '24913', '24914', '24915', '24916', '24917', '24918', '24919', '24920', '24921', '24922', '24923', '24924', '24925', '24926', '24927', '24928', '24929', '24930', '24931', '24932', '24933', '24934', '24935', '24936', '24937', '24938', '24939', '24940', '24941', '24942', '24943', '24944', '24945', '24946', '24947', '24948', '24949', '24950', '24951']

theLyr = r'D:\Chad\GIS\PROJECT\WAKE\QA_Check.gdb\wake_check\SoilLines_081816_Clip_Merge'

aStr = ''

n = 0
for e in oidLst:
    arcpy.management.MakeFeatureLayer(theLyr, "theGeom")

    attWC = '"OBJECTID" = ' + e
    arcpy.management.SelectLayerByAttribute("theGeom", "NEW_SELECTION", attWC)
    arcpy.management.SelectLayerByLocation("theGeom", "SHARE_A_LINE_SEGMENT_WITH", "theGeom", None, "ADD_TO_SELECTION")
    count = int(arcpy.management.GetCount("theGeom").getOutput(0))

    if count == 3:
        aStr = aStr + "'" + e + "',"
        n+=1


    print "Feature count for OID {} is {}".format(e, str(count))

    arcpy.management.Delete("theGeom")

aStr = aStr[:-1]
print aStr
print n

