## This is a sample case folder.

### Notes about the files contained.
1. Files that **should not be changed** under any circumstance: areas.txt, points.txt, surfaceNames.txt, skyDome.rad, manikinGeometry.rad
2. Files that may be changed (in case the building geometry is being changed. Let me know if you are changing these!): building.rad, viewAperture.rad    
3. File that **have to be changed**: fenestration.rad , fenestrationKlems.xml
4. If you are going to use a simple glass-based glazing, at the bare minimum the file fenestration.rad should contain the glass polygon and a compatible material definition.
5. In case you are using a fenestration with a complex geoemtry, then the file fenestration.rad must contain the geometry and materials for both the opaque object and the glass material. These have been shown in both the provided example folders.
6. The subfolders are optional. I can create them during runtime in case they are not present.
