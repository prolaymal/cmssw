import FWCore.ParameterSet.Config as cms

process = cms.Process("Dump")

process.load('FWCore.MessageService.MessageLogger_cfi')

process.load('Geometry.GEMGeometry.cmsExtendedGeometryPostLS1plusGEMXML_cfi')
process.load('Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi')
process.load('Geometry.CommonDetUnit.globalTrackingGeometry_cfi')
process.load('Geometry.MuonNumbering.muonNumberingInitialization_cfi')
process.load('Geometry.GEMGeometry.gemGeometry_cfi')
process.load('Geometry.TrackerGeometryBuilder.idealForDigiTrackerGeometryDB_cff')
process.load('Geometry.DTGeometryBuilder.idealForDigiDtGeometryDB_cff')
process.load('Geometry.CSCGeometryBuilder.idealForDigiCscGeometry_cff')


process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'POSTLS161_V12::All'


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:out_digi.root'
    )
)

process.dumper = cms.EDAnalyzer("GEMDigiReader"
    simhitToken = cms.InputTag("g4SimHits","MuonGEMHits"), 
    gemDigiToken = cms.InputTag("simMuonGEMDigis"), 
    gemDigiSimLinkToken = cms.InputTag("simMuonGEMDigis","GEM") 
)

process.p    = cms.Path(process.dumper)

