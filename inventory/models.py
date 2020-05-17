from django.db import models

# Create your models here.

#class agtAgentTypes(models.Model):
#    agentTypeID = models.IntegerField(primary_key=True)
#    agentType = models.CharField(max_length=50)
#
#class agtAgents(models.Model):
#    agentID = models.IntegerField(primary_key=True)
#    divisionID = models.IntegerField()
#    corporationID = models.IntegerField()
#    locationID = models.IntegerField()
#    level = models.IntegerField()
#    quality = models.IntegerField()
#    agentTypeID = models.ForeignKey('inventory.agtAgentTypes')
#    isLocator = models.BooleanField()
#class agtResearchAgents(models.Model):
#class certCerts(models.Model):
#class certMasteries(models.Model):
#class certSkills(models.Model):
#class chrAncestries(models.Model):
#class chrAttributes(models.Model):
#class chrBloodlines(models.Model):
#class chrFactions(models.Model):
class chrRaces(models.Model):
    raceID = models.IntegerField(db_column='raceID', primary_key=True)
    raceName = models.CharField(db_column='raceName', max_length=100)
    description = models.CharField(db_column='description', max_length=1000)
    iconID = models.ForeignKey('inventory.eveIcons', db_column='iconID', on_delete=models.PROTECT)
    shortDescription = models.CharField(db_column='shortDescription', max_length=500)
    class Meta:
        managed = False
        db_table = 'chrRaces'

#class crpActivities(models.Model):
#class crpNPCCorporationDevisions(models.Model):
#class crpNPCCorporationResearchFields(models.Model):
#class crpNPCCorporationTrades(models.Model):
#class crpNPCCorporations(models.Model):
#class crpNPCDivisions(models.Model):
#class dmgAttributeCategories(models.Model):
#class dmgAttributeTypes(models.Model):
#class dmgEffects(models.Model):
#class dmgExpressions(models.Model):
#class dmgTypeAttributes(models.Model):
#class dmgTypeEffects(models.Model):
class eveGraphics(models.Model):
    graphicID = models.IntegerField(db_column='groupID', primary_key=True)
    sofFactionName = models.CharField(db_column='sofFactionName', max_length=100)
    graphicFile = models.CharField(max_length=100)
    sofHullName = models.CharField(max_length=100)
    sofRaceName = models.CharField(max_length=100)
    decription = models.TextField()
    class Meta:
        managed = False
        db_table = 'eveGraphics'

class eveSound(models.Model):
    def __str__(self):
        return self
    class Meta:
        managed = False
        db_table = 'eveSound'

class eveIcons(models.Model):
    iconID = models.IntegerField(primary_key=True)
    iconFile = models.CharField(max_length=500)
    description = models.TextField()
    class Meta:
        managed = False
        db_table = 'eveIcons'

#class eveUnits(models.Model):
#class industryActivity(models.Model):
#class industryActivityMaterials(models.Model):
#class industryActivityProbabilities(models.Model):
#class industryActivityProducts(models.Model):
#class industryActivityRaces(models.Model):
#class industryActivitySkills(models.Model):
#class industryBlueprints(models.Model):
class invCategories(models.Model):
    categoryID = models.IntegerField(primary_key=True)
    categoryName = models.CharField(max_length=100)
    iconID = models.ForeignKey('inventory.eveIcons', db_column='iconID', on_delete=models.PROTECT)
    published = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'invCategories'

#class invContrabandTypes(models.Model):
#class invControlTowerResourcePurposes(models.Model):
#class invControlTowerResources(models.Model):
#class invFlags(models.Model):

class invGroups(models.Model):
    groupID = models.IntegerField(db_column='groupID', primary_key=True)
    categoryID = models.ForeignKey('inventory.invCategories', db_column='categoryID', on_delete=models.PROTECT)
    groupName = models.CharField(max_length=100)
    iconID = models.ForeignKey('inventory.eveIcons', db_column='iconID', on_delete=models.PROTECT)
    useBasePrice = models.BooleanField()
    anchored = models.BooleanField()
    anchorable = models.BooleanField()
    fittableNonSingleton = models.BooleanField()
    published = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'invGroups'

#class invItems(models.Model):
class invMarketGroups(models.Model):
    marketGroupID = models.IntegerField(db_column='marketGroupID', primary_key=True)
    parentGroupID = models.ForeignKey('self', db_column='parentGroupID', on_delete=models.PROTECT)
    marketGroupName = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    iconID = models.ForeignKey('inventory.eveIcons', db_column='iconID', on_delete=models.PROTECT)
    hasTypes = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'invMarketGroups'

#class invMetaGroups(models.Model):
#class invMetaTypes(models.Model):
#class invNames(models.Model):
#class invPositions(models.Model):
#class invTraits(models.Model):
class invTypeMaterials(models.Model):
    productTypeID = models.ForeignKey('inventory.invTypes', db_column='typeID', related_name='product_id', on_delete=models.PROTECT)
    materialTypeID = models.ForeignKey('inventory.invTypes', db_column='materialTypeID', related_name='material_id', on_delete=models.PROTECT, primary_key=True)
    quantity = models.IntegerField(db_column='quantity')
    class Meta:
        managed = False
        db_table = 'invTypeMaterials'
        unique_together = (('productTypeID', 'materialTypeID'),)
#class invTypeReactions(models.Model):

class invTypes(models.Model):
    typeID = models.IntegerField(db_column='typeID', primary_key=True)
    groupID = models.ForeignKey('inventory.invGroups', db_column='groupID', on_delete=models.PROTECT)
    typeName = models.CharField(max_length=100)
    description = models.TextField()
    mass = models.FloatField()
    volume = models.FloatField()
    capacity = models.FloatField()
    portionSize = models.IntegerField()
    raceID = models.ForeignKey('inventory.chrRaces', db_column='raceID', on_delete=models.PROTECT)
    basePrice = models.DecimalField(max_digits=19, decimal_places=4)
    published = models.BooleanField()
    marketGroupID = models.ForeignKey('inventory.invMarketGroups', db_column='marketGroupID', on_delete=models.PROTECT)
    iconID = models.ForeignKey('inventory.eveIcons', db_column='iconID', on_delete=models.PROTECT)
    soundID = models.ForeignKey('inventory.eveSound', db_column='soundID', on_delete=models.PROTECT)
    graphicID = models.ForeignKey('inventory.eveGraphics', db_column='graphicID', on_delete=models.PROTECT)
    class Meta:
        managed = False
        db_table = 'invTypes'

#class invUniqueNames(models.Model):
#class invVolumes(models.Model):
#class mapCelestialStatistics(models.Model):
#class mapConstellationJumps(models.Model):
#class mapConstellations(models.Model):
#class mapDenormalize(models.Model):
#class mapJumps(models.Model):
#class mapLandmarks(models.Model):
#class mapLocationScenes(models.Model):
#class mapLocationWormholeClasses(models.Model):
#class mapRegionJumps(models.Model):
#class mapRegions(models.Model):
#class mapSolarSystemJumps(models.Model):
#class mapSolarSystems(models.Model):
#class mapUniverse(models.Model):
#class planetSchematics(models.Model):
#class planetSchematicsPinMap(models.Model):
#class planetSchematicsTypeMap(models.Model):
#class ramActivities(models.Model):
#class ramAssemblyLineStations(models.Model):
#class ramAssenblyLineTypeDetailPerCategory(models.Model):
#class ramAssenblyLineTypeDetailPerGroup(models.Model):
#class ramAssenblyLineTypes(models.Model):
#class ramInstallationTypeContents(models.Model):
#class skinLicense(models.Model):
#class skinMaterials(models.Model):
#class skinShip(models.Model):
#class skins(models.Model):
#class staOperationServices(models.Model):
#class staOperations(models.Model):
#class staService(models.Model):
#class staStationTypes(models.Model):
#class staStations(models.Model):
#class translationTables(models.Model):
class trnTranslationColumns(models.Model):
    tcGroupID = models.IntegerField(db_column='tcGroupID')
    tcID = models.IntegerField(db_column='tcID', primary_key=True)
    tableName = models.CharField(max_length=256, db_column='tableName')
    columnName = models.CharField(max_length=128, db_column='columnName')
    masterID = models.CharField(max_length=128, db_column='masterID')
    class Meta:
        managed = False
        db_table = 'trnTranslationColumns'

class trnTranslationLanguages(models.Model):
    numericLanguageID = models.IntegerField(db_column='numericLanguageID')
    languageID = models.CharField(max_length=50, db_column='languageID', primary_key=True)
    languageName = models.CharField(max_length=200, db_column='languageName')
    class Meta:
        managed = False
        db_table = 'trnTranslationLanguages'

class trnTranslations(models.Model):
    tcID = models.ForeignKey('inventory.trnTranslationColumns', db_column='tcID', related_name='trans_column_id', on_delete=models.PROTECT)
    keyID = models.ForeignKey('inventory.invTypes', db_column='keyID', related_name='type_id', on_delete=models.PROTECT, primary_key=True)
    languageID = models.ForeignKey('inventory.trnTranslationLanguages', db_column='languageID', on_delete=models.PROTECT)
    text = models.TextField()
    class Meta:
        managed = False
        db_table = 'trnTranslations'
        unique_together = (('tcID', 'keyID', 'languageID'),)
#class warCombatZoneSystems(models.Model):
#class warCombatZones(models.Model):
