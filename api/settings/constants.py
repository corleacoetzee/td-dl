

IMPACT_ANALYSIS_LEVELS = "(r:Resource)<-[D:DEPENDS{levels}]-(n:Resource)"
LINEAGE_ANALYSIS_LEVELS = "(r:Resource)-[D:DEPENDS{levels}]->(n:Resource)"

IMPACT_ANALYSIS = "(g_ini:Resource)<-[D:DEPENDS]-(r:Resource)"
LINEAGE_ANALYSIS = "(g_ini:Resource)-[D:DEPENDS]->(r:Resource)"