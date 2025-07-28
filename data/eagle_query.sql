-- EAGLE Ref-L0100N1504: Core galaxy properties for centrals at z ~ 0.1
-- Save this file as data/EAGLE_data.csv

SELECT
    GalaxyID,
    MassType_Star as StellarMass,
    StarFormationRate as SFR,
    BlackHoleMass,
    BlackHoleMassAccretionRate,
    SubGroupNumber,
    SnapNum
FROM
    RefL0100N1504_SubHalo
WHERE
    SnapNum = 28           -- z ~ 0.1
    AND SubGroupNumber = 0 -- Only central galaxies
